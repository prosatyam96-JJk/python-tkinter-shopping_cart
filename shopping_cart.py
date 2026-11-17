import tkinter as tk
from tkinter import ttk, messagebox

#Creating Main Window
root = tk.Tk()

#Window Settings
root.title("Shopping Cart System")
root.geometry("800x650")
root.minsize(700, 550)

#Background colour
root.configure(bg="#f2f5fa")


# Main Scrollable Area
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(main_frame, bg="#f2f5fa")

scrollbar = ttk.Scrollbar(
    main_frame,
    orient="vertical",
    command=canvas.yview
)

scrollable_frame = tk.Frame(canvas, bg="#f2f5fa")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#Welcome Heading

heading = tk.Label(
    scrollable_frame,
    text ="SHOPPING CART SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#f2f5fa",
    fg="#1e3a5f"
)

heading.pack(pady=10)
#Product Catalouge code

products = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500
}

product_frame = tk.LabelFrame(
    scrollable_frame,
    text="Available Products",
    padx=10,
    pady=15
)
product_frame.pack(pady=20)

for name,price in products.items():
    product_label = tk.Label(
        product_frame,
        text=f"{name} - Rs. {price}"
    )
    product_label.pack()

#Shoping Cart
    cart = {}

#Product Selection


tk.Label(
    scrollable_frame,
    text="Select Product:",
    font=("Arial", 12),
    bg="#f2f5fa"
).pack(pady=(15, 5))

product_choice = ttk.Combobox(
    scrollable_frame,
    values=["Pen", "Notebook", "Bag", "Laptop"],
    state="readonly",
    width=25
)

product_choice.pack(pady=(5, 15))
product_choice.set("Pen")


#Quantity Input

tk.Label(
    scrollable_frame,
    text="Enter Quantity:",
    font=("Arial", 12),
    bg="#f2f5fa"
).pack(pady=(10, 5))

quantity_entry = tk.Entry(scrollable_frame)
quantity_entry.pack(pady=(5, 15))

quantity_entry.insert(0, 1)

#Add to Cart Function

def add_to_cart():

    name = product_choice.get()
    if name not in products:
        messagebox.showerror("Error", "Invalid Product Available: Pen, Notebook, Bag")
        return

    try:
        quantity = int(quantity_entry.get())

        if quantity <= 0:
            messagebox.showerror(
                "Error",
                "Quantity must be at least 1"
            )
            return
        cart[name] = cart.get(name, 0) + quantity
        update_cart_dispaly()
        calculate_bill()


        messagebox.showinfo(
            "Success"
            f"{quantity} {name}(s) added to cart!"
        )

    except ValueError:
        messagebox.showerror(
            "Please Enter a Valid Quantity"
        )


#Add to cart Button

add_button = tk.Button(
    root,
    text="Add to Cart",
    command=add_to_cart,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold")
)

add_button.pack(pady=(15, 25))

#Cart Display
cart_frame = tk.LabelFrame(
    scrollable_frame,
    text="Your Shopping Cart",
    font=("Arial", 14, "bold"),
    bg="#f2f5fa",
    fg="#1e3a5f",
    padx=20,
    pady=15
)

cart_frame.pack(padx=20, pady=5, fill="x", expand=True)

#Cart Table

cart_table = ttk.Treeview(
    cart_frame,
    columns=("Product", "Price", "Quantity", "Total"),
    show="headings",
    height=5
)

cart_table.heading("Product", text="Product")
cart_table.heading("Price", text="Price (Rs.)")
cart_table.heading("Quantity", text="Quantity")
cart_table.heading("Total", text="Total (Rs.)")

cart_table.pack(fill="x",expand=False)

def update_cart_dispaly():

    #Remove old rows
    for row in cart_table.get_children():
        cart_table.delete(row)

    # Display updated cart
    for name, quantity in cart.items():
        price = products[name]
        total = price * quantity

        cart_table.insert(
            "",
            "end",
            values=(name, price, quantity, total)
        )


# Remove Products from Cart

def remove_from_cart():
    selected = cart_table.selection()

    if not selected:
        messagebox.showerror("Error", "Please select a product")
        return

    item = cart_table.item(selected[0])
    name = item["values"][0]

    del cart[name]

    update_cart_dispaly()
    calculate_bill()

    messagebox.showinfo("Success", f"{name} removed from cart")




# Remove button

remove_button = tk.Button(
    cart_frame,
    text="Remove Selected Product",
    command=remove_from_cart,
    bg="#dc2626",
    fg="white",
    font=("Arial", 11, "bold")
)

