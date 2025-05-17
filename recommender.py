import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

class MovieRecommender:
    def __init__(self, features_matrix, movies):
        self.movies = movies
        self.model = NearestNeighbors(metric="cosine", algorithm="brute")
        self.model.fit(features_matrix)

    def recommend(self, movie_name, n=6):
        distances, indices = self.model.kneighbors(
            self.movies.loc[movie_name, :].values.reshape(1, -1),
            n_neighbors=n
        )
        results = []
        for i in range(1, len(distances.flatten())):
            results.append(self.movies.index[indices.flatten()[i]])
        return results