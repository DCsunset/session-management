#![deny(warnings)]

use std::time::{Duration, Instant};

// This is using the `tokio` runtime. You'll need the following dependency:
//
// `tokio = { version = "1", features = ["full"] }`
#[cfg(not(target_arch = "wasm32"))]
#[tokio::main]
async fn main() -> Result<(), reqwest::Error> {

    let client = reqwest::Client::new();
    let mut total_duation = Duration::new(0, 0);
    let num_of_trials = 10000;

    for _number in 1..num_of_trials {
        let start = Instant::now();
        let _res = client.post("http://localhost:8080/login")
        .body("0cxRnyQ0YqPP45TzcHFFxEX97Uekj")
        .send()
        .await?;

        let duration = start.elapsed();
        total_duation += duration;
    }

    println!("Number of trials is: {:?}", num_of_trials);
    println!("Time elapsed in login(average) is: {:?}", total_duation / num_of_trials);
    
    Ok(())
}

// The [cfg(not(target_arch = "wasm32"))] above prevent building the tokio::main function
// for wasm32 target, because tokio isn't compatible with wasm32.
// If you aren't building for wasm32, you don't need that line.
// The two lines below avoid the "'main' function not found" error when building for wasm32 target.
#[cfg(target_arch = "wasm32")]
fn main() {}