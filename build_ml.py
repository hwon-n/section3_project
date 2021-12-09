# LightGBM 찾아보기

import os
import pandas as pd
from sklearn.model_selection import train_test_split


CSV_FILENAME = 'Games.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)


Games = pd.read_csv(CSV_FILEPATH)

# train, val, test셋 나누기
train, test = train_test_split(Games, test_size = 0.2, random_state = 42)
train, val = train_test_split(train, test_size = 0.2, random_state=42)


# Tag 열 전처리 위해서 55개 이상의 Tag 목록 만들기
over_50_Tag = train['Tag'].value_counts() >= 50
over_50 = over_50_Tag.to_frame()
true_over = over_50.loc[(over_50.Tag == True)]
true_over = true_over.reset_index()
condition = true_over['index'].values.tolist()

# Tag_list = ['Singleplayer', 'Full controller support', 'RPG', '2D', 'exclusive', 'Partial Controller Support', 'Co-op', 'Horror', 'Multiplayer']
Tag_list = condition[:9]

# 데이터 전처리 위한 list
platform_list = ['Commodore / Amiga', 'SEGA', 'Web', 'Neo Geo']
Genre_list = ['Racing', 'Arcade', 'Sports', 'Platformer', 'Massively Multiplayer', 'Family', 'Fighting', 'no genre', 'Board Games', 'Card', 'Educational']

def platform(p):
    if p == 'iOS' or p == 'Android':
        return 'Mobile'
    elif p in platform_list:
        return 'other'
    elif p in ['Nintendo', 'PlayStation', 'Xbox']:
        return 'Video/Console'
    elif p == 'Apple Macintosh':
        return p
    else:
        return 'PC'


def engineer(df):
    df.Tag = df.Tag.apply(lambda x: x if x in Tag_list else 'other')
    df.Platform = df.Platform.apply(platform)
    df.Genres = df.Genres.apply(lambda x: 'other' if x in Genre_list else x)
    df = df.reset_index(drop=True)

    return df

train = engineer(train)
val = engineer(val)
test = engineer(test)

