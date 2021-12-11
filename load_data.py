from flask_app.private import API_KEY
import requests
import json
import pandas as pd
import os
from random import randint


BASE_URL = 'https://api.rawg.io/api/games?key='
CSV_FILENAME = 'Games.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)


Game_info = pd.DataFrame(columns = ['Added', 'Playtime', 'Platform', 'Genres', 'Stores', 'Tag', 'Esrb_rating'])


for i in range(1, 401):
    # api를 통해서 데이터 불러오기
    raw_data = requests.get(f'{BASE_URL}{API_KEY}&page={i}')
    parsed_data = json.loads(raw_data.text)
    datas = parsed_data['results']
    
    # 필요한 데이터만 가져오기
    for x in range(0, len(datas)):
        da_list = []

        # Added, Playtime
        da_list.append(str(datas[x]['added']))
        da_list.append(str(datas[x]['playtime']))
        
        # Platform 수 (parent_platform의 수)
        try:
          da_list.append(len(datas[x]['parent_platforms']))
        except IndexError:
          da_list.append(0)
        
        # 등록된 Genres 중 하나를 랜덤으로 가져오기
        try:
            try:
              gen_rand = randint(0, len(datas[x]['genres'])-1)
            except ValueError:
              gen_rand = 0
            da_list.append(datas[x]['genres'][gen_rand]['name'])
        except IndexError:
            da_list.append('no genre')
        
        # Stores
        try:
          da_list.append(len(datas[x]['stores']))
        except ValueError:
          da_list.append(0)

        # Tag
        try:
            i = 0
            if datas[x]['tags'][0]['name'] == 'Singleplayer':
              da_list.append(datas[x]['tags'][1]['name'])
            else:
              da_list.append(datas[x]['tags'][0]['name'])
        except IndexError:
            da_list.append('no tag')
        
        #Esrb_rating
        try:
            da_list.append(datas[10]['esrb_rating']['name'])
        except TypeError:
            da_list.append('No age info')
            
        # df에 데이터 삽입
        Game_info = Game_info.append(pd.Series(da_list, index=Game_info.columns), ignore_index=True)

Game_info.to_csv(CSV_FILEPATH, sep=',', index=False)

print('CSV 생성 완료!')
