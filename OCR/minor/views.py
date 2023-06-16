from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import os
import cv2
import pytesseract as pt
from PIL import Image
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Create your views here.

def index(request):
    context={'a':1}
    return render(request,'index.html',context)
#This is a Django view function that returns an HTML page rendered by the Django template engine.
#  It renders a template called "index.html" and passes a dictionary context as a context variable.
def predicttext(request):
    if request.method == 'POST':
        base_dir = r"C:\Users\chaud\OneDrive\Desktop\ocr final\OCR\media"
#checks whether the request method is POST
#If it is POST, the function initializes a base directory where the images will be saved.

        file_obj = request.FILES['filepath']
        fs = FileSystemStorage()             #it will help to store the image in the System
        filePathName = fs.save(file_obj.name,file_obj)
        filePathName = fs.url(filePathName)
        image_name = file_obj.name
        print(image_name)
        imageName = image_name
        
        file_path = os.path.join(base_dir,image_name)

#This block of code retrieves the uploaded image file from the POST request
#stores it using Django's FileSystemStorage, and assigns a URL to access the stored file
#and the image to image_name 
#os.path.join()

        test_img_path = r'C:\Users\chaud\OneDrive\Desktop\ocr final\OCR\media'
        create_path = lambda f : os.path.join(test_img_path, f)
        test_image_files = os.listdir(test_img_path)
        
        def show_image(img_path, size=(224, 224)):
            image = cv2.imread(img_path)
            image = cv2.resize(image, size)
            
        base_dir = r"C:\Users\chaud\OneDrive\Desktop\ocr final\OCR\media"

        image = cv2.imread(file_path) 
          
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        avb_langs = pt.get_languages(config='hin')
        path = create_path(file_path)
#image using OpenCV and assigns it to the image variable
#show_image() which takes an image path and size as inputs and resizes the image.
#  It also defines test_img_path,
#  which is the path where the test images are stored, 
# and create_path(), which constructs a full path to an image file.          
    
        image = Image.open(path)
        
        text = pt.image_to_string(image, lang='hin')

        context = {'filePathName': filePathName, 'imageName':imageName,'text': text,'file_path':file_path }
        return render(request,'index.html',context)
#it opens the image file using PIL and assigns it to the image variable. 
# It then uses Pytesseract to perform OCR on the image and extract the text. 
# Finally, it constructs a dictionary context containing variables to be passed to the index.html template and 
# returns the rendered HTML page.

    #else:
    #    return render(request, 'error.html')