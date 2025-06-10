import requests
from io import BytesIO
from PIL import Image
import base64
import math

PIXEL_LIMIT = 50_000_000  # Same as Odoo's internal limit

# # 1. Get image from URL
# image_url = "https://example.com/your_image.jpg"
# response = requests.get(image_url)
# response.raise_for_status()

# # 2. Open the image
# img = Image.open(BytesIO(response.content))

# remove the following 2 lines when want to add dynamic urls.
img_path = '/home/pratham/Desktop/trials/image.png'
img= Image.open(img_path)

width, height = img.size
total_pixels = width * height
print('------------------------', height,'--------', width)

# 3. Resize if image exceeds pixel limit
if total_pixels > PIXEL_LIMIT:
    # Calculate scale factor to bring image below pixel limit
    scale_factor = math.sqrt(PIXEL_LIMIT / total_pixels)
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    print('------------------------', new_height,'--------', new_width)
    print('----------------------resol',new_height*new_width)

img.save('resizedimg.png')

# # 4. Convert to base64
# buffered = BytesIO()
# img_format = 'PNG' if img.mode in ('RGBA', 'LA') else 'JPEG'
# img.save(buffered, format=img_format)
# img_base64 = base64.b64encode(buffered.getvalue())

# # Optional: Use it as string for storing in DB
# img_base64_str = img_base64.decode('utf-8')