remove_button.pack(pady=10)

# Billing Section
bill_frame = tk.LabelFrame(
    scrollable_frame,
    text="Bill Summary",
    font=("Arial", 14, "bold"),
    bg="#f2f5fa",
    fg="#1e3a5f",
    padx=20,
    pady=15
)


bill_frame.pack(
    padx=20,
    pady=5,
    fill="x",
    side="bottom"
)

subtotal_label = tk.Label(
    bill_frame,
    text="Subtotal: Rs. 0",
    font=("Arial", 12),
    bg="#f2f5fa",
    fg="black"
)
subtotal_label.pack(anchor="w", pady=3)

discount_label = tk.Label(
    bill_frame,
    text="Discount: Rs. 0",
    font=("Arial", 12),
    bg="#f2f5fa",
    fg="black"
)
discount_label.pack(anchor="w", pady=3)

gst_label = tk.Label(
    bill_frame,
    text="GST (18%): Rs. 0",
    font=("Arial", 12),
    bg="#f2f5fa",
    fg="black"
)
gst_label.pack(anchor="w", pady=3)

total_label = tk.Label(
    bill_frame,
    text="Grand Total: Rs. 0",
    font=("Arial", 14, "bold"),
    bg="#f2f5fa",
    fg="black"
)
total_label.pack(anchor="w", pady=5)


# calculate bill
def calculate_bill():
    subtotal = 0

    for name, quantity in cart.items():
        subtotal += products[name] * quantity

    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    gst = (subtotal - discount) * 0.18

    grand_total = subtotal - discount + gst

    subtotal_label.config(text=f"Subtotal: Rs. {subtotal:.2f}")
    discount_label.config(text=f"Discount: Rs. {discount:.2f}")
    gst_label.config(text=f"GST (18%): Rs. {gst:.2f}")
    total_label.config(text=f"Grand Total: Rs. {grand_total:.2f}")

# Bill button
# bill_button = tk.Button(
#     bill_frame,
#     text="Calculate Bill",
#     command=calculate_bill,
#     bg="#16a34a",
#     fg="white",
#     font=("Arial", 12, "bold")
# )

# bill_button.pack(pady=10)
#Run Application

root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox

#Creating Main Window
root = tk.Tk()

#Window Settings
root.title("Shopping Cart System")
root.geometry("800x650")
root.minsize(700, 550)

#Background colour
root.configure(bg="#f2f5fa")


# Main Scrollable Area
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(main_frame, bg="#f2f5fa")

scrollbar = ttk.Scrollbar(
    main_frame,
    orient="vertical",
    command=canvas.yview
)

scrollable_frame = tk.Frame(canvas, bg="#f2f5fa")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window(
    (0, 0),
    window=scrollable_frame,
    anchor="nw"
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

#Welcome Heading

heading = tk.Label(
    scrollable_frame,
    text ="SHOPPING CART SYSTEM",
    font=("Arial", 22, "bold"),
    bg="#f2f5fa",
    fg="#1e3a5f"
)

heading.pack(pady=10)
#Product Catalouge code

products = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500
}

product_frame = tk.LabelFrame(
    scrollable_frame,
    text="Available Products",
    padx=10,
    pady=15
)
product_frame.pack(pady=20)

for name,price in products.items():
    product_label = tk.Label(
        product_frame,
        text=f"{name} - Rs. {price}"
    )
    product_label.pack()

#Shoping Cart
    cart = {}

#Product Selection


tk.Label(
    scrollable_frame,
    text="Select Product:",
    font=("Arial", 12),
    bg="#f2f5fa"
).pack(pady=(15, 5))

product_choice = ttk.Combobox(
    scrollable_frame,
    values=["Pen", "Notebook", "Bag", "Laptop"],
    state="readonly",
    width=25
)

product_choice.pack(pady=(5, 15))
product_choice.set("Pen")


#Quantity Input

tk.Label(
    scrollable_frame,
    text="Enter Quantity:",
    font=("Arial", 12),
    bg="#f2f5fa"
).pack(pady=(10, 5))

quantity_entry = tk.Entry(scrollable_frame)
quantity_entry.pack(pady=(5, 15))

quantity_entry.insert(0, 1)

#Add to Cart Function

