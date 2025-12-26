import sys
import yaml
import base64

from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging

def read_yaml(file_path: str)-> dict:
    try:
        with open(file_path,'rb') as yaml_file:
            logging.info('Read yaml file successfully')
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise AppException(e,sys) from e
    

def write_yaml_file(file_path:str,content:object,replace:bool=False)->None:

    try:
        with open(file_path,'w') as file:
            yaml.dump(content,file_path)
            logging.info('Successfully write_yaml_file')


    except Exception as e:
        raise AppException(e,sys)


def decodeImage(imgstring,fileName):
    try:
        imgdata = base64.b16decode(imgstring)
        with open("./data/" + fileName,'wb') as f:
            f.write(imgdata)
            f.close()

    except Exception as e:
        raise AppException(e,sys)


def encodeImageIntoBase64(croppedImagePath):
    try:
        with open(croppedImagePath,'rb') as f:
            return base64.b64decode(f.read())
    except Exception as e:
        raise AppException(e,sys)




