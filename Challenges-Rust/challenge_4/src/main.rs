use std::io::{self, Write};

fn main() {
    let first_name = input("What's your first name? ");
    let last_name = input("What's your last name? ");
    println!("Your full name is {} {}", first_name, last_name);
}

fn input(print_text: &str) -> String {
    print!("{}", print_text);
    io::stdout().flush().unwrap();
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}