def add_to_cart():

    name = product_choice.get()
    if name not in products:
        messagebox.showerror("Error", "Invalid Product Available: Pen, Notebook, Bag")
        return

    try:
        quantity = int(quantity_entry.get())

        if quantity <= 0:
            messagebox.showerror(
                "Error",
                "Quantity must be at least 1"
            )
            return
        cart[name] = cart.get(name, 0) + quantity
        update_cart_dispaly()
        calculate_bill()


        messagebox.showinfo(
            "Success"
            f"{quantity} {name}(s) added to cart!"
        )

    except ValueError:
        messagebox.showerror(
            "Please Enter a Valid Quantity"
        )


#Add to cart Button

add_button = tk.Button(
    root,
    text="Add to Cart",
    command=add_to_cart,
    bg="#2563eb",
    fg="white",
    font=("Arial", 12, "bold")
)

add_button.pack(pady=(15, 25))

#Cart Display
cart_frame = tk.LabelFrame(
    scrollable_frame,
    text="Your Shopping Cart",
    font=("Arial", 14, "bold"),
    bg="#f2f5fa",
    fg="#1e3a5f",
    padx=20,
    pady=15
)

cart_frame.pack(padx=20, pady=5, fill="x", expand=True)

#Cart Table

cart_table = ttk.Treeview(
    cart_frame,
    columns=("Product", "Price", "Quantity", "Total"),
    show="headings",
    height=5
)

cart_table.heading("Product", text="Product")
cart_table.heading("Price", text="Price (Rs.)")
cart_table.heading("Quantity", text="Quantity")
cart_table.heading("Total", text="Total (Rs.)")

cart_table.pack(fill="x",expand=False)

def update_cart_dispaly():

    #Remove old rows
    for row in cart_table.get_children():
        cart_table.delete(row)

    # Display updated cart
    for name, quantity in cart.items():
        price = products[name]
        total = price * quantity

        cart_table.insert(
            "",
            "end",
            values=(name, price, quantity, total)
        )


# Remove Products from Cart

def remove_from_cart():
    selected = cart_table.selection()

    if not selected:
        messagebox.showerror("Error", "Please select a product")
        return

    item = cart_table.item(selected[0])
    name = item["values"][0]

    del cart[name]

    update_cart_dispaly()
    calculate_bill()

    messagebox.showinfo("Success", f"{name} removed from cart")




# Remove button

remove_button = tk.Button(
    cart_frame,
    text="Remove Selected Product",
    command=remove_from_cart,
    bg="#dc2626",
    fg="white",
    font=("Arial", 11, "bold")
)

remove_button.pack(pady=10)

# Billing Section
bill_frame = tk.LabelFrame(
    scrollable_frame,
    text="Bill Summary",
    font=("Arial", 14, "bold"),
    bg="#f2f5fa",
    fg="#1e3a5f",
    padx=20,
    pady=15
)


bill_frame.pack(
    padx=20,
    pady=5,
    fill="x",
    side="bottom"
)

subtotal_label = tk.Label(
    bill_frame,
    text="Subtotal: Rs. 0",
    font=("Arial", 12),
    bg="#f2f5fa",
    fg="black"
)
subtotal_label.pack(anchor="w", pady=3)

discount_label = tk.Label(
    bill_frame,
    text="Discount: Rs. 0",
    font=("Arial", 12),
    bg="#f2f5fa",
    fg="black"
)
discount_label.pack(anchor="w", pady=3)

gst_label = tk.Label(
    bill_frame,
    text="GST (18%): Rs. 0",
    font=("Arial", 12),
    bg="#f2f5fa",
    fg="black"
)
gst_label.pack(anchor="w", pady=3)

total_label = tk.Label(
    bill_frame,
    text="Grand Total: Rs. 0",
    font=("Arial", 14, "bold"),
    bg="#f2f5fa",
    fg="black"
)
total_label.pack(anchor="w", pady=5)


# calculate bill
def calculate_bill():
    subtotal = 0

    for name, quantity in cart.items():
        subtotal += products[name] * quantity

    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    gst = (subtotal - discount) * 0.18

    grand_total = subtotal - discount + gst

    subtotal_label.config(text=f"Subtotal: Rs. {subtotal:.2f}")
    discount_label.config(text=f"Discount: Rs. {discount:.2f}")
    gst_label.config(text=f"GST (18%): Rs. {gst:.2f}")
    total_label.config(text=f"Grand Total: Rs. {grand_total:.2f}")

# Bill button
# bill_button = tk.Button(
#     bill_frame,
#     text="Calculate Bill",
#     command=calculate_bill,
#     bg="#16a34a",
#     fg="white",
#     font=("Arial", 12, "bold")
# )

# bill_button.pack(pady=10)
#Run Application

root.mainloop()