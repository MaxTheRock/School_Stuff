use std::io;

fn main() {
  let mut name = String::new();
  io::stdin()
    .read_line(&mut name)
    .expect("Failed to read line");

  let mut age = String::new();
  io::stdin()
    .read_line(&mut age)
    .expect("Failed to read line");

  let mut color = String::new();
  io::stdin()
      .read_line(&mut color)
      .expect("Failed to read line");

  println!("");
  println!("Name: {name}");
  println!("Age: {age}");
  println!("Colour: {color}");
}
