Movie Recommendation System Summary
This project implements a content-based movie recommendation system that suggests the 10 most similar movies to a given input. The core methodology involves text vectorization and similarity measurement using two popular techniques:

CountVectorizer: This method converts the movie descriptions into a matrix of token counts, enabling the system to represent each movie as a vector of word frequencies.
TF-IDF (Term Frequency-Inverse Document Frequency): This technique enhances the CountVectorizer by weighing the frequency of words in each movie description against how common those words are across all movies, helping to emphasize more distinctive terms.
To determine the similarity between movies, cosine similarity is used, which measures the cosine of the angle between two vectors—allowing for a direct comparison of movie descriptions.

After evaluating both methods, TF-IDF was found to outperform CountVectorizer in capturing the nuances of the movie content, resulting in more accurate and relevant recommendations. As a result, the final system leverages TF-IDF for text vectorization, ensuring high-quality recommendations that closely match the content of the input movie.

This system provides a robust and effective way to discover similar movies based on content, making it a valuable tool for users looking to explore new films that align with their preferences.

Check it out : https://recommend-movie-sys.streamlit.app
