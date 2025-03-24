import tkinter as tk

# User credentials
USER_ID = "1"
PASSWORD = "2014"

# Product list
PRODUCTS = {
    "1": "Pringles Sour Cream",
    "2": "LAYS MEGA PACK XL"
}

class POSLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("POS Login")
        self.root.geometry("400x500")
        self.root.configure(bg="black")

        self.current_input = ""
        self.login_step = 0  # 0: User ID, 1: Password
        self.user_id = ""
        self.password = ""

        self.label = tk.Label(root, text="Enter User ID", font=("Arial", 16), fg="white", bg="black")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 20), width=10, justify="center", show="")
        self.entry.pack(pady=5)

        self.create_keypad()

    def create_keypad(self):
        keypad_frame = tk.Frame(self.root, bg="black")
        keypad_frame.pack()

        buttons = [
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2),
            ("0", 4, 1), ("DEL", 4, 0), ("OK", 4, 2)
        ]

        for text, row, col in buttons:
            btn = tk.Button(
                keypad_frame, text=text, font=("Arial", 18), width=5, height=2, 
                command=lambda t=text: self.on_keypress(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

    def on_keypress(self, key):
        if key == "DEL":
            self.current_input = self.current_input[:-1]
        elif key == "OK":
            self.process_login()
        else:
            self.current_input += key

        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.current_input)

    def process_login(self):
        if self.login_step == 0:
            self.user_id = self.current_input
            if self.user_id == USER_ID:
                self.login_step = 1
                self.current_input = ""
                self.label.config(text="Enter Password")
                self.entry.delete(0, tk.END)
                self.entry.config(show="*")
            else:
                self.label.config(text="Invalid User ID!")
                self.current_input = ""
        else:
            self.password = self.current_input
            if self.password == PASSWORD:
                self.root.destroy()
                self.open_pos_screen()
            else:
                self.label.config(text="Invalid Password!")
                self.current_input = ""

        self.entry.delete(0, tk.END)

    def open_pos_screen(self):
        pos_window = tk.Tk()
        pos_window.title("Point of Sale")
        pos_window.geometry("400x400")
        pos_window.configure(bg="black")

        tk.Label(pos_window, text="Select Product", font=("Arial", 16), fg="white", bg="black").pack(pady=10)

        tk.Button(
            pos_window, text="Pringles Sour Cream", font=("Arial", 14), command=lambda: self.add_product("1")
        ).pack(pady=5)

        tk.Button(
            pos_window, text="LAYS MEGA PACK XL", font=("Arial", 14), command=lambda: self.add_product("2")
        ).pack(pady=5)

        self.cart_label = tk.Label(pos_window, text="Cart: ", font=("Arial", 14), fg="white", bg="black")
        self.cart_label.pack(pady=10)

        pos_window.mainloop()

    def add_product(self, product_id):
        product_name = PRODUCTS[product_id]
        self.cart_label.config(text=f"Cart: {product_name}")

if __name__ == "__main__":
    root = tk.Tk()
    app = POSLoginApp(root)
    root.mainloop()
