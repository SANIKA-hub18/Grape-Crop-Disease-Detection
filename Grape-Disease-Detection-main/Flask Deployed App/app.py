import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd

# Flask App Initialization
app = Flask(__name__)

# File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "static/uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load CSV Data
disease_info_path = os.path.join(BASE_DIR, "disease_info.csv")
supplement_info_path = os.path.join(BASE_DIR, "supplement_info.csv")
disease_info = pd.read_csv(disease_info_path, encoding="cp1252")
supplement_info = pd.read_csv(supplement_info_path, encoding="cp1252")

# Load AI Model (Ensure It Only Detects Grape Diseases)
model_path = os.path.join(BASE_DIR, "plant_disease_model_1_latest.pt")
model = CNN.CNN(39)
model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
model.eval()

# Define Allowed Grape Disease Indices
grape_disease_indices = [12, 13, 14, 15]  # Indices for grape diseases

# Prediction Function
def prediction(image_path):
    image = Image.open(image_path).resize((224, 224))
    input_data = TF.to_tensor(image).unsqueeze(0)
    output = model(input_data).detach().numpy()
    index = np.argmax(output)

    return index if index in grape_disease_indices else None  # Ignore non-grape detections

# Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def ai_engine():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if "image" not in request.files:
        return redirect(request.url)

    image = request.files["image"]
    if image.filename == "":
        return redirect(request.url)

    file_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(file_path)

    pred = prediction(file_path)
    if pred is None:
        return render_template("submit.html", title="Invalid Input",
                               desc="Only grape leaves are supported.",
                               prevent="Try again with a grape leaf.",
                               image_url="/static/default.jpg")

    title = disease_info["disease_name"][pred]
    desc = disease_info["description"][pred]
    prevent = disease_info["Possible Steps"][pred]
    image_url = disease_info["image_url"][pred]
    supplement_name = supplement_info["supplement name"][pred]
    supplement_image_url = supplement_info["supplement image"][pred]
    supplement_buy_link = supplement_info["buy link"][pred]

    return render_template("submit.html", title=title, desc=desc, prevent=prevent,
                           image_url=image_url, sname=supplement_name,
                           simage=supplement_image_url, buy_link=supplement_buy_link)

if __name__ == "__main__":
    app.run(debug=True)
