import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:] %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir,"running.log"),level=logging.INFO,
format=logging_str,filemode='a')


# single try
try:
    1/0
except Exception as e:
    logging.info(e)

#double try

try:
    1/0
except Exception as e:
    logging.info("adafggga")
try:
    logging.info("This is a Program")
except :
    logging.info("fdscg")

try:
    a=10/0
    f=open("test.txt","r")
    f.write("This is my file")
    
except IOError as e:
    logging.error(e)
except ZeroDivisionError as e:
    logging.error(e)
