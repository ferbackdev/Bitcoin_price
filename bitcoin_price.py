from tkinter import *
from tkinter import ttk
import requests
import time
import json

class BitcoinPrice:
    def __init__(self, root=Tk()):
        self.root = root
        self.root.title("Bitcoin Price")
        self.root.geometry("520x400")
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file="bitcoin.png"))
        self.root.config(bg="lightgray")

        # titolo
        title = Label(self.root, text="Bitcoin Price", font=("times new roman", 30, "bold"), bg="gray", fg="black").place(x=0, y=0, relwidth=1)

        # BTN EURO, BRL, USD, 
        btn_euro = Button(self.root, text="EUR", command=lambda: self.get_price("EUR"), font=("times new roman", 20, "bold"), bg="blue", fg="white").place(x=50, y=280)
        btn_brl = Button(self.root, text="BRL", command=lambda: self.get_price("BRL"), font=("times new roman", 20, "bold"), bg="blue", fg="white").place(x=150, y=280)
        btn_usd = Button(self.root, text="USD", command=lambda: self.get_price("USD"), font=("times new roman", 20, "bold"), bg="blue", fg="white").place(x=250, y=280)
        
        # variabili
        self.var_price = StringVar()
        self.var_time = StringVar()
        self.var_price.set("Price: ")
        self.var_time.set("Updated: ")

        # labels
        lbl_price = Label(self.root, textvariable=self.var_price, font=("times new roman", 20, "bold"), bg="gray", fg="black").place(x=50, y=100)
        lbl_time = Label(self.root, textvariable=self.var_time, font=("times new roman", 20, "bold"), bg="gray", fg="black").place(x=50, y=150)
        
        # bottone per ottenere il prezzo
        btn = Button(self.root, text="Get Price", command=self.get_price, font=("times new roman", 20, "bold"), bg="blue", fg="white").place(x=50, y=200)
        
    def get_price(self, currency="USD"):
        # url
        url = f"https://api.coindesk.com/v1/bpi/currentprice/{currency}.json"
        response = requests.get(url)
        data = response.json()
        price = data["bpi"][currency]["rate"]
        time_ = data["time"]["updated"]
        self.var_price.set(f"Price: {price} {currency}")
        self.var_time.set(f"Updated: {time_}")
        
    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = BitcoinPrice()
    app.mainloop()

