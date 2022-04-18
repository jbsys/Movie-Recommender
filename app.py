import streamlit as st
import pandas as pd



movie_user_df = pd.read_csv('Recommenders/recs_users.csv')
movie_user_df.set_index('title', inplace=True)

action_df = pd.read_csv('Recommenders/Genre CSVs/action.csv')
action_df.set_index('title', inplace=True)

animation_df = pd.read_csv('Recommenders/Genre CSVs/animation.csv')
animation_df.set_index('title', inplace=True)

comedy_df = pd.read_csv('Recommenders/Genre CSVs/comedy.csv')
comedy_df.set_index('title', inplace=True)

crime_df = pd.read_csv('Recommenders/Genre CSVs/crime.csv')
crime_df.set_index('title', inplace=True)

documentary_df = pd.read_csv('Recommenders/Genre CSVs/documentary.csv')
documentary_df.set_index('title', inplace=True)

drama_df = pd.read_csv('Recommenders/Genre CSVs/drama.csv')
drama_df.set_index('title', inplace=True)

fantasy_df = pd.read_csv('Recommenders/Genre CSVs/fantasy.csv')
fantasy_df.set_index('title', inplace=True)

st.title("Movie Recommender") 

st.write("Welcome! This is the place where you can customize what you want to watch based off of mood, feelings about 'Friends', & favorite movies!")
st.markdown("##")

genre = st.radio(
     "What's today's vibe?",
     ('Action/Adventure', 'Comedy', 'Drama/Romance', 
     'Crime/Thriller/Horror/Mystery', 'Documentary/War/Western', 'Fantasy/Sci-Fi',
     'Animation/Children', 'Any'))

if genre == 'Action/Adventure':
    recs_df = action_df
elif genre == 'Animation/Children':
    recs_df = animation_df
elif genre == 'Comedy':
    recs_df = comedy_df
elif genre == 'Drama/Romance':
    recs_df = drama_df
elif genre == 'Crime/Thriller/Horror/Mystery':
    recs_df = crime_df
elif genre == 'Documentary/War/Western':
    recs_df = documentary_df
elif genre == 'Fantasy/Sci-Fi':
    recs_df = fantasy_df
else:
    recs_df = movie_user_df
#    st.write("Respect.")


#st.markdown("##")
movie_options = st.selectbox(label='Movies', options=recs_df.index.tolist())

mood = st.select_slider(
     "Would you say you're a fan of the tv show, Friends ?",
     options=['Absolutely not.', 'Entertaining enough', 'Love (AKA I have 0 taste)'])

if mood == 'Absolutely not.':
    recs = recs_df[movie_options].sort_values().index[1:21]
    st.write('I knew you had good taste!')
elif mood == 'Entertaining enough':
    recs = recs_df[movie_options].sort_values().index[21:41]
    st.write("Okay.. I'm suspicious of your television taste...")
else:
    recs = recs_df[movie_options].sort_values().index[41:61]
    st.write("Oof. I will pray for you.")

st.markdown("##")

st.subheader("Let's look at some recommendations!")

#title = st.text_input('Enter your movie title here :-)')

#movie_options = st.selectbox(label='movies', options=movie_user_df.index.tolist())

if st.button('Recommend'):  
    #title = movie_user_df[movie_user_df.index == movie_options].index
    #recs = movie_user_df[movie_options].sort_values(ascending=False).index[0:7]
    #st.text(recs)
    col1, col2 = st.columns(2)
    with col1:
        st.text(recs[0])
    with col2:
        st.text(recs[1])
    col3, col4 = st.columns(2)
    with col3:
        st.text(recs[2])
    with col4:
        st.text(recs[3])
    col5, col6 = st.columns(2)
    with col5:
        st.text(recs[4])
    with col6:
        st.text(recs[5])
    col7, col8 = st.columns(2)
    with col7:
        st.text(recs[6])
    with col8:
        st.text(recs[7])
    col9, col10 = st.columns(2)
    with col9:
        st.text(recs[8])
    with col10:
        st.text(recs[9])
    col11, col12 = st.columns(2)
    with col11:
        st.text(recs[10])
    with col12:
        st.text(recs[11])
    col13, col14 = st.columns(2)
    with col13:
        st.text(recs[12])
    with col14:
        st.text(recs[13])
    col15, col16 = st.columns(2)
    with col15:
        st.text(recs[14])
    with col16:
        st.text(recs[15])
    col17, col18 = st.columns(2)
    with col17:
        st.text(recs[16])
    with col18:
        st.text(recs[17])
    col19, col20 = st.columns(2)
    with col19:
        st.text(recs[18])
    with col20:
        st.text(recs[19])