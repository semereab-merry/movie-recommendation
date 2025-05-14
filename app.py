from flask import Flask, request, jsonify, render_template
import joblib
import os
import gdown

app = Flask(__name__)

# Correct file path and name
model_path = "model.pkl"
file_id = "1zYF5aBPaQUjz89xAQL9-WcUXlFnwIej2"  
url = f"https://drive.google.com/uc?id={file_id}"

# Download model if not already downloaded
if not os.path.exists(model_path):
    print("Downloading model...")
    gdown.download(url, model_path, quiet=False)

# Load the model from the correct path
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_name = data.get('movie')
    
    # The model has a recommend method that returns top 5 movies
    recommendations = model.recommend(movie_name)
    
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
