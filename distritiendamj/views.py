# views.py
from django.http import HttpResponse
from django.conf import settings
import mimetypes
import os

def product_image_view(request, image_name):
    # Construct the full path to the image file
    image_path = os.path.join(settings.MEDIA_ROOT + "/producto", image_name)
    print(image_path) 
    # Check if the file exists
    if os.path.exists(image_path):
        # Open the image file and read its content
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        # Determine the content type based on the file extension
        content_type, _ = mimetypes.guess_type(image_name)
        if content_type is None:
            content_type = 'application/octet-stream'

        # Return the image as an HTTP response
        response = HttpResponse(image_data, content_type=content_type)
        return response
    else:
        # Handle the case where the image file does not exist
        return HttpResponse("Image not found", status=404)
