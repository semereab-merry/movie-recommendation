from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__)

# Load your trained recommendation model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    movie_name = data.get('movie')
    
    # Assume model has a recommend method that returns top 5 movies
    recommendations = model.recommend(movie_name)
    
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # use PORT env var if available
    app.run(host='0.0.0.0', port=port)
