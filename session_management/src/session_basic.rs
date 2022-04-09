use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use std::collections::HashSet;
use std::sync::Mutex;

pub struct TokenServer {
	tokens: Mutex<HashSet<String>>,
}

#[get("/")]
async fn hello() -> impl Responder {
	HttpResponse::Ok().body("Hey there!")
}

#[post("/login")]
async fn login(data: web::Data<TokenServer>) -> String {
	let rand_token: String = thread_rng()
		.sample_iter(&Alphanumeric)
		.take(30)
		.map(char::from)
		.collect();

	let mut tokens_copy = data.tokens.lock().unwrap();
	let rand_token_copy = rand_token.clone();
	tokens_copy.insert(rand_token);
	format!("Hello {}!", rand_token_copy)
}

#[post("/verify")]
async fn verify(req_body: String, data: web::Data<TokenServer>) -> String {
	let tokens_copy = data.tokens.lock().unwrap();

	if (*tokens_copy).contains(&req_body) {
		format!("Success!")
	} else {
		format!("Failed!")
	}
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
	let server = web::Data::new(TokenServer {
		tokens: Mutex::new(HashSet::new()),
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
