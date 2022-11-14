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
        df_view = self.df[['video_title_mv_official','video_viewCount_mv_official','video_duration_mv_official','video_channelSubscriber','video_viewCount']]
        df_view = df_view.sort_values(by='video_viewCount_mv_official', ascending=False).drop_duplicates().head(5)    
        sns.set(style="whitegrid")
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        ax = sns.barplot(x="video_title_mv_official", y="video_viewCount_mv_official", data=df_view)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
        return plt
    
    def show_top_video_length(self):
        df_view = self.df[['video_title_mv_official','video_viewCount_mv_official','video_duration_mv_official','video_channelSubscriber','video_viewCount']]        
        sns.set(style="whitegrid")
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        ax = sns.barplot(x="video_title_mv_official", y="video_duration_mv_official", data=df_view)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
        ax.bar_label(ax.containers[0])
        return plt
    
    def show_scatter_view_count(self):
        sns.set(style="whitegrid")
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        x = self.df['video_viewCount_mv_official']
        y = self.df['video_viewCount']
        plt.scatter(x, y)
        # ax.set_xlabel('MV view count')
        # ax.set_ylabel('Trailer view count')
        plt.xlabel('MV view count')
        plt.ylabel('Trailer view count')
        return plt
        
    def show_distribution(self):
        features = ['video_viewCount','video_likeCount','video_commentCount']
        plt.figure(figsize=(15, 7))
        for i in range(0, len(features)):
            plt.subplot(1, 8, i+1)
            sns.boxplot(y=self.df[features[i]],color='green',orient='v')
            # plt.tight_layout()
        return plt