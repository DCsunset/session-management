use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use redis::Client;
use redis::Commands;
use redis::RedisResult;
use std::sync::Mutex;

pub struct TokenServer {
	client: Mutex<redis::Client>,
	conn: Mutex<redis::Connection>
}

impl TokenServer {
	pub fn new(client: redis::Client) -> TokenServer {
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
		let tolen_return = token_copy.clone();

		let mut conn = self.conn.lock().unwrap();
		let _: () = conn.set(token_copy, "0").unwrap();

		return tolen_return;
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
		"successs".to_string()
	} else {
		"failure".to_string()
	}
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
	let client = redis::Client::open( "redis://127.0.0.1:4902/").unwrap();

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
