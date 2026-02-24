# 🍽️ Spice Garden — Restaurant Billing Web App

A beautiful web-based restaurant billing system built with **Python Flask**, priced in Indian Rupees (₹).

## Features
- 🗂️ 5 menu categories with 21 items
- ➕ Add / remove items with quantity controls
- 🧾 Live order summary with running totals
- 💰 Auto-calculates GST (5%) + Service Charge (10%)
- 🖨️ Print-ready bill receipt modal
- 📱 Responsive — works on mobile & desktop

## Requirements
- Python 3.8+
- Flask

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
python app.py
```

### 3. Open in browser
```
http://127.0.0.1:5000
```

## Project Structure
```
restaurant_app/
├── app.py               ← Flask backend
├── requirements.txt     ← Dependencies
├── README.md
└── templates/
    └── index.html       ← Frontend (HTML + CSS + JS)
```

## Bill Breakdown
| Component       | Rate |
|----------------|------|
| GST             | 5%   |
| Service Charge  | 10%  |
