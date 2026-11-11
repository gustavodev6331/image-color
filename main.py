from PIL import Image
import numpy as np
from sklearn.cluster import KMeans



image = Image.open('Screenshot 2026-11-10 at 7.22.31 PM.png')
image = image.convert("RGB")

image_array = np.array(image)
pixels = image_array.reshape(-1,3)

color, quantity = np.unique(pixels, axis=0, return_counts=True)

sorted_indices = quantity.argsort()[::-1][:10]

sorted_color = color[sorted_indices]
sorted_quantity = quantity[sorted_indices]

kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(pixels)
centers = kmeans.cluster_centers_

labels = kmeans.labels_
count = np.bincount(labels)

sorter_indices = count.argsort()[::-1]
sorted_center = centers[sorter_indices]
sorted_count = count[sorter_indices]

int_center = sorted_center.astype(int)

for color, quantity in zip(int_center, sorted_count):

    hex_color = "#{:02X}{:02X}{:02X}".format(*color)

    print(f"{hex_color}: {quantity:,}pixels")


