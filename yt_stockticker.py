from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title('Stock Ticker 2000 by Impulse Buyer')
root.iconbitmap('C:/Users/brand/Desktop/')
root.geometry ("1000x150")



def stockLookup():
    try:
        global symbol
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ zip.get() +"/batch?types=quote,news,chart&range=1m&last=10&token=YOUR TOKEN HERE")
        api = json.loads(api_request.content)
        symbol = api['quote']['symbol']
        price = api['quote']['latestPrice']
        companyName = api['quote']['companyName']


        root.configure(background="#FFFF00")
        myLabel = Label(root, text=companyName + " Is Currently priced @" + " "+str(price) + \
                        "  " + symbol, font=("Helvetica", 25), background="#FFFF00")
        myLabel.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "Error..."
        print(e)



zip = Entry(root)
zip.grid(row=0, column=0)

stockButton = Button(root, text= "Lookup symbol",command=stockLookup)
stockButton.grid(row=0, column=1, stick=W+E+N+S)
root.mainloop()
