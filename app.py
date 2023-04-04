from flask import Flask, render_template, request
from base64 import b64encode
from extractor import get_palette

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  
        image = request.files.get('image')
        n_colors = int(request.form.get('n_colors'))
        image_string = b64encode(image.read())
        image_string = image_string.decode('utf-8')
        palette = get_palette(image, n_colors)
        return render_template("index.html", filestring=image_string, palette=palette)
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
