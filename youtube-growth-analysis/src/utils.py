def plot_title_length_vs_views(df):
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    df['title_length'] = df['video_title'].apply(len)
    sns.scatterplot(data=df, x='views', y='likes',)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['title_length'], df['views'], alpha=0.5)
    plt.title('Title Length vs Views')
    plt.xlabel('Title Length (characters)')
    plt.ylabel('Number of Views')
    plt.grid()
    plt.show()
    plt.close()

def views_vs_likes(df):
   import matplotlib.pyplot as plt
   import seaborn as sns
   plt.figure(figsize=(10, 6))
   sns.scatterplot(data=df,x="views",y="likes")
   plt.xlabel('Views')
   plt.ylabel('Likes')
   plt.title('Views vs Likes')
   plt.show()