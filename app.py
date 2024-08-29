import streamlit as st
import pickle
import pandas as pd

# Load data
movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

# Function to recommend 10 similar movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:11]

    recommendations = []
    for i in movies_list:
        movie_id = i[0]
        recommendations.append(movies.iloc[movie_id].title)
    return recommendations

# Set the page layout and title
st.set_page_config(page_title='Movie Recommender', page_icon=':clapper:', layout='wide')

# Header
st.markdown("<h1 style='text-align: center; color: #FFA07A;'>Movie Recommender System</h1>", unsafe_allow_html=True)

# Movie selection box
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

# Button to show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    # Display recommendations
    if recommended_movie_names:  # Check if the list is not empty
        st.markdown("<h3 style='text-align: center; color: #4682B4;'>Recommended Movies</h3>", unsafe_allow_html=True)
        for i in recommended_movie_names:
            st.write(f"- {i}")
    else:
        st.write("No recommendations found.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ by Himanshu Nagapure </p>", unsafe_allow_html=True)