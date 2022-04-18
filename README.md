# Movie-Recommender System

The goal of this system is to recommend movies based on user profiles. I have created systems using both item-based and user-based approaches. The final result is an easy app that takes in genre-preference, thoughts on the TV show, Friends, and previously liked movies. The result is 20 movie recommendations, all within seconds. 

The main changes to our original dataset was turning dates into days of the week, requiring a minimum of 30 reviews per users and 20 reviews per movies, and breaking up genres into top 3. The resultant dataframe includes 1820 unique movies. 

It was also interesting to pull information from IMDb's website and compare their top list to MovieLens'. I did this by applying the same equation IMDb uses to my dataset.

To wrap everything up and upload it to Streamlit, I created dataframe's for every class of genre. I split them up accordingly: - - Children & Animation 
Comedy
Drama & Romance
Crime, Thriller, Horror, Mystery
Documentary, War, Western
Action & Adventure
Fantasy & Sci-Fi