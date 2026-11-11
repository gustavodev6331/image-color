from PIL import Image, UnidentifiedImageError
import numpy as np
from sklearn.cluster import KMeans
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    color_palette = []
    error = None

    if request.method == 'POST':
        uploaded_file = request.files.get("image")

        if not uploaded_file or uploaded_file.filename == "":
            error = "Please select an image."

        else:
            try:
                image = Image.open(uploaded_file)
                image = image.convert("RGB")

            except (UnidentifiedImageError, OSError, ValueError):
                error = "Invalid image file. Please upload a valid image."

            else:
                image_array = np.array(image)
                pixels = image_array.reshape(-1,3)

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
                    color_palette.append({
                        "hex": hex_color,
                        "quantity": int(quantity),
                    })

    return render_template('index.html', colors=color_palette, error=error)


if __name__ == '__main__':
    app.run(debug=True)