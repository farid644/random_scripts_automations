import pyautogui
from  PIL import  Image
import os

myScreenshot = pyautogui.screenshot()
pngpath=(r'/Users/faridbabayev/PycharmProjects/Git/local_scripts/2.png')
myScreenshot.save(pngpath)

image=Image.open(r'/Users/faridbabayev/PycharmProjects/Git/local_scripts/2.png')
image_var=image.convert('RGB')
pdfpath=(r'/Users/faridbabayev/PycharmProjects/Git/local_scripts/2.pdf')
image_var.save(pdfpath)

os.remove(pngpath)


