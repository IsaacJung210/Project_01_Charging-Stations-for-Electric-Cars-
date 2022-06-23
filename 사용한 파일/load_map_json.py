import json
import pandas as pd


def load_json(locations):
    df = pd.read_json('/home/kang/www/webapp/intro/Ecar_info.json')
    copy = df[df['addr'].str.contains(locations)]
    print(copy)


###
# 데이터프레임을 받아서 
# 딕셔너리 형태의 콘텍스트로 반환하는 함수    







