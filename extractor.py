from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def get_palette(image, n_colors):
    img = Image.open(image)
    img = img.convert("RGB")
    img = img.resize((500, 500))
    arr = np.asarray(img)
    w, h, d = arr.shape
    arr = arr.reshape(-1, d)
    model = KMeans(n_clusters=n_colors, n_init=1, random_state=28).fit(arr)
    return list(np.uint8(model.cluster_centers_))