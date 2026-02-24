from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = "spicegarden2024"

MENU = {
    "Starters": {
        "Veg Spring Roll": 120,
        "Chicken Tikka": 220,
        "Paneer Tikka": 180,
        "Samosa (2 pcs)": 60,
    },
    "Main Course": {
        "Butter Chicken": 280,
        "Paneer Butter Masala": 240,
        "Dal Makhani": 200,
        "Biryani (Chicken)": 260,
        "Biryani (Veg)": 200,
    },
    "Breads": {
        "Naan": 40,
        "Tandoori Roti": 30,
        "Paratha": 50,
        "Puri (2 pcs)": 40,
    },
    "Beverages": {
        "Lassi": 80,
        "Cold Drink": 60,
        "Masala Chai": 40,
        "Fresh Lime Soda": 70,
    },
    "Desserts": {
        "Gulab Jamun (2 pcs)": 80,
        "Ice Cream": 100,
        "Rasgulla (2 pcs)": 70,
        "Kheer": 90,
    },
}

GST_RATE = 0.05
SERVICE_RATE = 0.10

CATEGORY_ICONS = {
    "Starters": "🥗",
    "Main Course": "🍛",
    "Breads": "🫓",
    "Beverages": "🥤",
    "Desserts": "🍮",
}

@app.route("/")
def index():
    return render_template("index.html", menu=MENU, icons=CATEGORY_ICONS)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    order = data.get("order", {})
    customer = data.get("customer", "Guest")
    table = data.get("table", "1")

    items = []
    subtotal = 0
    for item_name, qty in order.items():
        qty = int(qty)
        if qty <= 0:
            continue
        # find price
        price = None
        for cat_items in MENU.values():
            if item_name in cat_items:
                price = cat_items[item_name]
                break
        if price is None:
            continue
        amount = price * qty
        subtotal += amount
        items.append({"name": item_name, "qty": qty, "price": price, "amount": amount})

    gst = round(subtotal * GST_RATE, 2)
    service = round(subtotal * SERVICE_RATE, 2)
    total = subtotal + gst + service

    return jsonify({
        "customer": customer,
        "table": table,
        "date": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "items": items,
        "subtotal": subtotal,
        "gst": gst,
        "service": service,
        "total": total,
    })

if __name__ == "__main__":
    app.run(debug=True)
