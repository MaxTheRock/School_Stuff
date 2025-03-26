use std::io;

fn add(number1, number2) {
  return number1 + number2
}

fn main() {
    let mut num1 = String::new();
    io::stdin()
      .read_line(&mut num1)
      .expect("Failed to read line");

    let int1: i32 = num1.trim().parse().expect("Not a valid number");

    let mut num2 = String::new();
    io::stdin()
      .read_line(&mut num2)
      .expect("Failed to read line");
    
    let int2: i32 = num2.trim().parse().expect("Not a valid number");

    println!("{}", int1 + int2)
}
