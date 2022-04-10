use actix_web::{post, web, App, HttpServer};
use async_trait::async_trait;
use chord_dht::client::setup_client;
use rand::distributions::Alphanumeric;
use rand::{thread_rng, Rng};
use session_management::TokenStore;

pub struct ChordDht {
	client: chord_dht::rpc::NodeServiceClient,
}

impl ChordDht {
	pub async fn new(server_addr: &str) -> anyhow::Result<Self> {
		let client = setup_client(server_addr).await?;
		Ok(Self { client: client })
	}
}

#[async_trait]
impl TokenStore for ChordDht {
	async fn contains(&self, token: String) -> bool {
		let result = self
			.client
			.get_rpc(tarpc::context::current(), token.as_bytes().to_vec())
			.await
			.unwrap();

		match result {
			Some(_) => true,
			None => false,
		}
	}

	async fn insert(&self, token: String) {
		self.client
			.set_rpc(
				tarpc::context::current(),
				token.as_bytes().to_vec(),
				Some(Vec::new()),
			)
			.await
			.unwrap();
	}
}

#[post("/login")]
async fn login(data: web::Data<ChordDht>) -> String {
	let rand_token: String = thread_rng()
		.sample_iter(&Alphanumeric)
		.take(30)
		.map(char::from)
		.collect();

	data.insert(rand_token.clone()).await;
	format!("Hello {}!", rand_token)
}

#[post("/verify")]
async fn verify(req_body: String, data: web::Data<ChordDht>) -> String {
	if data.contains(req_body).await {
		format!("success")
	} else {
		format!("failure")
	}
}

#[actix_web::main]
async fn main() -> anyhow::Result<()> {
	let dht = ChordDht::new("localhost:5902").await?;
	let server = web::Data::new(dht);

	HttpServer::new(move || {
		App::new()
			.app_data(server.clone())
			.service(login)
			.service(verify)
	})
	.bind("127.0.0.1:8080")?
	.run()
	.await?;

	Ok(())
}
