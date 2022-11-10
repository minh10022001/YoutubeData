import streamlit as st
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# import plotly.express as px
import pickle as pk
from data import get_video_info, youtube
import re
from app_show_plot import Plot
st.title("Predict view M/V Kpop")

menu=["View MV  Prediction","About","Visual"]
choices=st.sidebar.selectbox("Menu Bar",menu)

if choices=='View MV  Prediction':
    st.subheader("View MV Prediction")
    url = st.text_input("Enter url link teaser")
    # video_channelSubscriber, video_viewCount, video_likeCount, video_commentCount , no_tag, len_description,  len_titile , hour_teaser_with_mv, hour_publised_mv = 0,0,0,0,0,0,0,0,0
    info = ['video_channelSubscriber', 'video_viewCount', 'video_likeCount', 'video_commentCount' , 'no_tag', 'len_description',  'len_titile' , 'hour_teaser_with_mv', 'hour_publised_mv']
    hour_teaser_with_mv = st.number_input("Enter number of hours to publish MV offical affer publish Mv teaser",value=0.0,format='%f')
    hour_publised_mv = st.number_input("Enter number of hours  affer  Mv teaser is published",value=0.0,format='%f')
    view = st.button('View')
    if view:
        reg = re.search(r'(?<=v=)[^&]+', url)
        id_video = reg.group(0)
        # st.text(id_video)
        list_check_snippet_video = ['channelId', 'channelTitle', 'title', 'publishedAt','description','thumbnails','tags','categoryId'] 
        list_check_statistics_video = ['viewCount', 'likeCount','commentCount']
        video = get_video_info(youtube, id_video, list_check_snippet_video, list_check_statistics_video)
        # video_channelId = st.number_input("the number of subcribers channel ",value= int(video['video_channelSubscriber']))
        video_channelTitle = st.text_input("title channel ",value= video['video_channelTitle'])
        video_channelSubscriber= st.number_input("the number of subcribers channel ",value= int(video['video_channelSubscriber']))
        # st.session_state['video_channelSubscriber'] = video_channelSubscriber
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
        # for item in info:
        #     st.session_state[item] = item
        print('--------------------------')
        print(video['video_tags'])
        if video['video_tags'] is np.nan :
            no_tag = 0
        else: no_tag = len(video['video_tags'])
        print(no_tag)
        len_description = len(video_description)
        len_titile = len(video_title)
    # submit = st.button('Predict')
    # if submit:
        # st.success("Prediction Done")
        value=[video_channelSubscriber, video_viewCount, video_likeCount, video_commentCount , no_tag, len_description,  len_titile , hour_teaser_with_mv, hour_publised_mv]
        # value = [132000, 1228718, 15693, 1047, 19, 616, 40, 1.0, 2.0]
        print(value)
        df=pd.DataFrame(value).transpose()
        print(df)
        st.dataframe(df)
        with open("rfrmodel.pkl", "rb") as f:
            model = pk.load(f)
        with open("scale.pkl", "rb") as f:
            scaler = pk.load(f)

        a = scaler.transform(df)
        ans=int(model.predict(a))
        st.subheader("The view prediction of MV is {} views".format(ans))

if choices=='Visual':
    plott = Plot()
    visual_menu=["Subcriber of each channel","Time publish teaser and MV","Top video","Distribution chart"]
    visual_choices=st.selectbox("Select Chart To View",visual_menu)
    st.write('You selected:', visual_choices)
    if(visual_choices=='Subcriber of each channel'):
        chart = plott.show_plot_subcriber()
        st.pyplot(chart)
    if(visual_choices=='Time publish teaser and MV'):
        chart = plott.show_time_publish()
        st.pyplot(chart)
    if(visual_choices=='Top video'):
        chart = plott.show_top_video()
        st.pyplot(chart)
    if(visual_choices=='Distribution chart'):
        chart = plott.show_distribution()
        st.pyplot(chart)
    