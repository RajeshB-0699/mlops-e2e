import os
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

MODEL_PATH = "model/iris_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise Exception("Model not found")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])[0]

    return render_template(
        "index.html", prediction_text=f"Predicted Iris class:{prediction}"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
