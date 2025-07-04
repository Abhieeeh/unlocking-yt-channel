
import pandas as pd
import numpy as np
from feature_engineering import is_viral
from feature_engineering import create_features
import utils


data_path= r'C:\Users\Abhishek k\codes learning\yt secrets\youtube-growth-analysis\data\sample_videos.csv'
df = pd.read_csv(data_path)

def load_data(data_path):   
   
    try:        
        
        df= pd.read_csv(data_path)
        print("loaded sucessfully")
        return df
    except Exception as e:
        print("Error loading data: {e}")
        return None     
    
load_data(data_path)
df = pd.read_csv(data_path)
df['is_viral'] = is_viral(df, threshold=1_000_000)
print(df[['video_title','views', 'is_viral']])

create_features(df)


utils.plot_title_length_vs_views(df)

utils.views_vs_likes(df)






"""
    Load video metadata from a CSV file into a Pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file containing video metadata.

    Returns:
    DataFrame: A Pandas DataFrame containing the video metadata.
"""
