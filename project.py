from tkinter import *
from tkinter import ttk

class CurrencyConverter:
    def __init__(self):
        self.currencies = dict()
        with open("weight.py") as file:
            for line in file:
                line = line.rstrip("\n")
                currency, rate = line.split(":") #  split the data [USA:1] into two parts
                self.currencies[currency] = float(rate)  #  make a dictioanry of [Currency name] -> [rate]

    def convert(self, from_currency, to_currency, amount):
        amount = amount / self.currencies[from_currency]
        amount = amount * self.currencies[to_currency]
        amoutn = round(amount, 2)  #  keep two decimal places
        return amount
    #  The convert function will provide/generate the converted result

class App(Tk):
    def __init__(self, converter):
        Tk.__init__(self)  #  NO NEED TO Change
        self.my_converter = converter  #  NO NEED TO Change
        self.config(bg="indigo")  #  NO NEED TO Change
        self.geometry("800x400")  #  NO NEED TO Change
        # Title
        self.title = Label(self, text="Weight Converter")  #  Change title
        self.title.config(fg='pink', bg='indigo', font=("Courier", 15, "bold",))  #  NO NEED TO Change
        self.title.place(x=300, y=5)  #  NO NEED TO Change
        # Entry Box
        self.entry_box = Entry(self, bd=3, justify=CENTER)  #  NO NEED TO Change
        self.entry_box.place(x=350, y=80)  #  NO NEED TO Change
        #  DropDown List
        self.from_currency_list = StringVar(self)  #  NO NEED TO Change if you did not change variable name
        self.from_currency_list.set("lbs") #  Default option is CAD
        self.to_currency_list = StringVar(self)		 #  NO NEED TO Change if you did not change variable name
        self.to_currency_list.set("kg")  #   Default option is USD

        self.or_currency_list = StringVar(self)		 #  NO NEED TO Change if you did not change variable name
        self.or_currency_list.set("g")  #   Default option is USD
        font = ("Courier", 12)  #  NO NEED TO Change
        self.option_add("*TCombobox*Listbox.font", font)  #  NO NEED TO Change
        self.from_currency_dropdown = ttk.Combobox(self,textvariable=self.from_currency_list,value=list(self.my_converter.currencies.keys()))  # Read all options from from_currency_list
        self.to_currency_dropdown = ttk.Combobox(
            self,
            textvariable=self.to_currency_list,
            value=list(self.my_converter.currencies.keys()),
        )  # Read all options from to_currency_list

        self.from_currency_dropdown.place(x=250,y=50)   #  NO NEED TO Change if you did not change variable name
        self.to_currency_dropdown.place(x=400,y=50)    #  NO NEED TO Change if you did not change variable name


        # result message
        self.result = Label(self,text='')  #  NO NEED TO Change
        self.result.config(font=("Arial",12,"bold"))  #  NO NEED TO Change
        self.result.place(x=380,y=200)  #  NO NEED TO Change
        # Convert Button
        self.convert_button = Button(self,text="Convert",fg='white',bg='purple',command=self.do_convert)  #  NO NEED TO Change
        self.convert_button.config(font=('Arial',10))  #  NO NEED TO Change
        self.convert_button.place(x=380,y=120)  #  NO NEED TO Change

    def do_convert(self):
        amount = float(self.entry_box.get())  #  get amount value from entry box
        from_curr = self.from_currency_dropdown.get()  #  get value from dropdown list
        to_curr = self.to_currency_dropdown.get()		#  get value from dropdown list
        converted_amount = self.my_converter.convert(from_curr,to_curr,amount)  #  use the convert function to calculate result

        self.result.config(text=str(round(converted_amount,2)))   # Show result

# Launch the App
my_converter = CurrencyConverter()  #  NO NEED TO Change if you did not change class name
App(my_converter)		#  NO NEED TO Change if you did not change class name
mainloop()  #  NO NEED TO Change

