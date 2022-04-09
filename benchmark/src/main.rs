#![deny(warnings)]

use std::time::{Duration, Instant};
use tokio::task;
use std::io::prelude::*;
use std::fs::OpenOptions;

async fn process(path: &str, thread_num: i32) {
    let client = reqwest::Client::new();
    let mut total_duation = Duration::new(0, 0);
    let num_of_trials = 10;
    let thread_path = path.to_string();
    let thread_str = thread_num.to_string();

    let mut file = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .append(true)
            .open(thread_path + "data" + &thread_str + ".txt").unwrap();

    for _number in 0..num_of_trials {
        let start = Instant::now();
        let _res = client.post("http://localhost:8080/login")
        .body("0cxRnyQ0YqPP45TzcHFFxEX97Uekj")
        .send()
        .await;

        let duration = start.elapsed();
        file.write(format!("{:?} ", duration).as_bytes()).unwrap();
        total_duation += duration;
    }

    file.write("\n".as_bytes()).unwrap();
}


#[tokio::main]
async fn main(){

    let num_of_threads = 5;
    let mut handles = Vec::new();
    let path = "C:\\Waterloo\\Class\\CS 654\\Project\\Research\\experiment_data\\";

    for _num in 0..num_of_threads {
        let join_handle: task::JoinHandle<_> = tokio::spawn(async move {
            process(path, _num).await
        });
        
        handles.push(join_handle);
    }

    futures::future::join_all(handles).await;
}