from vendingMachine import VendingMachine
from product import Product
from purchase import Purchase



def makePurchase(productId, count, amount):

    vendingMachine = VendingMachine()

    product = Product(productId,count)

    purchase = Purchase(product, amount)
    
    vendingMachine.getProduct(purchase)


makePurchase(1, 8, 50)