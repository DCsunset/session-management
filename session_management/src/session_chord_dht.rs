use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use rand::{thread_rng, Rng};
use std::sync::Mutex;
use std::collections::HashSet;
use rand::distributions::Alphanumeric;
use chord_dht::{
	client::setup_client
};
use session_management::TokenStore;
use async_trait::async_trait;

pub struct ChordDht {
	client: chord_dht::rpc::NodeServiceClient
}

impl ChordDht {
	pub async fn new(server_addr: &str) -> Self {
		Self {
			client: setup_client(server_addr).await
		}
	}
}

#[async_trait]
impl TokenStore for ChordDht {
	async fn contains(&self, token: String) -> bool {
		let result = self.client.get_rpc(
			tarpc::context::current(),
			token.as_bytes().to_vec()
		).await.unwrap();

		match result {
			Some(_) => true,
			None => false
		}
	}

	async fn insert(&self, token: String) {
		self.client.set_rpc(
			tarpc::context::current(),
			token.as_bytes().to_vec(),
			Some(Vec::new())
		).await.unwrap();
	}
}

#[post("/login")]
async fn login(data: web::Data<ChordDht>) -> String {
    let rand_token: String = thread_rng()
        .sample_iter(&Alphanumeric)
        .take(30)
        .map(char::from)
        .collect();

		data.insert(rand_token.clone());
    format!("Hello {}!", rand_token)
}

#[post("/verify")]
async fn verify(req_body: String, data: web::Data<ChordDht>) -> String {
	if data.contains(req_body).await {
		format!("Success!")
	}
	else {
		format!("Failed!")
	}
}


#[actix_web::main]
async fn main() -> std::io::Result<()> {
	let server = web::Data::new(
		ChordDht::new("localhost:9600")
	);

	HttpServer::new(move || {
			App::new()
					.app_data(server.clone())
					.service(login)
					.service(verify)
	})
	.bind("127.0.0.1:8080")?
	.run()
	.await
}
