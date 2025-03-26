from rich import box
from rich.table import Table
from rich.console import Console
from rich.text import Text
import random
import time

def clear_screen():
  print("\033c")

stock = {
  "🧀 Cheese": 0.50,
  "💧 Water": 0.20,
  "🍕 Pizza": 1.20,
  "🍎 Apple": 0.25,
  "🍞 Bread": 1.00,
  "🥛 Milk": 0.80,
  "🍫 Chocolate": 1.50,
  "🍌 Banana": 0.30,
  "🍇 Grapes": 2.00,
  "🍓 Strawberry": 1.75,
  "🍊 Orange": 0.60,
  "🍋 Lemon": 0.40,
  "🍒 Cherry": 2.50,
  "🍍 Pineapple": 3.00,
  "🥕 Carrot": 0.45,
  "🥦 Broccoli": 1.10,
  "🍅 Tomato": 0.70,
  "🥔 Potato": 0.35,
  "🍗 Chicken": 4.50,
  "🥩 Steak": 7.00,
  "🍤 Shrimp": 5.00,
  "🍣 Sushi": 8.00,
  "🍜 Noodles": 2.50,
  "🍲 Soup": 3.00,
  "🍿 Popcorn": 1.25,
  "🍪 Cookie": 0.75,
  "🍩 Donut": 1.00,
  "🍰 Cake": 2.50,
  "🍦 Ice Cream": 1.75,
  "🍭 Lollipop": 0.50,
  "🍺 Beer": 2.00,
  "🍷 Wine": 10.00,
  "🍸 Cocktail": 5.50,
  "🍹 Juice": 1.50,
  "🍵 Tea": 1.00,
  "☕ Coffee": 1.20,
}

customer = {}

def add_to_cart():
  item, price = random.choice(list(stock.items()))
  if item in customer:
    customer[item] += price
  else:
    customer[item] = price

# Add rows to the table
def display_rows():
  table = Table(box=box.ROUNDED)
  table.add_column("", justify="center")
  table.add_column("Items")
  table.add_column("Price")
  for item, price in customer.items():
    emoji, item_name = item.split(' ', 1)
    table.add_row(emoji, item_name, f"{price:.2f}")
  table.add_row("", "", "")  # Add a separator line
  total_price = sum(customer.values())
  table.add_row("📠", Text("Total", style="bold"), Text(f"{total_price:.2f}", style="bold"))
  return table

# Create a console object
console = Console()

for i in range(10):
  add_to_cart()
  clear_screen()
  table = display_rows()
  console.print(table)
  time.sleep(0.2)

clear_screen()
table = display_rows()
console.print(table)
