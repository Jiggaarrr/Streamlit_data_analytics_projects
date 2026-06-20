import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.header("Student_Marks_Analytics_Dashboard")
students=[]

np.random.seed(42)
for i in range(1,31):
    students.append([
        f"Student_{i}",
        np.random.randint(40,100),
        np.random.randint(40,100),
        np.random.randint(40,100),
        np.random.randint(40,100),
    ])

# print(students)

st.text("Data Overview :")
df=pd.DataFrame(students,columns=["name","phy","bio","chem","maths"])
# print(df)
st.dataframe(df)

df["total"]=(df["phy"]+df["chem"]+df["bio"]+df["maths"])
df["average"]=df["total"]/4

# print(df)

#Adding history subject
df["history"]=np.random.randint(40,100,size=len(df))
# print(df)

st.text("Topper :")
#Getting topper
topper=df.loc[df["total"].idxmax()]
# print(topper)
# print(df["total"].dtype)
st.write(topper)

st.text("Low marks kid :")
#Getting lowerr
lowest_marks_student=df.loc[df["total"].idxmin()]
# print(lowest_marks_student)
st.write(lowest_marks_student)

st.text("Subject Avg :")
#Getting weak subject
subject_avg=df[["phy","bio","chem","maths"]].mean()
# print(subject_avg)
st.write(subject_avg)


#Weak Subject
# print(subject_avg.idxmin())
st.write("The weak subject is :",f"{subject_avg.idxmin()}")

#Creating new column Performance
df["performance"]=pd.cut(df["average"],bins=[0,60,80,100],labels=["weak","average","good"])

#groupwise average ka mean()
st.text("Groupwise average :")
summary=df.groupby("performance")["average"].mean()
# print(summary)
st.write(summary)

#Students wise marks
st.text("Student Wise Marks :")
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(df["name"], df["total"])
ax.set_xlabel("Students")
ax.set_ylabel("Total Marks")
ax.set_title("Student Wise Total Marks")
plt.xticks(rotation=90)
st.pyplot(fig)

#Subject total marks
subject_total = df[["phy","bio","chem","maths"]].sum()
st.text("Subject Wise Total Marks")
fig, ax = plt.subplots(figsize=(6,4))
ax.bar(subject_total.index, subject_total.values)
ax.set_xlabel("Subjects")
ax.set_ylabel("Total Marks")
st.pyplot(fig)

st.subheader("Subjects Correlation Heatmap")
#Heatmap Correlation
st.text("All Subject Correlation :")
corr = df[["phy","bio","chem","maths"]].corr()
fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu",
    ax=ax
)
st.pyplot(fig)

#Pivot table analysis
st.text("Pivot table analysis :")
pivot=pd.pivot_table(df,index="performance",values="average")
st.write(pivot)

#Class performance trendd
st.text("Class Performance Trend :")
fig,ax=plt.subplots(figsize=(8,4))
df["average"].plot(
    kind="line",
    marker="o",
    ax=ax
)
st.pyplot(fig)


st.text("Subject Average Comparison :")
fig,ax=plt.subplots(figsize=(8,4))
subject_avg.plot(
    kind="bar",
    ax=ax
)
st.pyplot(fig)


#Adding pass fail column
df["status"]=pd.cut(df["total"],bins=[0,250,400],labels=["fail","pass"])
# print(df)

#Adding top 5 student
st.text("Top 5 students :")
top_5_students=df.nlargest(5,"total")
# print(top_5_students[["name","total"]])
st.write(top_5_students)

col1,col2,col3=st.columns(3)
col1.metric("Top score",df["total"].max())
col1.metric("Class Average",round(df["average"].mean(),2))
col1.metric("Weak subject",subject_avg.idxmin())

st.progress(80)










