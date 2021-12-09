import requests
import json

import pandas as pd
import csv
import os
from random import randint




a = ['steam-trading-cards', 'Steam Achievements', 'Singleplayer', 'None', 'hi']


for i in a:
    if 'Steam' in i:
        print('in steam')
    elif 'steam' in i:
        print('in Steam')
    elif 'Single' in i:
        print('in Single')
    else:
        print(i)