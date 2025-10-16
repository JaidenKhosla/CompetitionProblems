import os
import shutil
from pdf2image import convert_from_path

problems_folder = "./problems"

def deepSearch(path: str, counter = 0):
    for instance in os.listdir(path):

        counter+=1

        absPath = f"{path}\\{instance}"
        
        instanceName = instance[:instance.find(".")]

        if os.path.isfile(absPath):
            if instance.endswith(".png"): 
                os.mkdir(f"{problems_folder}/{instanceName}")
                shutil.copy(absPath, f"{problems_folder}/{instanceName}/1.png")
            elif instance.endswith(".pdf"):
                pdfImages = convert_from_path(absPath)
                os.mkdir(f"{problems_folder}/{instanceName}{counter}")
                for idx, image in enumerate(pdfImages):
                    image.save(f"{problems_folder}/{instanceName}{counter}/{idx}.jpeg")
        elif not instance == "problems":
            deepSearch(absPath, counter)




deepSearch(os.getcwd())




