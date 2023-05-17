import requests


class Person:
    def __init__(self, naam, kaam):
        self.name = naam
        self.occupation = kaam

    def info(self):
        print(f"{self.name} is a {self.occupation}")

    def getSingleProduct(self):
        id = 3
        url = f'https://fakestoreapi.com/products/{id}'
        x = requests.get(url)
        print(x.json())

    def getProductWithLimit(self):
        id = 3
        url = f'https://fakestoreapi.com/products?limit=5'
        x = requests.get(url, json=myjson)
        print(x.json())

    def addProduct(self):
        url = f'https://fakestoreapi.com/products'
        x = requests.post(url, json={
            "title": 'test product',
            "price": 13.5,
            "description": 'lorem ipsum set',
            "image": 'https://i.pravatar.cc',
            "category": 'electronic'
        })
        print(x.json())


person_1 = Person("Ali", "Mali")
# person_2 = Person("Khan", "Phatan")

person_1.info()
person_1.addProduct()

# person_2.info()
# person_2.getProducts()
