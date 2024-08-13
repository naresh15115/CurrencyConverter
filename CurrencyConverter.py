from currency_converter import CurrencyConverter
import tkinter as tk


c = CurrencyConverter()

def clicked():

    
    amount = float(e1.get())
    cur1 = var_source_currency.get()
    cur2 = var_target_currency.get()

    
    result = c.convert(amount, cur1, cur2)

   
    l5.config(text=f"Converted Amount: {result:.2f} {cur2}")

def clear():
    e1.delete(0, 'end')  
    l5.config(text="")  

window = tk.Tk()
window.geometry("800x360")
window.title("Currency Converter")


l1 = tk.Label(window, text="Currency Converter ", font="Times 25 bold")
l1.place(x=100, y=30)

l2 = tk.Label(window, text="Enter amount here: ", font="Times 18 bold")
l2.place(x=50, y=80)

l3 = tk.Label(window, text="Select Source Currency: ", font="Times 18 bold")
l3.place(x=50, y=130)

l4 = tk.Label(window, text="Select Target Currency:", font="Times 18 bold")
l4.place(x=50, y=180)

l5 = tk.Label(window, text="", font="Times 25 bold")
l5.place(x=170, y=290)


e1 = tk.Entry(window)
e1.place(x=300, y=90)


source_currency_list = ['USD', 'EUR', 'JPY', 'GBP', 'AUD','INR']  
var_source_currency = tk.StringVar()
var_source_currency.set(source_currency_list[0]) 
source_currency_menu = tk.OptionMenu(window, var_source_currency, *source_currency_list)
source_currency_menu.place(x=320, y=135)


target_currency_list = ['USD', 'EUR', 'JPY', 'GBP', 'AUD','INR']  
var_target_currency = tk.StringVar()
var_target_currency.set(target_currency_list[1]) 
target_currency_menu = tk.OptionMenu(window, var_target_currency, *target_currency_list)
target_currency_menu.place(x=320, y=185)


b1 = tk.Button(window, text="Convert", command=clicked)
b1.place(x=230, y=240)


b2 = tk.Button(window, text="Clear", command=clear)
b2.place(x=320, y=240)


window.mainloop()
