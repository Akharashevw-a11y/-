import json
import os

FILE = "stock.json"


def load_stock():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_stock(stock):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(stock, f, ensure_ascii=False, indent=4)


def add_tire(brand, size, season, quantity):
    stock = load_stock()

    tire = {
        "brand": brand,
        "size": size,
        "season": season,
        "quantity": quantity
    }

    stock.append(tire)
    save_stock(stock)


def get_stock():
    return load_stock()
