use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use redis::cluster::ClusterClient;
use redis::Commands;
use redis::RedisResult;
use std::sync::Mutex;

pub struct TokenServer {
	nodes: Mutex<Vec<String>>,
	client: Mutex<redis::cluster::ClusterClient>,
}

impl TokenServer {
	pub fn new(&mut self) -> TokenServer {
		TokenServer {
			nodes: Mutex::new(vec![
				"redis://127.0.0.1:7000/".to_string(),
				"redis://127.0.0.1:7001/".to_string(),
				"redis://127.0.0.1:7002/".to_string(),
				"redis://127.0.0.1:7003/".to_string(),
				"redis://127.0.0.1:7004/".to_string(),
				"redis://127.0.0.1:7005/".to_string(),
			]),
			client: Mutex::new(
				redis::cluster::ClusterClient::open(self.nodes.get_mut().unwrap().to_vec())
					.unwrap(),
			),
		}
	}

	pub fn token_generator(&mut self) -> String {
		let rand_token: String = thread_rng()
			.sample_iter(&Alphanumeric)
			.take(30)
			.map(char::from)
			.collect();

		let token_copy = rand_token.clone();
		let tolen_return = token_copy.clone();

		let mut connection = self.client.get_mut().unwrap().get_connection().unwrap();
		let _: () = connection.set(token_copy, "0").unwrap();

		return tolen_return;
	}

	pub fn get_token(&mut self) {
		let token = self.token_generator();
	}
}

#[get("/")]
async fn hello() -> impl Responder {
	HttpResponse::Ok().body("Hey there!")
}

#[post("/login")]
async fn login(mut data: web::Data<TokenServer>) -> String {
	let rand_token: String = thread_rng()
		.sample_iter(&Alphanumeric)
		.take(30)
		.map(char::from)
		.collect();

	let mut client_copy = data.client.lock().unwrap();
	let token_copy = rand_token.clone();
	let token_print = token_copy.clone();
	let mut connection = client_copy.get_connection().unwrap();
	let _: () = connection.set(token_copy, "exist").unwrap();

	format!("Hello {}!", token_print)
}

#[post("/verify")]
async fn verify(req_body: String, mut data: web::Data<TokenServer>) -> String {
	let mut client_copy = data.client.lock().unwrap();
	let mut connection = client_copy.get_connection().unwrap();
	let rv: RedisResult<String> = connection.get(req_body);

	if let Ok(_) = rv {
		"successs".to_string()
	} else {
		"failure".to_string()
	}
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
	let original_nodes = vec![
		"redis://127.0.0.1:7000/",
		"redis://127.0.0.1:7001/",
		"redis://127.0.0.1:7002/",
		"redis://127.0.0.1:7003/",
		"redis://127.0.0.1:7004/",
		"redis://127.0.0.1:7005/",
	];

	let server = web::Data::new(TokenServer {
		nodes: Mutex::new(vec![
			"redis://127.0.0.1:7000/".to_string(),
			"redis://127.0.0.1:7001/".to_string(),
			"redis://127.0.0.1:7002/".to_string(),
			"redis://127.0.0.1:7003/".to_string(),
			"redis://127.0.0.1:7004/".to_string(),
			"redis://127.0.0.1:7005/".to_string(),
		]),
		client: Mutex::new(redis::cluster::ClusterClient::open(original_nodes).unwrap()),
	});

	HttpServer::new(move || {
		App::new()
			.app_data(server.clone())
			.service(hello)
			.service(login)
			.service(verify)
	})
	.bind("127.0.0.1:8080")?
	.run()
	.await
}
