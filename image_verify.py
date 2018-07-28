from PIL import Image
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        size= (img.size[0])

        
        # corrupted images have set size (32,32)
        if size<40:

        	print ('removing')
        	os.remove("/home/ip-d/Documents/e-commerce/SHORTS/"+str(filename))
        	
    
load_images_from_folder("/home/ip-d/Documents/e-commerce/SHORTS")