from purchase import Purchase
from product import Product



class VendingMachine:


    def getProduct(self, purchase: Purchase):

        if not self.__isProductAvailable__(purchase.product):
            self.__dispenseFullRefund__(purchase.amount)
            return

        if not self.__isValidPurchase__(self.purchase):
            self.__dispenseFullRefund__(purchase.amount)
            return
        
        self.__dispenseProduct__(purchase)
 


    def __isProductAvailable__(self, product: Product):
        return product.getCount() >= product.count
    


    def __isValidPurchase__(self, purchase: Purchase):
        return purchase.product.price * purchase.product.count <= purchase.amount
        


    def __dispenseFullRefund__(self, amount):
        print("Dispense Full Refund of {} Rupees".format(amount))
        self.__dispenseChangesOrFullRefund__(amount)



    def __dispenseChanges__(self, amount):
        print("Dispense Changes for {} Rupees".format(amount))
        self.__dispenseChangesOrFullRefund__(amount)
    


    def __dispenseChangesOrFullRefund__(self, amount):
        # call for return action
        pass
    


    def __dispenseProduct__(self, purchase: Purchase):
        # call for string spin action
        print("Dispense {} Product for ProductId {}: ".format(purchase.product.count, purchase.product.productId))

        # TODO: Wait for scan event to be fire before continuing
        # If event is scanPositive then dispense the changes 
        # If event is scanNegative then dispense the full refund

        self.__dispenseChanges__(purchase.amount - purchase.product.price * purchase.product.count)
        purchase.product.updateStorage()


