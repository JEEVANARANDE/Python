import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:] %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir,"running.log"),level=logging.INFO,
format=logging_str,filemode='a')

logging.info("sgfsl")
class Person:
    def __init__(self,first_name,last_name,age):  #initialize constructor or method
        #instance variable 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person("Jeevan","Arande",28)
p2 = Person("gafa","gaha",27)

class Laptop:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand + " " + name

laptop1 = Laptop("Hp","au114tx",63000)
logging.info(laptop1.brand)
logging.info(laptop1.laptop_name)

logging.info(p1.first_name)
logging.info(p1.last_name)
logging.info(p1.age)
logging.info(p2.first_name)
logging.info(p2.last_name)
logging.info(p2.age)