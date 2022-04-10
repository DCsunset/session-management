use std::time::{Instant};
use tokio::task;
use std::io::prelude::*;
use std::fs::OpenOptions;
use std::io::BufReader;
use std::collections::HashMap;
use rand::prelude::*;

async fn test_login(path: &str, thread_num: i32, num_of_trials: i32) {
    let client = reqwest::Client::new();
    let thread_path = path.to_string();
    let thread_path_copy = path.to_string().clone();
    let thread_str = thread_num.to_string();

    let mut file = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .append(true)
        .open(thread_path + "/login/data" + &thread_str + ".txt").unwrap();

    let mut token = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .append(true)
        .open(thread_path_copy + "/token/token" + &thread_str + ".txt").unwrap();

    for _number in 0..num_of_trials {
        let start = Instant::now();
        let _res = client.post("http://10.10.0.1:8080/login")
        .send()
        .await;

        let duration = start.elapsed();
        let data = match _res {
            Ok(r) => {
                r.text().await
            },
            Err(_) => {
                file.write(format!("-{:?} ", duration).as_bytes()).unwrap();
                continue;
            }
        };

        let token_str = format!("{:?} \n", data);

        if token_str.len() < 40 {
            file.write(format!("-{:?} ", duration).as_bytes()).unwrap();
        }
        else {
            file.write(format!("{:?} ", duration).as_bytes()).unwrap();
            let token_slice = &token_str[10..40];
            token.write(token_slice.as_bytes()).unwrap();
            token.write("\n".as_bytes()).unwrap();
        }
    }

    file.write("\n".as_bytes()).unwrap();
}


async fn test_verify(path: &str, thread_num: i32, num_of_trials: i32) {
    let client = reqwest::Client::new();
    let thread_path = path.to_string();
    let thread_path_copy = path.to_string().clone();
    let thread_str = thread_num.to_string();

    let mut file = OpenOptions::new()
        .read(true)
        .write(true)
        .create(true)
        .append(true)
        .open(thread_path + "/verify/data" + &thread_str + ".txt").unwrap();
    
    let token = OpenOptions::new()
        .read(true)
        .open(thread_path_copy + "/token/token" + &thread_str + ".txt").unwrap();
    
    let tokens = BufReader::new(token);
    let mut token_map = HashMap::new();
    let mut number = 1;

    for line in tokens.lines() {
        token_map.insert(number, line.unwrap());
        number += 1;
    }

    for index in 1..number {
        let token = token_map.get(&index).unwrap().clone();

        let start = Instant::now();
        let _res = client.post("http://10.10.0.1:8080/verify")
        .body(token)
        .send()
        .await;
        let duration = start.elapsed();

        let data = match _res {
            Ok(r) => {
                r.text().await
            },
            Err(_) => {
                file.write(format!("-{:?} ", duration).as_bytes()).unwrap();
                continue;
            }
        };

        if let Ok(v) = data {
            if v == "success" {
                file.write(format!("{:?} ", duration).as_bytes()).unwrap();
            }
        }
        file.write(format!("-{:?} ", duration).as_bytes()).unwrap();
        
    }

    file.write("\n".as_bytes()).unwrap();
}

#[tokio::main]
async fn main(){
    let args: Vec<_> = std::env::args().collect();
    let num_of_threads = args[1].parse().unwrap();
    let num_of_trials = 4000;
    let mut handles_login = Vec::new();
    let path = "./experiment_data/";

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