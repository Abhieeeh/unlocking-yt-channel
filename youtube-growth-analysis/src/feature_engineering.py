import pandas as pd

 

def create_features(df):
    # Load the CSV file into a DataFrame
   
    """
    Create new features for the YouTube video dataset.

    Parameters:
    df (pd.DataFrame): DataFrame containing video metadata.

    Returns:
    pd.DataFrame: DataFrame with new features added.
    """
    # Feature: Title Length
    print()
    print("CALCULATING TITLE LENGTH")

    df['title_length'] = df['video_title'].astype(str).apply(len)
    print(df[['video_title','title_length']])
    

    # Feature: Engagement Ratio (avoid division by zero)
    print()
    print("CALCULATING ENGAGEMENT RATIO")
    df['engagement_ratio'] = (df['likes'] + df['comments']) / df['views'].replace(0, 1)
    print(df[['video_title','engagement_ratio']])

    # Feature: Dislike Ratio (avoid division by zero)
    print()
    print("CALCULATING DISLIKE RATIO")
    df['dislike_ratio'] = df['dislikes'] / (df['likes'] + df['dislikes']).replace(0, 1)
    print(df[['video_title','dislike_ratio']])

    return df




def is_viral(df, threshold=1_000_000):
    """
    Determine if each video is viral based on views.

    Parameters:
    df (pd.DataFrame): DataFrame containing video metadata.
    threshold (int): The view count threshold to define virality.

    Returns:
    pd.Series: Series indicating whether each video is viral.
    """
    return df['views'] > threshold
    




