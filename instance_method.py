import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:] %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir,"running.log"),level=logging.INFO,
format=logging_str,filemode='a')


#instance method
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

p1= Person("Jeevan","Arande",28)

logging.info(p1.full_name())

