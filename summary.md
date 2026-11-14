# 📊 Project Summary – Python Shopping Cart System

## 1. Project Information

| Detail          | Description |

| Project Name    | Python Shopping Cart System |
| Language        | Python 3 |
| GUI Framework   | Tkinter |
| Project Type    | Desktop GUI Application |
| Author          | Satyam Kumar Singh |
| College         | Rungta University |
| Branch          | B.Tech CSE (AI & ML) |

## 2. Project Description

The Python Shopping Cart System is a desktop application developed using Python and Tkinter.

It allows users to select products, add them to a shopping cart, manage quantities, remove products, and calculate the final bill.

The application also includes automatic discount and GST calculations along with input validation.

## 3. Main Features

- Product selection through a dropdown.
- Add products to the shopping cart.
- Display products in a table.
- Remove selected products.
- Automatic billing calculations.
- Discount and GST calculation.
- Input validation.
- Scrollable GUI.

## 4. Test Cases

| Test ID | Test Scenario | Input | Expected Result |
|---|---|---|---|
| TC01 | Add Notebook | Quantity: 2 | Subtotal ₹100 |
| TC02 | Add Bag | Quantity: 1 | Total ₹590 |
| TC03 | Apply discount | Bag × 2 | Total ₹1,062 |
| TC04 | Invalid product | Laptop | Error message |
| TC05 | Negative quantity | -1 | Error message |
| TC06 | Zero quantity | 0 | Error message |
| TC07 | Invalid quantity | abc | Error message |
| TC08 | Remove product | Select Pen | Product removed |
| TC09 | Empty cart | Remove all products | Total ₹0 |
| TC10 | Automatic billing | Add/remove products | Bill updates automatically |

## 5. Test Results

Update the status after running each test.

| Test ID | Status | Remarks |
|---|---|---|
| TC01 | Passed | Executed as expected |
| TC02 | Passed | Executed as expected |
| TC03 | Passed | Executed as expected |
| TC04 | Passed | Executed as expected |
| TC05 | Passed | Executed as expected |
| TC06 | Passed | Executed as expected |
| TC07 | Passed | Executed as expected |
| TC08 | Passed | Executed as expected |
| TC09 | Passed | Executed as expected |
| TC10 | Passed | Executed as expected |


## 6. Project Assets

All project screenshots are stored in the `assets/` folder.



## 7. Learning Outcomes

Through this project, I learned:

1. Python dictionaries and functions.
2. GUI development using Tkinter.
3. Managing data using dictionaries.
4. Input validation and exception handling.
5. Creating interactive buttons and dropdowns.
6. Implementing discount and GST calculations.
7. Testing and debugging a Python application.

## 8. Future Improvements

- Add more products dynamically.
- Add product images.
- Generate downloadable bills.
- Save cart data using files or a database.
- Add customer information and order history.

## 9. Conclusion

This project helped me understand how Python can be used to develop practical desktop applications. It improved my knowledge of GUI development, programming logic, data management, and debugging.
