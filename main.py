from PIL import Image
import numpy as np


image = Image.open('Screenshot 2026-11-10 at 7.22.31 PM.png')
image = image.convert("RGB")
image_array = np.array(image)

# print(image_array[0][0][:3])
# print(image_array.shape)

print(np.unique(image_array))