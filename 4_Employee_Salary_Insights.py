import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.subheader("Employee_Salary_Insights")
employees=[]
department=["Sales","Marketing","Hr","IT"]
job_role=["Intern","Fresher","Experienced"]

np.random.seed(42)
for i in range(1,51):
    role=np.random.choice(job_role)

    if role == "Intern":
        salary=np.random.randint(12000,25000)

    elif role == "Fresher":
        salary=np.random.randint(25000,60000)
    
    else:
        salary=np.random.randint(60000,150000)

    employees.append([
        i,
        f"Empolyee_name{i}",
        np.random.choice(department),
        role,
        salary
    ])

df=pd.DataFrame(employees,columns=["Employee_id","Employee_name","Department","Role","Salary"])
# print(df.head())
st.text("Data overview")
st.dataframe(df)


#FILTERING

#Salary greater than 50000
st.text("Salary Greater than 50k : ")
salary_greater_than_50k=df[(df["Salary"]>50000)]
# print(salary_greater_than_50k)
# print(f"There are {len(salary_greater_than_50k)} people who are getting salary more than 50k")
st.write(salary_greater_than_50k)
st.write(f"There are {len(salary_greater_than_50k)} people who are getting salary more than 50k")



#Department == "IT"
st.text("IT Department Employees :")
department_IT=df[df["Department"] == "IT"]
# print(department_IT)
# print(f"There are {len(department_IT)} people who are working in IT department")
st.write(department_IT)
st.write(f"There are {len(department_IT)} people who are working in IT department")



#"Job role" == "Experienced"
st.text("Experienced People In Company :")
job_role_exp=df[df["Role"]== "Experienced"]
# print(job_role_exp)
# print(f"There are {len(job_role_exp)} people who are Experienced !")
st.write(job_role_exp)
st.write(f"There are {len(job_role_exp)} people who are Experienced !")


selected_departments=st.multiselect(
    "Select Departments:",
    options=df["Department"].unique(),
    default=df["Department"].unique(),
)

selected_roles = st.multiselect(
    "Select Role:",
    options=df["Role"].unique(),
    default=df["Role"].unique(), # Default to all selected
)

filtered_df=df[(df["Department"].isin(selected_departments)) & (df["Role"].isin(selected_roles))]

#Groupby

#Department wise salary mean
st.text('Department wise salary  :')
dept_wise_sal=filtered_df.groupby("Department")["Salary"].mean()
# print(round(dept_wise_sal,2))
st.write(dept_wise_sal)

#Job role  wise sal mean
st.text("Job Role wise Salary :")
job_role_wise_sal=filtered_df.groupby("Role")["Salary"].mean()
# print(round(job_role_wise_sal,2))
st.write(job_role_wise_sal)


#Dept + role sal mean
st.text("Department Wise Job Roles Salary :")
dept_role_wise_sal=filtered_df.groupby(["Department","Role"])["Salary"].mean()
st.write(dept_role_wise_sal)
# print(dept_role_wise_sal)

#Visualization

#Box Plot
st.text("Box Plot - Salary vs Department :")
fig,ax=plt.subplots()
sns.boxplot(data=filtered_df,x="Department",y="Salary",ax=ax)
# plt.show()
st.pyplot(fig)



#Violin plot
st.text("Vilon plot - Role vs Salary :")
fig,ax=plt.subplots()
sns.violinplot(data=filtered_df,x="Role",y="Salary",ax=ax)
st.pyplot(fig)
# plt.show()


#Interactive Dashboard

st.write(filtered_df)

st.success("Dashboard Done")

