def get_file_content(filePath):
    with open('f:/py/OcrCar/'+filePath+'.jpg','rb') as file:
        return file.read()