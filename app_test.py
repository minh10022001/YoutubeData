import streamlit as st
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# import plotly.express as px
import pickle as pk
from data import get_video_info, youtube

st.title("Predict view M/V Kpop")

menu=["View MV  Prediction","About","Visual"]
choices=st.sidebar.selectbox("Menu Bar",menu)

if choices=='View MV  Prediction':
    st.subheader("View MV Prediction")
    url = st.text_input("Enter url link teaser")
    view = st.button('View')
    if view:
        id_video = url.split('=')[1]
        st.text(id_video)
        list_check_snippet_video = ['channelId', 'channelTitle', 'title', 'publishedAt','description','thumbnails','tags','categoryId'] 
        list_check_statistics_video = ['viewCount', 'likeCount','commentCount']
        video = get_video_info(youtube, id_video, list_check_snippet_video, list_check_statistics_video)
        # video_channelId = st.number_input("the number of subcribers channel ",value= int(video['video_channelSubscriber']))
        video_channelTitle = st.text_input("title channel ",value= video['video_channelTitle'])
        video_channelSubscriber= st.number_input("the number of subcribers channel ",value= int(video['video_channelSubscriber']))
        video_id = st.text_input("video id Teaser ",value= video['video_id'])
        video_title = st.text_input("video title Teaser ",value= video['video_title'])
        video_publishedAt = st.text_input("published date Teaser ",value= video['video_publishedAt']),
        video_description = st.text_input("description Teaser ",value= video['video_description'])
        video_tags = st.text_input("Tag Teaser ",value= video['video_tags'])
        # video_categoryId = st.number_input("the number of subcribers channel ",value= int(video['video_categoryId']))
        video_viewCount =  st.number_input("Number of views Teaser",value= int(video['video_viewCount']))
        video_likeCount = st.number_input("Number of likes Teaser",value= int(video['video_likeCount']))
        video_commentCount = st.number_input("Number of comments Teaser",value= int(video['video_commentCount']))
        video_duration = st.text_input(" duration Teaser ",value= video['video_duration'])
    
   
    # No_tag = st.number_input("Enter number tag of MV Teaser",value=0,format='%d')
    # Len_description = st.number_input("Enter length description of MV Teaser",value=0,format='%d')
    # Len_titile = st.number_input("Enter length tilte of MV Teaser",value=0,format='%d')
        HourTeaerWithMV = st.number_input("Enter number of hours to publish MV offical affer publish Mv teaser",value=0.0,format='%f')
        HourPublisedMV = st.number_input("Enter number of hours  affer  Mv teaser is published",value=0.0,format='%f')
    submit = st.button('Predict')
    if submit:
        st.success("Prediction Done")
        # value=[SubcriberChannel, TeaserViewCount, TeaserLikeCount, TeaserCommentCount , No_tag, Len_description,  Len_titile , HourTeaerWithMV, HourPublisedMV]
        # df=pd.DataFrame(value).transpose()
        # st.dataframe(df)
        # model=pk.load(open('rfrmodel.pkl','rb'))
        # scaler=pk.load(open('scale.pkl','rb'))

        # scaler.transform(df)
        # ans=int(model.predict(df))
        # st.subheader("The view prediction of MV is {} views".format(ans))
        # save_data(value,ans)