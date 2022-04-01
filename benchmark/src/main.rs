#![deny(warnings)]

use std::time::{Duration, Instant};


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
