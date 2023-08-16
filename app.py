import streamlit as st
import pandas as pd
import pickle

# Load the data
df = pd.read_csv('data.csv', nrows=10000)  # Adjust the number of rows as needed

# Load the recommendation model from the pickle file
with open('recommendation_model.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

# Function to get recommendations
def recommend_products(product_id, num_recommendations):
    product_idx = df[df['product_id'] == product_id].index[0]
    similar_scores = list(enumerate(cosine_sim[product_idx]))
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)
    similar_products = [i for i, _ in similar_scores][1:num_recommendations + 1]
    
    return df.iloc[similar_products][['product_id', 'product_category_name_english', 'price']]

# Streamlit UI
st.title('Product Recommendation App')
st.write("on Brazilian E-Commerce Public Dataset by Olist")

# Dropdown to select a product
product_options = df['product_id'].unique()
selected_product = st.selectbox('Select a product:', product_options)

# Get the number of recommendations
num_recommendations = st.slider('Number of recommendations:', 1, 10, 5)

# Make recommendations
if selected_product:
    recommended_products = recommend_products(selected_product, num_recommendations)

    st.write(f"Top {num_recommendations} recommended products:")
    for index, row in recommended_products.iterrows():
        st.info(f"- Product ID: {row['product_id']}, Category: {row['product_category_name_english']}, Price: {row['price']}")
