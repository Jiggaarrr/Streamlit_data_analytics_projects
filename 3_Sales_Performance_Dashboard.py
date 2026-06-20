import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.subheader("Sales_performance_Dashboard")
category=["electronics","clothing","household","furniture","food"]
region=["Maharashtra","Delhi","Kashmir","Karnataka","Tamil Nadu"]
products=[]

np.random.seed(42)
for i in range(1,51):
    units=np.random.randint(1,51)
    price=np.random.randint(100,2000)
    products.append([i,
                    f"product_name{i}",
                    np.random.choice(category),
                    units,
                    price,
                    units*price,
                    np.random.randint(2020,2026),
                    np.random.choice(region)
                    ])
    
df=pd.DataFrame(products,columns=["product_id","product_name","product_category","unit_sold","price_per_unit","revenue","sale_date","region"])

st.text("Data Overview:")
# print(df)
st.dataframe(df)


#Best Selling products

#Approach 1
top_5_products=df.nlargest(5,"revenue")
# print(top_5_products)

#Approch2
top_5_products=df["revenue"].sort_values(ascending=False).head(5)
# print(top_5_products) #This only give me particular column value in sorted way not whole row

#Approch3
st.text("Top 5 Best Selling Product :")
top_5_products=df.sort_values("revenue",ascending=False).head(5)
# print(top_5_products)
st.write(top_5_products)

#Best selling product

#Approach1

best_selling_product=df.loc[df["revenue"].idxmax()] # i get whole row
# print(best_selling_product)
st.write("Best Selling product :"," ",best_selling_product)

#Approach2
best_selling_product=df["revenue"].sort_values(ascending=False).head(1) #I get only that particular column value 
# print(best_selling_product)

#Approach3
best_selling_product=df.sort_values("revenue",ascending=False).head(1)
# print(best_selling_product)


#Data vizualization

#Unit sold by years

st.text("Unit Sold By Year Trend :")
product_sales=df.groupby("sale_date")["unit_sold"].mean()
fig,ax=plt.subplots()
product_sales.plot(
    kind="line",
    marker="o",
    ax=ax
)
# plt.show()
st.pyplot(fig)


#Revenue trend by years
st.text("Revenue Trend By Year Trend :")
revenue_trend=df.groupby("sale_date")["revenue"].mean()
fig,ax=plt.subplots()
revenue_trend.plot(
    kind="line",
    marker="o",
    ax=ax
)
# plt.show()
st.pyplot(fig)

#Top_5_Product(Bar chart)
st.text("Revenue By Category:")
top_5_df=df.groupby("product_category")["revenue"].sum().reset_index()
top_5_df=top_5_df.sort_values("revenue",ascending=False)
fig, ax = plt.subplots()
sns.barplot(data=top_5_df,x="product_category",y="revenue",ax=ax)
# plt.show()
st.pyplot(fig)


#Second TOP 5 PRODUCTS
st.text("Top 5 product by revenue")
top_5_products=df.nlargest(5,"revenue")
fig, ax = plt.subplots()
sns.barplot(data=top_5_products,x="product_name",y="revenue",ax=ax)
plt.xticks(rotation=90)
# plt.show()
st.pyplot(fig)


st.progress(80)


