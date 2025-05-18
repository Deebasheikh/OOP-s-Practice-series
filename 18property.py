class Product:
    def __init__(self,price):
        self._price = price    #internal variable
    @property
    def price(self):
        return self._price  
    @price.setter
    def price(self,new_price):
        if not isinstance (new_price,int):
            raise ValueError ("Price must be in numbers")
        self._price = new_price
    @price.deleter
    def price(self):
        print("Price deleted successfully")
        del self._price
#  create product price
product = Product(60)    
print(f"Product Price: {product.price}")
# set new price using setter method
product.price = 70
print(f"Updated price: {product.price}")
# Delete price using deleter
del product.price

# Try to access deleted price (will raise AttributeError)
try:
    print(product.price)
except AttributeError as e:
    print("Error:", e)


