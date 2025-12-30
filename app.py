import streamlit as st
import pickle
import base64
import requests
import streamlit.components.v1 as components


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c08eaf643876504cca1e0707a82c8c39&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.title("🎬 Movie Recommendation System")
selectvalue = st.selectbox("Select movie from dropdown", movies_list)

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[0:5]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster



if st.button("Show Recommend"):
    movie_name, movie_poster= recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        # st.image(movie_poster[4])



# Function to add background + transparent overlay
def add_bg_with_opacity(image_path, opacity=0.55):
    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: 
            linear-gradient(rgba(0,0,0,{opacity}), rgba(0,0,0,{opacity})),
            url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}

    h1, h2, h3, p, label {{
        color: white !important;
    }}
    </style>
    """
   
    st.markdown(css, unsafe_allow_html=True)

add_bg_with_opacity("moviebg.jpg", opacity=0.55)


st.markdown("""
    <style>
    .stButton>button {
        background-color: red;
        color: white;
        
    }
    </style>
""", unsafe_allow_html=True)

# import streamlit.components.v1 as components

# imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


# imageUrls = [
#     fetch_poster(1632),
#     fetch_poster(299536),
#     fetch_poster(17455),
#     fetch_poster(2830),
#     fetch_poster(429422),
#     fetch_poster(9722),
#     fetch_poster(13972),
#     fetch_poster(240),
#     fetch_poster(155),
#     fetch_poster(598),
#     fetch_poster(914),
#     fetch_poster(255709),
#     fetch_poster(572154)
