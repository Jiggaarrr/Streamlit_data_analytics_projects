import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header("Event_Registration_Dashboard")
attendees=[]
event_name=["Hackathon","AI Workshop","Webinar","Tech Fest"]
age_group=["18-25","26-35","36-50"]
gender=["Male","Female"]
registration_status=["Registered","Cancelled","Attended"]

np.random.seed(42)
for i in range(1,51):
    attendees.append([
        np.random.randint(1000,9999),          # Attendee_ID
        np.random.choice(event_name),          # Event
        np.random.choice(age_group),           # Age
        np.random.choice(gender),              # Gender
        np.random.choice(registration_status)  # Status
    ])


df=pd.DataFrame(
    attendees,
    columns=[
        "Attendee_ID",
        "Event_Name",
        "Age_Group",
        "Gender",
        "Registration_Status"
    ]
)

# print(df.info())
# print(df.head())
st.text("Data Overview :")
st.write(df)

# Filtering 

st.text("Interactive Dashboard :")
selected_event=st.multiselect(
    "Select Event :",
    options=df["Event_Name"].unique(),
    default=df["Event_Name"].unique()
)

selected_status=st.multiselect(
    "Select Registration Status :",
    options=df["Registration_Status"].unique(),
    default=df["Registration_Status"].unique()
)

selected_gender=st.multiselect(
    "Select Gender :",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

selected_age=st.multiselect(
    "Select Age Group :",
    options=df["Age_Group"].unique(),
    default=df["Age_Group"].unique()
)


filtered_df=df[
    (df["Event_Name"].isin(selected_event))
    &
    (df["Registration_Status"].isin(selected_status))
    &
    (df["Gender"].isin(selected_gender))
    &
    (df["Age_Group"].isin(selected_age))
]

st.write(filtered_df)

#Manual filter 
attended_df=df[df["Registration_Status"] == "Attended"]
# print(f"There are {len(attended_df)} people who have attended for this event.")


registered_df=df[df["Registration_Status"] == "Registered"]
# print(f"There are {len(registered_df)} people who have registered this event.")

# choice=input("Enter a specific event name :")
# filtered=df[df["Event_Name"] == choice]
# print(filtered)

#Groupby 

st.text("Event wise Registration :")
event_wise_registeration=filtered_df.groupby("Event_Name")["Attendee_ID"].count()
# print(event_wise_registeration)
st.write(event_wise_registeration)


st.text("Gender wise attendees :")
gender_wise_attendees=filtered_df.groupby("Gender")["Attendee_ID"].count()
# print(gender_wise_attendees)
st.write(gender_wise_attendees)


st.text("Age Group wise Attendees :")
age_group_wise_attendees=filtered_df.groupby("Age_Group")["Attendee_ID"].count()
# print(age_group_wise_attendees)
st.write(age_group_wise_attendees)


#Visualization

#1
st.text("Event wise Registration status :") 
fig,ax=plt.subplots(figsize=(10,6))
sns.countplot(data=filtered_df,x="Event_Name",hue="Registration_Status",ax=ax)
# plt.show()
st.write(fig)


#2
st.text("Gender Wise Attendee Demographics")
gender_count=df["Gender"].value_counts()
fig,ax=plt.subplots()
ax.pie(
    gender_count,
    labels=gender_count.index,
    autopct="%1.1f%%",
)
ax.set_title("Attendee Demographics")
st.write(fig)

st.success("Dashboard Done.")