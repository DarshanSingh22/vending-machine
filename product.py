import json



class Product:

    __products__ = {}

    def __init__(self, Id, count):

        self.__products__ = self.__loadProducts__('products.json')

        self.productId = str(Id)
        self.count = count

        self.price = self.__getPrice__()



    def __getPrice__(self):
        product = self.__getProduct__()

        return product['price']



    def __getProduct__(self):
        return self.__products__.get(self.productId)

    

    def __loadProducts__(self, json_file):

        with open(json_file, 'r') as file:
            return json.load(file)



    def getCount(self):
        product = self.__getProduct__()

        return product['count']
    


    def updateStorage(self):
        product = self.__getProduct__()
    
        product['count'] -= self.count

        self.__updateJson__()

        print("Reducing count by {}".format(self.count))



    def __updateJson__(self):
        with open('products.json', 'w') as file:
            json.dump(self.__products__, file)
    