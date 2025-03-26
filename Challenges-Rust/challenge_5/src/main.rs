use std::io::{self, Write};

fn main() {
    let num1 = int(&input("Enter a number: "));
    let num2 = int(&input("Enter a number: "));
    println!("The sum of the numbers is: {}", num1 + num2);
}

fn input(print_text: &str) -> String {
    print!("{}", print_text);
    io::stdout().flush().unwrap();
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}

fn int(string: &str) -> i32 {
    string.parse().expect("Please enter a valid number")
}