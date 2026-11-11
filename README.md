# Image Color Extractor

A web application built with Python and Flask that extracts the 10 most dominant colors from an uploaded image using K-Means clustering. Displays each color as a visual swatch with its HEX code and pixel count, allowing users to copy HEX values with a single click.

## Screenshots

<img width="1470" height="834" alt="Screenshot 2026-11-11 at 3 27 23 PM" src="https://github.com/user-attachments/assets/7b031d10-1a69-4b34-adff-c721c44db0ac" />

<img width="1470" height="834" alt="Screenshot 2026-11-11 at 3 27 39 PM" src="https://github.com/user-attachments/assets/1252cd1c-aef9-4851-9978-71d42df06036" />


## Features

- Upload images directly through the web interface.
- Extract the 10 most dominant colors using K-Means clustering.
- Convert RGB values into HEX color codes.
- Display colors ranked by pixel frequency.
- Copy HEX codes to the clipboard with one click.
- Validate uploaded files and handle invalid images.
- Responsive interface for different screen sizes.

## Technologies

- **Python** – Core application logic
- **Flask** – Web framework
- **Pillow** – Image processing
- **NumPy** – Pixel data manipulation
- **Scikit-learn** – K-Means clustering
- **HTML5 / CSS3** – Frontend structure and styling
- **JavaScript** – Clipboard functionality
- **Jinja2** – Dynamic HTML rendering

## How It Works

1. The user uploads an image through the web interface.
2. Pillow opens the image and converts it to RGB format.
3. NumPy transforms the image into an array of RGB pixels.
4. K-Means clustering groups similar colors into 10 clusters.
5. The average RGB value of each cluster is calculated.
6. Colors are sorted by the number of pixels assigned to each cluster.
7. The application converts the RGB values into HEX codes and displays the resulting palette.

## Installation

Clone the repository:

```bash
git clone https://github.com/gustavodev6331/image-color.git
```

Navigate to the project directory:

```bash
cd image-color
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install the dependencies:

```bash
pip install flask pillow numpy scikit-learn
```

Run the application:

```bash
python main.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Usage

1. Select an image from your computer.
2. Click **Extract Colors**.
3. View the 10 most dominant colors in the generated palette.
4. Click any HEX code to copy it to your clipboard.

## Author

**Gustavo Sene**

[GitHub Profile](https://github.com/gustavodev6331)
