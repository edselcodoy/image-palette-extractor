# 🖼️🎨 Image Palette Extractor


This app extracts the colors and generate the palette of images for design and theming purposes. 

Upload images (currently supporting **.jpg** and **.png** extensions only) in the app and choose the number of colors (**1 - 10** only) you want to be extracted from the image. By clicking any of the color from the palette, the color's hex code is copied for ease and convenience.

Through the use of unsupervised machine learning, pixels are clustered which results in obtaining the top *k* colors (RGB values). 

You can also run this locally by 
1. Cloning this repository,
2. Installing dependencies, and
   ```
   pip install -r requirements.txt
   ```
3. Running the Flask app.
    ```
        flask run 
    ```
