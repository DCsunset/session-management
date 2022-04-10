use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use redis::cluster::ClusterClient;
use redis::Commands;
use redis::RedisResult;
use std::sync::Mutex;

pub struct TokenServer {
	client: Mutex<redis::cluster::ClusterClient>,
	conn: Mutex<redis::cluster::ClusterConnection>
}

impl TokenServer {
	pub fn new(client: redis::cluster::ClusterClient) -> TokenServer {
		let conn = client.get_connection().unwrap();
		TokenServer {
			client: Mutex::new(client),
			conn: Mutex::new(conn)
		}
	}

	pub fn generate_token(&self) -> String {
		let rand_token: String = thread_rng()
			.sample_iter(&Alphanumeric)
			.take(30)
			.map(char::from)
			.collect();

		let token_copy = rand_token.clone();

		let mut conn = self.conn.lock().unwrap();
		let rv: redis::RedisResult<()> = conn.set(token_copy, "0");
		match rv {
			Ok(_) => rand_token,
			Err(_) => "".to_string()
		}
	}

	pub fn verify_token(&self, token: String) -> bool {
		let mut conn = self.conn.lock().unwrap();
		let rv: RedisResult<String> = conn.get(token);
		match rv {
			Ok(_) => true,
			Err(_) => false
		}
	}
}

#[get("/")]
async fn hello() -> impl Responder {
	HttpResponse::Ok().body("Hey there!")
}

#[post("/login")]
async fn login(mut data: web::Data<TokenServer>) -> String {
	let token = data.generate_token();
	format!("Hello {}!", token)
}

#[post("/verify")]
async fn verify(req_body: String, mut data: web::Data<TokenServer>) -> String {
	let result = data.verify_token(req_body);
	if result {
		"success".to_string()
	} else {
		"failure".to_string()
	}
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
	let client = redis::cluster::ClusterClient::open(vec!["redis://127.0.0.1:4902/"]).unwrap();

	let server = web::Data::new(TokenServer::new(client));

	HttpServer::new(move || {
		App::new()
			.app_data(server.clone())
			.service(hello)
			.service(login)
			.service(verify)
	})
	.bind("0.0.0.0:8080")?
	.run()
	.await
}
