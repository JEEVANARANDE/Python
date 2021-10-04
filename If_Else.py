import logging
import os

logging_str = "[%(asctime)s: %(levelname)s: %(module)s:] %(message)s"
log_dir = "logs"
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(filename=os.path.join(log_dir,"running.log"),level=logging.INFO,
format=logging_str,filemode='a')



def Age_check(n=None):
    try:
        if n==None:
            n = int(input("Enter your Age : "))
        assert n>0 and int(n)==n ,f"Values should be Integer and greater then 0, But we got {n}"
        if n >= 14:
            return f"Number is above 14 i.e {n}"
        else:
            return f"Number is below 14 i.e {n}"
    except Exception as e:
        return e

logging.info(Age_check()) 
logging.info(Age_check(0)) 
logging.info(Age_check(1)) 
logging.info(Age_check(15)) 
logging.info(Age_check("dfghdfz")) 
logging.info(Age_check(-11)) 

