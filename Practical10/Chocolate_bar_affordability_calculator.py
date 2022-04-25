def f(money, price):
#define a function about money and price
    x = money//price
#x is the chocolate bar number
    y = money%price
#y is the change
    return[x,y]
#take and example:
money = 100
price = 7
print("The chocolate bar number and the change are", f(money, price))
#print: The chocolate bar number and the change are [14, 2]

