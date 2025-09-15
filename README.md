<h1 align="center">🍇 Grape Crop Disease Detection</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-yellow?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-2.15-orange?logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-2.3-green?logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-2.0-blue?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Pillow-10.0-purple?logo=python&logoColor=white" />
</p>

---

<h2>📖 Overview</h2>
<p>
<strong>Grape Crop Disease Detection</strong> is a Machine Learning + Deep Learning based web application that helps in identifying different grape leaf diseases using image classification.  
It uses <strong>Convolutional Neural Networks (CNN)</strong> trained on grape leaf datasets from <strong>Kaggle</strong> to predict whether the plant is <strong>healthy</strong> or affected by diseases like <em>Black Rot</em>, <em>Esca</em>, or <em>Leaf Blight</em>.  
The model is deployed using <strong>Flask</strong> for real-time predictions.
</p>

---

<h2>✨ Features</h2>
<ul>
  <li><strong>Image Upload</strong> – Upload grape leaf images for instant prediction</li>
  <li><strong>Disease Classification</strong> – Detect common grape crop diseases with high accuracy</li>
  <li><strong>Data Preprocessing</strong> – Image enhancement using <code>Pillow</code> and <code>OpenCV</code></li>
  <li><strong>Visualization</strong> – Analyze datasets with <code>Pandas</code> & <code>Matplotlib</code></li>
  <li><strong>Web Deployment</strong> – Flask-based interface for farmers & researchers</li>
</ul>

---

<h2>⚙️ Installation</h2>
<ol>
  <li>Clone the Repository</li>
  <pre><code>git clone https://github.com/SANIKA-hub18/grape-crop-disease-detection.git
cd grape-crop-disease-detection</code></pre>

  <li>Create Virtual Environment & Install Dependencies</li>
  <pre><code>python -m venv venv
# On Linux/Mac
source venv/bin/activate
# On Windows
venv\Scripts\activate

pip install -r requirements.txt</code></pre>

  <li>Train the Model (if needed)</li>
  <pre><code>python train_model.py</code></pre>

  <li>Run the Flask Server</li>
  <pre><code>python app.py</code></pre>

  <li>Open in Browser</li>
  <pre><code>http://127.0.0.1:5000/</code></pre>
</ol>

---

<h2>📂 Project Structure</h2>
<pre>
grape_crop_disease_detection/
├── dataset/             # Training & testing images
├── models/              # Saved trained models (h5)
├── static/              # CSS, JS, Images
├── templates/           # Flask HTML templates
├── app.py               # Flask application
├── train_model.py       # Model training script
├── requirements.txt     # Dependencies
└── README.md
</pre>

---

<h2>🤝 Contributing</h2>
<p>
Contributions are welcome! Fork the repo and create a new branch:
</p>
<pre><code>git checkout -b feature/YourFeature
git commit -m "Add YourFeature"
git push origin feature/YourFeature
</code></pre>
<p>Then open a Pull Request 🚀</p>

---

<h2>📧 Contact</h2>
<p>
<strong>Maintainer:</strong> Sanika Shaligram <br>
<strong>Email:</strong> shaligramsanika@gmail.com
</p>
