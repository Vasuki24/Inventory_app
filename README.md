# 🏷️ Inventory Management Web Application (Flask)

A simple **Flask-based web application** to manage product inventory across multiple warehouse locations.  
You can add products, locations, and record product movements (in, out, or transfer).  
Finally, view a **report of product balances** across locations.

---

## 🚀 Features

- Add / View Products  
- Add / View Locations  
- Add / View Product Movements  
- Calculate and display **Product Quantity per Location**  
- Simple, clean UI with navigation bar  
- SQLite Database (no setup needed)

---

## 🗂️ Project Structure
inventory_app/
│
├── app.py
├── models.py
├── requirements.txt
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── products.html
│ ├── locations.html
│ ├── movements.html
│ └── report.html
└── static/
└── style.css

---

## ⚙️ Installation

1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Inventory_app.git
cd Inventory_app

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

🧱 Database Schema
| Table               | Columns                                                                         |
| ------------------- | ------------------------------------------------------------------------------- |
| **Product**         | `product_id`, `name`                                                            |
| **Location**        | `location_id`, `name`                                                           |
| **ProductMovement** | `movement_id`, `timestamp`, `from_location`, `to_location`, `product_id`, `qty` |


Movement Logic:

Incoming (Add Stock): Leave from_location empty

Outgoing (Remove Stock): Leave to_location empty

Transfer: Fill both from_location and to_location

📊 Balance Report

The Report view calculates the current stock for each product at each location using:

Balance = SUM(qty moved in) - SUM(qty moved out)

Displayed in a grid with columns:

| Product | Warehouse | Qty |

💻 Screenshots

1. Home Page<img width="941" height="426" alt="image" src="https://github.com/user-attachments/assets/adae3f29-d8e9-47fb-9517-a4d0b8a65c53" />
   


 2. Products Page<img width="956" height="693" alt="image" src="https://github.com/user-attachments/assets/ad11159a-8e61-4e6a-b8a6-cf2a372687d4" />



 3. Locations Page<img width="952" height="644" alt="image" src="https://github.com/user-attachments/assets/ff86f3bb-7e06-4548-ba9a-b5de6309b88a" />



 4. Movements Page<img width="921" height="842" alt="image" src="https://github.com/user-attachments/assets/42f635da-2859-44df-8525-2272985c713a" />



 5. Report Page ![Uploading image.png…]()




