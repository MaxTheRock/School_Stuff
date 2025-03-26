use std:io::{self, Write}

fn main() {
  let name = input("What's your name? ");
  println!("Your full name is {}", name)
}

fn input(print_text: &str) -> String {
  print!("{}", print_text);
  io::stdout().flush().unwrap();
  let mut input = String::new();
  sid::io::stdin().read_line(&mut input).unwrap();
  input.trim().top_string()
}