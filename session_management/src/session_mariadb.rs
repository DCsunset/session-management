use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use mysql::prelude::*;
use mysql::*;
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use std::sync::Mutex;

#[derive(Debug, PartialEq, Eq)]
pub struct Session {
	token: String,
	value: String,
}

pub struct TokenServer {
	url: Mutex<String>,
	pool: Mutex<Pool>,
	connection: Mutex<PooledConn>,
}

impl TokenServer {
	pub fn token_generator(&mut self) -> String {
		let rand_token: String = thread_rng()
			.sample_iter(&Alphanumeric)
			.take(30)
			.map(char::from)
			.collect();

		let mut pool_copy = self.pool.lock().unwrap();
		let token_copy = rand_token.clone();
		let token_return = token_copy.clone();

		return token_return;
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

	let token_copy = rand_token.clone();
	let token_print = token_copy.clone();
	let mut connection = data.connection.lock().unwrap();

	connection
		.exec_drop(
			"INSERT INTO sessions (token, value)
        VALUES (:token, :value)",
			params! {
					"token" => token_copy,
					"value" => "success",
			},
		)
		.unwrap();

	format!("Hello {}!", token_print)
}

#[post("/verify")]
async fn verify(req_body: String, mut data: web::Data<TokenServer>) -> String {
	let mut connection = data.connection.lock().unwrap();

	let rv: Option<String> = connection
		.exec_first(
			"select token from sessions where token = :token",
			params! {
				"token" => req_body
			},
		)
		.unwrap();

	if let Some(_) = rv {
		"successs".to_string()
	} else {
		"failure".to_string()
	}
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
	let original_url: &str = "mysql://root@localhost:3901/session_rust";
	let original_pool = Pool::new(Opts::from_url(original_url).unwrap()).unwrap();
	let mut original_connection = original_pool.get_conn().unwrap();

	original_connection.query_drop(
		"CREATE TEMPORARY TABLE sessions (
        token text not null,
        value text
    )",
	);

	let server = web::Data::new(TokenServer {
		url: Mutex::new(original_url.to_string()),
		pool: Mutex::new(original_pool),
		connection: Mutex::new(original_connection),
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
