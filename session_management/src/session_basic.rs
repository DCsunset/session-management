use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use rand::{thread_rng, Rng};
use std::sync::Mutex;
use rand::distributions::Alphanumeric;

pub struct TokenServer {
    tokens: Mutex<Vec<String>>
}

impl TokenServer {
    pub fn new() -> TokenServer {
        TokenServer {
            tokens: Mutex::new(Vec::new())
        }
    }

    pub fn token_generator(&mut self) -> String {

        let rand_token: String = thread_rng()
            .sample_iter(&Alphanumeric)
            .take(30)
            .map(char::from)
            .collect();

        let token_copy = rand_token.clone();
        self.tokens.get_mut().unwrap().push(rand_token);

        return token_copy;
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

    let mut tokens_copy = data.tokens.lock().unwrap();
    let rand_token_copy = rand_token.clone();
    tokens_copy.push(rand_token);
    format!("Hello {}!", rand_token_copy)
}

#[post("/verify")]
async fn verify(req_body: String, mut data: web::Data<TokenServer>) -> String {
    let mut tokens_copy = data.tokens.lock().unwrap();

    if (*tokens_copy).contains(&req_body) {
        format!("Success!")
    }
    else {
        format!("Failed!")
    }
}



#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let server = web::Data::new(TokenServer {
        tokens: Mutex::new(vec![]),
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