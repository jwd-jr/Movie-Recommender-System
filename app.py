import streamlit as st
import pandas as pd
import numpy as np

import pickle
filn_list=pickle.load(open('movie_list.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
filn=pd.DataFrame(filn_list)


st.title("Movie Recommender System")

def recommend(movie):
    index = filn[filn['title'] == movie].index[0]
    distances = similarity[index]
    filn_lis = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]
    recommended_movies = []
    for i in filn_lis:
        filn_id = i[0]
        recommended_movies.append(filn.iloc[i[0]].title)
    return recommended_movies




selected_movie_name = st.selectbox("Type or select a movie from the dropdown",
    filn['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

