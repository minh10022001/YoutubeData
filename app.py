import streamlit as st
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# import plotly.express as px
import pickle as pk

st.title("Predict view M/V Kpop")

menu=["View MV  Prediction","About","Visual"]
choices=st.sidebar.selectbox("Menu Bar",menu)

if choices=='View MV  Prediction':
    st.subheader("View MV Prediction")
    SubcriberChannel= st.number_input("Enter the number of subcribers channel ",value=0 ,min_value=0,format='%d')
    TeaserViewCount=st.number_input("Enter views of MV Teaser",value=0,format='%d')
    TeaserLikeCount=st.number_input("Enter likes of MV Teaser",value=0,format='%d')
    TeaserCommentCount=st.number_input("Enter number comments of MV Teaser",value=0,format='%d')
    No_tag = st.number_input("Enter number tag of MV Teaser",value=0,format='%d')
    Len_description = st.number_input("Enter length description of MV Teaser",value=0,format='%d')
    Len_titile = st.number_input("Enter length tilte of MV Teaser",value=0,format='%d')
    HourTeaerWithMV = st.number_input("Enter number of hours to publish MV offical affer publish Mv teaser",value=0.0,format='%f')
    HourPublisedMV = st.number_input("Enter number of hours  affer  Mv teaser is published",value=0.0,format='%f')
    submit = st.button('Predict')
    if submit:
        st.success("Prediction Done")
        value=[SubcriberChannel, TeaserViewCount, TeaserLikeCount, TeaserCommentCount , No_tag, Len_description,  Len_titile , HourTeaerWithMV, HourPublisedMV]
        df=pd.DataFrame(value).transpose()
        st.dataframe(df)
        model=pk.load(open('rfrmodel.pkl','rb'))
        scaler=pk.load(open('scale.pkl','rb'))

        scaler.transform(df)
        ans=int(model.predict(df))
        st.subheader("The view prediction of MV is {} views".format(ans))
        # save_data(value,ans)