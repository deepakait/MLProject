import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #format of the log file name
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)     #Log folder gets created in the current working directory. Files will have name starting with "logs"+filename
os.makedirs(logs_path,exist_ok=True)    #Even though there is a file named logs_path , keep appending 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",     #[2023-07-18 02:11:57,600] 17 root - INFO - Logging has started
    level=logging.INFO,
)

# if __name__=="__main__":
#     logging.info("Logging has started")