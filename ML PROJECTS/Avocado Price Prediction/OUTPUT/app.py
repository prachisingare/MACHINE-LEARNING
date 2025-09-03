from flask import Flask, render_template, request
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect form data
        total_volume = float(request.form["total_volume"])
        total_bags = float(request.form["total_bags"])
        small_bags = float(request.form["small_bags"])
        large_bags = float(request.form["large_bags"])
        xlarge_bags = float(request.form["xlarge_bags"])
        year = int(request.form["year"])
        avocado_type = 1 if request.form["type"] == "organic" else 0
        region = request.form["region"]

        # NOTE: encode region properly (same encoding as during training)
        # Example: using dummy encoding dictionary
        region_mapping = {"Albany": 0, "California": 1, "Chicago": 2}
        region_encoded = region_mapping.get(region, 0)

        # Prepare input
        features = np.array([[total_volume, total_bags, small_bags, 
                              large_bags, xlarge_bags, avocado_type, 
                              year, region_encoded]])
        
        # Predict
        prediction = model.predict(features)[0]
        
        return render_template("index.html", prediction_text=f"Predicted Price: ${prediction:.2f}")
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
