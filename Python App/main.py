import requests
import json
from tkinter import *

# free_api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
#  api_free = json.loads(free_api_request.content)
# print(api_free)

pycrypto = Tk()
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('C:/Users/mirva/PycharmProjects/pythonProject/Python App/favicon.ico')

def my_portfolio():
    try:
        # This is my basic developer account API Key, I am passing query params to limit the data output.
        api_request  = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD&CMC_PRO_API_KEY=ccd55895-0f0e-41c5-85a1-1b321ffdf191")
        if str(api_request) != "<Response [200]>":
            print("The API call was unsuccessful, the URL may no longer be supported") 
        api = json.loads(api_request.content)
        # print(api_request.content)
        # print(api)
        coins = [
            {
            "symbol" : "BTC",
            "amount_owned" : 2,
            "price_per_coin" : 22343
            },
            {
            "symbol" : "ETH",
            "amount_owned" : 100,
            "price_per_coin" : 1396
            },
            {
            "symbol" : "DOGE",
            "amount_owned" : 52000,
            "price_per_coin" : 0.0723
            },
            {
            "symbol" : "XRP",
            "amount_owned" : 4500,
            "price_per_coin" : 0.50
            }
        ]

        total_pl = 0
        r_count = 1
        for i in range(0,100):
            for coin in coins:
                if api["data"][i]["symbol"] == coin["symbol"]:
                    total_paid = coin["amount_owned"] * coin["price_per_coin"]
                    profit_earned = ((api["data"][i]["quote"]["USD"]["price"]) * coin["amount_owned"]) - total_paid
                    current_val= (api["data"][i]["quote"]["USD"]["price"]) * coin["amount_owned"]
                    # print((api["data"][i]["name"]) + " - " + api["data"][i]["symbol"])
                    # # print((api["data"][i]["slug"]).upper())
                    # print("Price - ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
                    # print("Number of coins owned: ", coin["amount_owned"])
                    # print("Total amount paid - ${0:.2f}".format(total_paid))
                    # print("Total profit owned till date for this crypto: ", "${0:.2f}".format(profit_earned))
                    # print("----------------------------")
                    total_pl = total_pl + profit_earned
                    name = Label(pycrypto, text = api["data"][i]["name"], bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
                    name.grid(row=r_count, column=0, sticky=N+S+E+W)

                    price = Label(pycrypto, text = "${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]), bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
                    price.grid(row=r_count, column=1, sticky=N+S+E+W)

                    coins_owned = Label(pycrypto, text = coin["amount_owned"], bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
                    coins_owned.grid(row=r_count, column=2, sticky=N+S+E+W)

                    amount_paid = Label(pycrypto, text = "${0:.2f}".format(total_paid), bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
                    amount_paid.grid(row=r_count, column=3, sticky=N+S+E+W)

                    current_value = Label(pycrypto, text = "${0:.2f}".format(current_val), bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
                    current_value.grid(row=r_count, column=4, sticky=N+S+E+W)

                    pl_per_coin = Label(pycrypto, text = "${0:.2f}".format(profit_earned), bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
                    pl_per_coin.grid(row=r_count, column=5, sticky=N+S+E+W)

                    r_count = r_count + 1
                    
        
    except:
        print("There was an error in loading the JSON values, the URL may no longer be supported") 
    tpl = Label(pycrypto, text = "TOTAL", bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
    tpl.grid(row=r_count, column=0, sticky=N+S+E+W)    
    tpl = Label(pycrypto, text = "${0:.2f}".format(total_pl), bg= "white" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
    tpl.grid(row=r_count, column=5, sticky=N+S+E+W)
# print("Total Profit-Loss till date: $", "{0:.2f}".format(total_pl))


name = Label(pycrypto, text = "Coin Name", bg= "#1f7a1f" , fg="white", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycrypto, text = "Price", bg= "#33ffff" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
price.grid(row=0, column=1, sticky=N+S+E+W)

coins_owned = Label(pycrypto, text = "Coins Owned", bg= "#1f7a1f" , fg="white", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
coins_owned.grid(row=0, column=2, sticky=N+S+E+W)

amount_paid = Label(pycrypto, text = "Total Amount Paid", bg= "#33ffff" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
amount_paid.grid(row=0, column=3, sticky=N+S+E+W)

current_value = Label(pycrypto, text = "Current Value", bg= "#1f7a1f" , fg="white", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
current_value.grid(row=0, column=4, sticky=N+S+E+W)

pl_per_coin = Label(pycrypto, text = "P/L Per Coin", bg= "#33ffff" , fg="black", font="Helvetica 11 bold", padx="6", pady="6", borderwidth=2, relief="ridge")
pl_per_coin.grid(row=0, column=5, sticky=N+S+E+W)
my_portfolio()
pycrypto.mainloop()




























# # print(coindata_file.read())
# try:
#     coindata_file = open('C:/Users/mirva/PycharmProjects/pythonProject/Python App/Coin.txt', "r+")
#     print(coindata_file.read())
# except:
#     print("Unknown Error")
# coindata_file.write("\n" + "Toby - Human Resource")
# print(coindata_file.read())
# coindata_file.close()