import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("MOVIE_RATINIG_ANALYZER")
genres=["horror","comedy","action","adventure","romantic"]

movies=[]

np.random.seed(42)
for i in range(1,31):
    movies.append([
        i,
        f"Movie_{i}",
        np.random.choice(genres),
        round(np.random.uniform(1,10),1),
        np.random.randint(100,10000),
        np.random.randint(2015,2026),
        np.random.randint(80,180),
        np.random.randint(15,60)
    ])

df=pd.DataFrame(
    movies,
    columns=[
        "movie_id",
        "movie_name",
        "genre",
        "rating",
        "votes",
        "release_year",
        "watch_time",
        "user_age"
    ]
)
print(df)
st.text("Data Overview :")
# st.dataframe(df)

# Analysis Section


#Best genre according to ratings
st.text("Best genre according to rating :")
best_genre_rating=df.groupby("genre")["rating"].mean().sort_values(ascending=False)
st.write(best_genre_rating)



#Best genre according to votes 
st.text("Best genre according to votes :")
best_genre_vote=df.groupby("genre")["votes"].mean().sort_values(ascending=False)
# print(best_genre_vote)
st.write(best_genre_vote)

#Genre popularity
st.text('genre popularity')
fig,ax=plt.subplots()
df["genre"].value_counts().plot(
    kind="bar",
    ax=ax
)
st.pyplot(fig)

#Rating trend over years
st.text("Rating trend over years")
trend=df.groupby("release_year")["rating"].mean()
fig,ax=plt.subplots()
trend.plot(kind="line",marker="o",ax=ax)
st.pyplot(fig)


#Pivot table on genre




st.text("Pivot tables on different functions :")
st.text("According to mean :")
pivot_mean=pd.pivot_table(df,index="genre",values=["rating","votes","watch_time","user_age"])
st.write(pivot_mean)

st.text("According to sum :")
pivot_sum=pd.pivot_table(df,index="genre",values=["rating","votes","watch_time","user_age"],aggfunc="sum")
st.write(pivot_sum)

st.text("According to max :")
pivot_max=pd.pivot_table(df,index="genre",values=["rating","votes","watch_time","user_age"],aggfunc="max")
st.write(pivot_max)


#SORTING



# First way using sort_values 

#Approach1
st.text("Best rated Movie : ")
highest_rated_movie=df.sort_values("rating",ascending=False).head(1)
st.write(highest_rated_movie)
# print(highest_rated_movie)


#Approch2 using .idxmax()
highest_rated_movie=df.loc[df["rating"].idxmax()]
# print(highest_rated_movie)

#Best voted movie
st.text("Best voted Movie : ")
highest_voted_movie=df.sort_values("votes",ascending=False).head(1)
st.write(highest_voted_movie)



#Top 5's


#Using sort
st.text("Top 5 Movies according to rating :")
top_5_movies_rate=df.sort_values("rating",ascending=False).head(5)
st.write(top_5_movies_rate)
# print(top_5_movies)


#Using n_largest method to get top 5 movies according to rating and votes
top_5_movies=df.nlargest(5,"rating")
# print(top_5_movies)

st.text("Top 5 movies according to vote : ")
top_5_movies_votes=df.nlargest(5,'votes')
# print(top_5_movies_votes)
st.write(top_5_movies_votes)



#Visualization section



#Seaborn Countplot
st.text("Count of movies according to genre :")
fig,ax=plt.subplots(figsize=(6,4))
sns.countplot(x="genre",data=df,ax=ax)
# plt.show()
st.pyplot(fig)

#Seaborn Pairplot
st.text("Pairplot of different genre")
pair=sns.pairplot(df,hue="genre")
st.pyplot(pair.fig)


#Interactive dashboard

st.text("Interactive Dashboard")
selected=st.selectbox('Select Genre',df["genre"].unique())
filtered=df[df["genre"]==selected]
st.write(filtered)

#Insights

st.text('Some insights ')
st.write('Average Rating',round(df["rating"].mean(),2))
st.write('Most popular genre',df["genre"].mode()[0])

st.progress(80)

