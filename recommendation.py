import pandas as pd
import numpy as np
from lightfm import LightFM
from lightfm.data import Dataset
import pickle

# Load and prepare datasets

def load_data():
    movies_df = pd.read_csv('./data/tmdb_5000_movies.csv')  # Use relative path
    credits_df = pd.read_csv('./data/tmdb_5000_credits.csv')  # Use relative path

    return movies_df, credits_df


def prepare_data(movies_df, credits_df):
    user_ids = movies_df['id'].unique().tolist()[:]  # limit for example
    item_ids = credits_df['movie_id'].unique().tolist()[:]  # limit for example

    dataset = Dataset()
    dataset.fit(users=user_ids, items=item_ids)

    interactions, _ = dataset.build_interactions([(user, item) for user, item in zip(user_ids, item_ids)])
    return dataset, interactions

# Train LightFM model
def train_model(interactions):
    model = LightFM(loss='warp')
    model.fit(interactions, epochs=10, num_threads=2)
    return model

# Compute similarity matrix based on LightFM embeddings
def compute_similarity_matrix(model, interactions):
    item_embeddings = model.get_item_representations()[1]  # Get item embedding weights
    similarity_matrix = np.dot(item_embeddings, item_embeddings.T)
    return similarity_matrix

# Save data and similarity matrix for later use
def save_model_data(movies_df, similarity_matrix):
    with open('model/movie_list.pkl', 'wb') as f:
        pickle.dump(movies_df[['id', 'title']], f)  # Save only necessary columns
    with open('model/similarity.pkl', 'wb') as f:
        pickle.dump(similarity_matrix, f)

# Main function to generate and save data
def generate_data():
    movies_df, credits_df = load_data()
    dataset, interactions = prepare_data(movies_df, credits_df)
    model = train_model(interactions)
    similarity_matrix = compute_similarity_matrix(model, interactions)
    save_model_data(movies_df, similarity_matrix)

# Call to generate data
generate_data()
