import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("Online_Course_Performance_Tracker")
students=[]
courses=["Data Science","AIML","Python","GEN AI"]

np.random.seed(42)
for i in range(1,51):
    students.append([
        i,
        f"Student_name{i}",
        np.random.choice(courses),
        np.random.randint(1,100),
        np.random.randint(1,100)
    ])


df=pd.DataFrame(students,columns=["student_id","student_name","course","Quiz_Score","Progress_percentage"])

# print(df.head())

df["Completion_Status"]=pd.cut(
    df["Progress_percentage"],
    bins=[0,49,99,100],
    labels=["Not_Started","In_progress","Completed"]
)
# print(df.head())
st.text("Complete Data Overview :")
st.dataframe(df)


#Group by

#1 Course wise average Quiz score :
st.text("Average Quiz score course wise :")
course_wise_quiz_score=df.groupby("course")["Quiz_Score"].mean()
st.write(course_wise_quiz_score)
# print(course_wise_quiz_score)

#2 Course_wise_avg_progress
st.text("Average Progress course wise :")
Course_wise_avg_progress=df.groupby("course")["Progress_percentage"].mean()
st.write(Course_wise_avg_progress)
# print(Course_wise_avg_progress)


#Completion status count student
st.text("Completion status count of student : ")
completion=df.groupby("Completion_Status")["student_name"].count()
st.write(completion)
# print(completion)


#Visualization

st.text("Quick Performance Visualization :")
pivot_df=df.pivot_table(
    index="course",
    columns="Completion_Status",
    values="student_id",
    aggfunc="count"
).fillna(0).astype(int)
st.write(pivot_df)

st.text("Student Performance Heatmap :")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, fmt='d', cmap='YlGnBu', ax=ax)
ax.set_title('Student Performance Heatmap')
st.pyplot(fig)

st.success('Dashboard completed')