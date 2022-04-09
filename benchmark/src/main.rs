#![deny(warnings)]

use std::time::{Instant};
use tokio::task;
use std::io::prelude::*;
use std::fs::OpenOptions;

async fn test_login(path: &str, thread_num: i32, num_of_trials: i32) {
    let client = reqwest::Client::new();
    let thread_path = path.to_string();
    let thread_str = thread_num.to_string();

    let mut file = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .append(true)
            .open(thread_path + "\\login\\data" + &thread_str + ".txt").unwrap();

    for _number in 0..num_of_trials {
        let start = Instant::now();
        let _res = client.post("http://localhost:8080/login")
        .send()
        .await;

        let duration = start.elapsed();
        file.write(format!("{:?} ", duration).as_bytes()).unwrap();
    }

    file.write("\n".as_bytes()).unwrap();
}

async fn test_verify(path: &str, thread_num: i32, num_of_trials: i32) {
    let client = reqwest::Client::new();
    let thread_path = path.to_string();
    let thread_str = thread_num.to_string();

    let mut file = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .append(true)
            .open(thread_path + "\\verify\\data" + &thread_str + ".txt").unwrap();

    for _number in 0..num_of_trials {
        let start = Instant::now();
        let _res = client.post("http://localhost:8080/verify")
        .body("DeJ4R0EdFEMT5QC2LErpFgcdb27jUi")
        .send()
        .await;

        let duration = start.elapsed();
        file.write(format!("{:?} ", duration).as_bytes()).unwrap();
    }

    file.write("\n".as_bytes()).unwrap();
}

#[tokio::main]
async fn main(){

    let num_of_threads = 5;
    let num_of_trials = 100;
    let mut handles_login = Vec::new();
    let path = "C:\\Waterloo\\Class\\CS 654\\Project\\Research\\experiment_data\\";

    for _num in 0..num_of_threads {
        let join_handle: task::JoinHandle<_> = tokio::spawn(async move {
            test_login(path, _num, num_of_trials).await
        });
        
        handles_login.push(join_handle);
    }

    futures::future::join_all(handles_login).await;

    let mut handles_verify = Vec::new();

    for _num in 0..num_of_threads {
        let join_handle: task::JoinHandle<_> = tokio::spawn(async move {
            test_verify(path, _num, num_of_trials).await
        });
        
        handles_verify.push(join_handle);
    }

    futures::future::join_all(handles_verify).await;
}