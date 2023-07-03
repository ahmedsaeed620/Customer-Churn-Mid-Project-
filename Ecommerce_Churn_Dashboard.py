import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

st.set_page_config(layout= 'wide')
data = pd.read_csv('Ecommerce Churn_clean.csv')
 
row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title('Customer Churn  Dataset Analysis')
with row0_2:
    st.text("")
    st.subheader('Streamlit App by [Ahmed ELSaied](https://www.linkedin.com/in/ahmed-el-saied-75ab56217/)')
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("Customer churn problem refers to the issue of losing customers who were previously active on an online store.Churn occurs when customers stop using a service or buying from a company, and it is a common problem in e-commerce businesses. The churn rate is an important metric for e-commerce businesses because it can significantly impact their revenue and profitability. High churn rates can indicate issues with customer service, product quality, or pricing. To combat churn, e-commerce businesses often implement retention strategies, such as targeted marketing campaigns, loyalty programs, and personalized recommendations, to keep customers engaged and satisfied .")
    st.markdown("You can find the source code in the [Ecommerce of Customer Churn GitHub Repository](https://github.com/ahmedsaeed620/Ecommerce-of-Customer-Churn-Mid-Project-.git)")

### Understanding Data ###
row3_spacer1, row3_1, row3_spacer2 = st.columns((.2, 7.1, .2))
with row3_1:
    st.markdown("")
    see_data = st.expander('You can click here to see the raw data first ')
    with see_data:
        st.dataframe(data=data.reset_index(drop=True))
    st.text('')

### Univariate Categorical variables ###
row4_spacer1, row4_1, row4_spacer2 = st.columns((.2, 7.1, .2))
with row4_1:
    st.subheader('Analysis Univariate For Categorical Variables ')
row5_spacer1, row5_1, row5_spacer2, row5_2, row5_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row5_1:
    st.markdown('Any value in Every Column of E-Commerce Is More in Demand?')    
    option = st.selectbox('selsect an option' , ['PreferredLoginDevice','PreferredPaymentMode','Gender','PreferedOrderCat','MaritalStatus'],key ="option_sec1")   
with row5_2:
    fig = px.bar(y= data[option].value_counts()  ,  text_auto='0.3s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)

### Univariate Numerical Variables ###
row6_spacer1, row6_1, row6_spacer2 = st.columns((.2, 7.1, .2))
with row6_1:
    st.subheader('Analysis Univariate Numerical Variables')
row7_spacer1, row7_1, row7_spacer2, row7_2, row7_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row7_1:
    st.markdown('In Which Range Numaric Value Lies, What Is Distribution Look Like?')    
    option1 = st.selectbox('selsect an option' , ['Tenure', 'CityTier', 'WarehouseToHome', 'HourSpendOnApp','SatisfactionScore','NumberOfAddress','Complain' ,'OrderAmountHikeFromlastYear','CouponUsed','OrderCount','DaySinceLastOrder','CashbackAmount'],key = "tap_sec2")   
with row7_2:
    fig = px.histogram(data_frame= data , x = option1 )
    st.plotly_chart(fig)


### Target ###
row8_spacer1, row8_1, row8_spacer2 = st.columns((.2, 7.1, .2))
with row8_1:
    st.subheader('Target (Churn Value)')
row9_spacer1, row9_1, row9_spacer2, row9_2, row9_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row9_1:
    st.markdown("We can see from the pie chart, about 17% of customers from our data set end up flopping, I'll take that value for what it is and won't read too much into it yet. Since this is our target variable, we will be using Churn as an element in most of our EDA variants")    
with row9_2:
    fig = px.pie(data_frame=data , names =data.groupby('Churn')['CustomerID'].count().index
    , values = data.groupby('Churn')['CustomerID'].count().values)
    st.plotly_chart(fig)

### Analysis Bivariate Categorical Variables ###
row9_spacer1, row9_1, row9_spacer2 = st.columns((.2, 7.1, .2))
with row9_1:
    st.subheader('Analysis Bivariate  Categorical Variables')
row10_spacer1, row10_1, row10_spacer2, row10_2, row10_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row10_1:
    st.markdown('Is there a significant relationship between a (Categorical variables)and their likelihood to churn?')    
    option = st.selectbox('selsect an option' , ['PreferredLoginDevice','PreferredPaymentMode','Gender','PreferedOrderCat','MaritalStatus'],key = "tap_sec4")
with row10_2:
    fig = px.bar(data_frame=data.groupby([option , 'Churn']).count()
    ['CustomerID'].reset_index() 
    , x = option , y = 'CustomerID' , color='Churn' ,  text_auto='0.2s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)



### Analysis Bivariate Numerical Variables ###
row10_spacer1, row10_1, row10_spacer2 = st.columns((.2, 7.1, .2))
with row10_1:
    st.subheader('Analysis Bivariate  Numerical Variables')
row11_spacer1, row11_1, row11_spacer2, row11_2, row11_spacer3  = st.columns((.2, 2.3, .4, 4.4, .2))
with row11_1:
    st.markdown('Does the (Numerical Values) have a significant impact on their likelihood to churn?')    
    option1 = st.selectbox('selsect an option' , ['Tenure', 'CityTier', 'WarehouseToHome', 'HourSpendOnApp','SatisfactionScore','NumberOfAddress','Complain' ,'OrderAmountHikeFromlastYear','CouponUsed','OrderCount','DaySinceLastOrder'],key = "tap_sec5")   
with row11_2:
    fig = px.bar(data_frame=data.groupby([option1 , 'Churn']).count()
    ['CustomerID'].reset_index() 
    , x = option1 , y = 'CustomerID' , color='Churn' ,  text_auto='0.2s')
    fig.update_traces(textfont_size = 12 , textposition = 'outside')
    st.plotly_chart(fig)