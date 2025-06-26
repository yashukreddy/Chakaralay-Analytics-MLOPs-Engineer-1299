from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np
import os
import random
import time

app = Flask(__name__)

# Load model
model = load_model('animal_classification_model.h5')

class_names = [
    'Bear', 'Bird', 'Cat', 'Cow', 'Deer', 'Dog', 'Dolphin', 
    'Elephant', 'Giraffe', 'Horse', 'Kangaroo', 'Lion', 
    'Panda', 'Tiger', 'Zebra'
]

# Metrics
total_requests = 0
successful_predictions = 0
total_latency = 0.0


# Image preprocessing
def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array


@app.route("/", methods=["GET", "POST"])
def index():
    global total_requests, successful_predictions, total_latency, latest_confidence

    prediction = None
    image_url = None
    latest_confidence = 0.0  

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            total_requests += 1
            start_time = time.time()
            filename = file.filename
            filepath = os.path.join("static", filename)
            file.save(filepath)

            try:
                img = prepare_image(filepath)
                preds = model.predict(img)[0]
                predicted_index = np.argmax(preds)
                predicted_class = class_names[predicted_index]
                confidence = float(preds[predicted_index]) * 100
                latest_confidence = confidence 

                prediction = f"Predicted Animal: {predicted_class} ({confidence:.2f}%)"
                successful_predictions += 1
                image_url = filepath
            except Exception as e:
                prediction = f"Prediction error: {e}"

            latency = time.time() - start_time
            total_latency += latency

    return render_template("index.html", prediction=prediction, image_url=image_url)

@app.route("/metrics", methods=["GET"])
def metrics():
    avg_latency = total_latency / total_requests if total_requests > 0 else 0.0
    success_rate = (successful_predictions / total_requests * 100) if total_requests > 0 else 0.0

    prometheus_metrics = (
        f"# HELP total_api_requests_total Total number of API requests\n"
        f"# TYPE total_api_requests_total counter\n"
        f"total_api_requests_total {total_requests}\n"
        f"\n"
        f"# HELP request_processing_latency_seconds Average latency for request processing\n"
        f"# TYPE request_processing_latency_seconds gauge\n"
        f"request_processing_latency_seconds {round(avg_latency, 3)}\n"
        f"\n"
        f"# HELP model_prediction_success_rate Model prediction success rate (%)\n"
        f"# TYPE model_prediction_success_rate gauge\n"
        f"model_prediction_success_rate {round(success_rate, 2)}\n"
        f"\n"
        f"# HELP latest_prediction_confidence Confidence of the latest prediction (%)\n"
        f"# TYPE latest_prediction_confidence gauge\n"
        f"latest_prediction_confidence {round(latest_confidence, 2)}\n"
    )

    return prometheus_metrics, 200, {"Content-Type": "text/plain; charset=utf-8"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
