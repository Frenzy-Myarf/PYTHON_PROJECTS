# global variable
product = []
price = []

# main function
while True:
    productName = input("Enter your product: ")
    quantity = int(input("How many would you want to buy: "))
    priceTag = float(input("Enter the product price: "))
    productPrice = priceTag * float(quantity)

    product.append(productName)
    price.append(productPrice) 
    choice = input("Would you like to add a product again (q) to quit: ").lower()
    if choice == "q":
        break



for productName in product:
    print(productName)

for priceTag in price:
    total += priceTag

    

    