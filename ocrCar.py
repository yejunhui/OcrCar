from aip import AipOcr

APP_ID = '17217405'
API_KEY = 'oKCQOIGnzMgvs24VGfGZFcvG'
SECRET_KEY = 'GVhh0amW4gIXcZNDn5o6GO4cUbGoZTib'

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

def ocrClinet(img):
    return client.licensePlate(img)
