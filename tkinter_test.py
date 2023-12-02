from tkinter import * 
import random

numShares = 0
account = 10000
sharePrice = 97

def update():
    shares['text'] = 'You own {0} shares'.format(numShares)
    cash['text'] = 'Cash balance: ${0:.0f}'.format(account)
    totalWorth = account + numShares*sharePrice
    worth['text'] = 'Total worth: ${0:.0f}'.format(totalWorth)
    price['text'] = '${0:.2f}/share'.format(sharePrice)

def changePrice():
    global sharePrice
    sharePrice += random.random()*4 - 2
    update()
    root.after(2000, changePrice)

def doBuy():
    global account, numShares

    if account >= 10 * sharePrice:
        numShares += 10
        account -= 10*sharePrice
        update()

def doSell():
    global account, numShares
    if numShares >= 10:
        numShares -= 10
        account += 10*sharePrice
        update()

root = Tk()
# root['bg'] = 'light yellow'

# frame widget: a rectangle into 
# which other widgets may be placed 
# like div?
status = Frame(root)
# status['bg'] = 'light green'

shares = Label(status)
shares['text'] = 'Number of shares'
shares.pack(anchor=W)

cash = Label(status)
cash['text'] = 'Cash on hand'
cash.pack(anchor=W)

worth = Label(status)
worth['text'] = 'Total Worth'
worth.pack(side=BOTTOM, anchor=W)


############## second frame ##############

action = Frame(root)
# action['bg'] = 'pink'

price = Label(action)
price['text'] = 'Price of stock'
price.pack(anchor=E)

sell = Button(action)
sell['text'] = 'sell'
sell['command'] = doSell
sell.pack(side=BOTTOM, fill=X)

buy = Button(action)
buy['text'] = 'buy'
buy['command'] = doBuy
buy.pack(side=BOTTOM, fill=X)

status.pack(expand=YES, fill=BOTH, side=LEFT)
action.pack(expand=YES, fill=BOTH, side=RIGHT)

changePrice()

mainloop()
