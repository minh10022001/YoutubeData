import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

class Plot():
    df = pd.DataFrame()
    def __init__(self):
        self.df = pd.read_csv('data_youtube.csv', header=0)
    def show_plot_subcriber(self):
        df_channel = pd.DataFrame(self.df['video_channelTitle'].unique(), columns = ['channel'])
        df_channel['subcribers']=0
        for x in df_channel['channel']:
            df_channel.loc[df_channel['channel']==x, 'subcribers'] = self.df.loc[self.df['video_channelTitle']==x, 'video_channelSubscriber'].max()        
        sns.set(style="whitegrid")
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        ax = sns.barplot(x="channel", y="subcribers", data=df_channel.sort_values(by='subcribers', ascending=False))
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
        # plt.tight_layout()
        # plt.show()
        # st.pyplot(plt)
        return plt

    def show_time_publish(self):
        df_time = pd.DataFrame()
        df_time['trailer_time'] = pd.to_datetime(self.df['video_publishedAt']).dt.hour
        df_time['mv_time'] = pd.to_datetime(self.df['video_publishedAt_mv_official']).dt.hour
        df_trailer_time = pd.DataFrame(df_time.groupby(['trailer_time'], as_index=False)['trailer_time'].agg({'trailer_videos':'count'}))
        df_mv_time = pd.DataFrame(df_time.groupby(['mv_time'], as_index=False)['mv_time'].agg({'mv_videos':'count'}))
        df_time_merge = pd.merge(df_trailer_time, df_mv_time, left_on='trailer_time', right_on='mv_time')
        df_time_merge.drop(['mv_time'], axis=1, inplace=True)
        df_time_merge.rename(columns={'trailer_time':'time'}, inplace=True)
        sns.set(style="whitegrid")
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        ax = sns.lineplot(data=pd.melt(df_time_merge, id_vars=['time'], value_vars=['trailer_videos', 'mv_videos']), x='time', y='value', hue='variable')   
        ax.set_xticks(np.arange(0, 24, 1))
        return plt
    
    def show_top_video(self):
        df_view = self.df[['video_title','video_viewCount','video_likeCount','video_commentCount']]
        df_view = df_view.sort_values(by='video_viewCount', ascending=False).head(5)       
        sns.set(style="whitegrid")
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        ax = sns.barplot(x="video_title", y="video_viewCount", data=df_view)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
        return plt
    
    def show_distribution(self):
        features = ['video_viewCount','video_likeCount','video_commentCount']
        plt.figure(figsize=(15, 7))
        for i in range(0, len(features)):
            plt.subplot(1, 8, i+1)
            sns.boxplot(y=self.df[features[i]],color='green',orient='v')
            # plt.tight_layout()
        return plt