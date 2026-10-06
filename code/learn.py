print("Hello Pravin")


### Dictionary,
#### Type 3 :

apple_rev = {
    "USA" : {
        "iphone":45,
        "ipad": 56,
        "Macbook":39
    },
    "China":{
        "iphone":10,
        "ipad": 15,
        "Macbook":12
    },
    "India":{
        "iphone":5,
        "ipad": 6,
        "Macbook":7
    }
}

for country, product_data in apple_rev.items():
    for product, rev in product_data.items():
        print(f"{country} , {product}  : {rev} millions $ " )
print(dir(apple_rev))


#### Type 2 :
d = {
    1:'a',
    2:'b',
    3:'c'
}
print(d)
d2 = {
    'rachal':89972588,
    'monica':79866323,
    'Joey':98656324
}
print(d2["Joey"])
d2['rachal']=123456789
print(d2["rachal"])
#### Type  1 :
# contacts = [('rachal',45695554),('monica',4545454),('joey',446466128)]
# for contact in contacts:
#     if contact[0] == 'monica':
#         print(contact[0], contact[1])




"""
def company_info(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])
    # if 'ticker' in kwargs: 
    #     print("ticker =",kwargs['ticker'])
    # if 'ceo' in kwargs:
    #     print("ceo =",kwargs["ceo"])
    # if 'revenue' in kwargs:
    #     print("revenue =",kwargs['revenue'])
company_info(ticker='AAPL',ceo='elice',revenue='200 billion',finance='brad')
"""



"""

### Arguments :
def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

total_num = sum(1,2,4,5,6,7,8,9,10)
print(total_num)
"""


"""
### functions :
def toatal_exp(expenses):
    
    # expenses: list
    # :param expenses: expenses carried by individual ones
    total_expense = 0
    for i in range(len(expenses)):
    # :return: totsl sum of expenses
    
    total = 0
    for expense in expenses:
        total += expense
    return total

exp_sergey = [30,59,30,56,24]
exp_sunder = [56,23,77,34,10]

total_expenses_sergey = toatal_exp(exp_sergey)
print(f" tostal expenses for serget is : {total_expenses_sergey}")
toatal_expenses_sunder = toatal_exp(exp_sunder)
print(f" tostal expenses for sunder is : {toatal_expenses_sunder}")

"""




"""
### for loop :

Indian = ["samosa","dal","roti"]            
monthly_sales = [45,78,33,46,39]
month = ["Jan","Feb","Mar","Apr","May","Jun"]
thresold = 35
# for sales in monthly_sales:
for sales, month in zip(monthly_sales,month):
    if sales < thresold:
        print(f" The sales amount {sales} is less than thresold in {month}")
        break
    else :
        print(f" sales amount {sales} is greater than thresold in  {month}")

"""



"""
print(len(expenses))
expenses = [1000,1300,2400,4789,2345]
total_expense = 0

for i in range(len(expenses)):
    expense = expenses[i]
    print(f"Month {i+1} , expenses : {expense}")

for expense in expenses:
    total_expense +=  expense
print(total_expense)
"""



















#n= input("Enter the number : ")
#n = int(n)
#message = "number is even" if n%2==0 else "number is odd"
#print(message)
"""
Indian = ["samosa","dal","roti"]
Chinese = ["noodles", "fried rice"]
Italian = ["pizza","pasta","risotto"]

dish = input("Enter the dish name : ")

if dish in Indian:
    print(f" {dish} is Indian")
elif dish in Chinese:
    print(f"{dish} is Chinese")
elif dish in Italian:
    print(f"{dish} is Italian")
else:
    print(f" {dish} is Not available")
"""