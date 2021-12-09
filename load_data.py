from private import API_KEY
import requests
import json
import pandas as pd
import os
from random import randint

from flask_app.test import CSV_FILEPATH


BASE_URL = 'https://api.rawg.io/api/games?key='
CSV_FILENAME = 'Games.csv'
CSV_FILEPATH = os.path.join(os.getcwd(), CSV_FILENAME)


Game_info = pd.DataFrame(
    columns=['Added', 'Playtime', 'Platform', 'Genres', 'Tag', 'Esrb_rating'])


for i in range(1, 301):
    # api를 통해서 데이터 불러오기
    raw_data = requests.get(f'{BASE_URL}{API_KEY}&page={i}')
    parsed_data = json.loads(raw_data.text)
    datas = parsed_data['results']

    # 필요한 데이터만 가져오기
for i in range(1, 301):
    # api를 통해서 데이터 불러오기
    raw_data = requests.get(f'{BASE_URL}{API_KEY}&page={i}')
    parsed_data = json.loads(raw_data.text)
    datas = parsed_data['results']

    # 필요한 데이터만 가져오기
    for x in range(0, len(datas)):
        da_list = []
        da_list.append(str(datas[x]['added']))
        da_list.append(str(datas[x]['playtime']))

        # 등록된 parent_platform 중 한개를 랜덤으로 가져오기 => 첫번째것을 가져오면 90%가 Action이 나옴
        try:
            try:
                plat_rand = randint(0, len(datas[x]['parent_platforms'])-1)
            except ValueError:
                plat_rand = 0
            da_list.append(datas[x]['parent_platforms']
                           [plat_rand]['platform']['name'])
        except IndexError:
            da_list.append('no platform')

        # 등록된 genres 중 하나를 랜덤으로 가져오기
        try:
            try:
                gen_rand = randint(0, len(datas[x]['genres'])-1)
            except ValueError:
                gen_rand = 0
            da_list.append(datas[x]['genres'][gen_rand]['name'])
        except IndexError:
            da_list.append('no genre')

        try:
            try:
                tag_rand = randint(0, len(datas[x]['tags'])-1)
                if 'Steam' in datas[x]['tags'][tag_rand]['name']:
                    tag_rand = randint(0, len(datas[x]['tags'])-1)
                elif 'steam' in datas[x]['tags'][tag_rand]['name']:
                    tag_rand = randint(0, len(datas[x]['tags'])-1)
                elif 'Singleplayer' in datas[x]['tags'][tag_rand]['name']:
                    tag_rand = randint(0, len(datas[x]['tags'])-1)
                elif 'Multiplayer' in datas[x]['tags'][tag_rand]['name']:
                    tag_rand = randint(0, len(datas[x]['tags'])-1)
                da_list.append(datas[x]['tags'][tag_rand]['name'])
            except ValueError:
                da_list.append(datas[x]['tags'][0]['name'])
        except IndexError:
            da_list.append('no tag')

        try:
            da_list.append(datas[10]['esrb_rating']['name'])
        except TypeError:
            da_list.append('No age info')

        # df에 데이터 삽입
        Game_info = Game_info.append(
            pd.Series(da_list, index=Game_info.columns), ignore_index=True)


Game_info.to_csv(CSV_FILEPATH, sep=',', index=False)

print('CSV 생성 완료!')
