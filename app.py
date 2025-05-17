from flask import Flask, request, jsonify, render_template
import joblib
import os
import gdown
from recommender import MovieRecommender

app = Flask(__name__)

model_path = "model.pkl"
file_id = "1W_FyX1rzrak9r2uK93FM4i7cHHDrQP3O"
gdrive_url = f"https://drive.google.com/uc?id={file_id}"

# Download if the model doesn't already exist
if not os.path.exists(model_path):
    print("Model not found locally. Downloading from Google Drive...")
    gdown.download(gdrive_url, model_path, quiet=False)

# Now load the model
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
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
