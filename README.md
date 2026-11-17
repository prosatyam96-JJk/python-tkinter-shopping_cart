# 🛒 Python Shopping Cart System

A GUI-based Shopping Cart Management System developed using **Python and Tkinter**. This application allows users to select products, manage their shopping cart, remove products, and automatically calculate bills with discounts and GST.

## 📌 Project Overview

This project is designed to demonstrate Python programming concepts and desktop GUI development. It provides a simple shopping experience through an interactive interface.

## ✨ Features

- Product catalogue with prices.
- Product selection using a dropdown menu.
- Add products with custom quantities.
- View cart items in a table.
- Remove selected products.
- Automatic subtotal calculation.
- 10% discount when subtotal exceeds ₹500.
- 18% GST calculation after discount.
- Automatic bill updates.
- Input validation and error handling.
- Scrollable graphical interface.

## 🛠️ Technologies Used

- Python 3
- Tkinter
- ttk
- Python Dictionaries
- Functions
- Exception Handling

## 🛍️ Available Products

| Product | Price |
|---|---:|
| Pen | ₹10 |
| Notebook | ₹50 |
| Bag | ₹500 |

## 🧮 Billing Logic

**Subtotal:** Sum of product price × quantity.

**Discount:** 10% when subtotal is greater than ₹500.

**GST:** 18% of the amount after discount.

**Grand Total:** Subtotal − Discount + GST.

### Example

For 2 Bags:

| Description | Amount |
|---|---:|
| Subtotal | ₹1,000 |
| Discount | ₹100 |
| GST | ₹162 |
| **Grand Total** | **₹1,062** |

## 🚀 How to Run

### Prerequisites
- Python 3 installed.
- Tkinter available.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/python-tkinter-shopping-cart.git
```

2. Open the project folder:

```bash
cd python-tkinter-shopping-cart
```

3. Run the application:

```bash
python shopping_cart.py
```

## 📁 Project Structure

```text
python-tkinter-shopping-cart/
│
├── shopping_cart.py
├── README.md
├── summary.md
└── assets/
    ├── main-window.png
    ├── shopping-cart.png
    └── billing-result.png
```

## 📊 Project Summary and Testing

For detailed project documentation, test cases, testing results, and application screenshots, see:

**[View Project Summary](summary.md)**

## 🎯 Learning Outcomes

- Understanding Python dictionaries and functions.
- Building desktop applications using Tkinter.
- Managing shopping cart data.
- Implementing billing calculations.
- Handling invalid user inputs.
- Working with GUI components and events.

## 👨‍💻 Author

**Satyam Kumar Singh**

B.Tech – Computer Science and Engineering (AI & ML)

Rungta University

## 📄 License

This project is available for educational and learning purposes.