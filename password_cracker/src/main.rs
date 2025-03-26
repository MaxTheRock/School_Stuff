use rpassword::read_password;
use std::thread::sleep;
use std::time::Duration;
use std::io::{self,Write};

fn main() {
    println!("Welcome to Max's password cracker!");
    println!("");
    print!("Enter your password >> ");
    io::stdout().flush().expect("Failed to flush stdout");

    let password = read_password().expect("Failed to read password");

    println!("");
    sleep(Duration::from_secs(1));
    println!("Checking Algorithm");
    sleep(Duration::from_secs(1));
    println!("Reading your mind");
    sleep(Duration::from_secs(1));
    println!("Error handling and correction");
    sleep(Duration::from_secs(1));
    println!("Reading personal information");
    sleep(Duration::from_secs(2));
    println!("Eating a cookie 🍪");
    sleep(Duration::from_secs(1));
    println!("");
    println!("Password Summary:");
    println!("  Value [{}]", password);
    println!("  Type [String]");
    println!("  Length [{}]", password.len());
}
