import requests
import json

# 大カテゴリ ---------------------------
url = 'https://api.gnavi.co.jp/master/CategoryLargeSearchAPI/v3/'
params = {
        'keyid':'1adeadfea9709941bac87f77415887b7',
        'lang':'ja',
        }    
result_api = requests.get(url, params)
result_api = result_api.json()
'''
result_api...
{'@attributes': {'api_version': 'v3'},
 'category_l': [{'category_l_code': 'RSFST09000', 'category_l_name': '居酒屋'},
  {'category_l_code': 'RSFST02000', 'category_l_name': '日本料理・郷土料理'},
  ...
  {'category_l_code': 'RSFST18000', 'category_l_name': 'カフェ・スイーツ'},
'''
# コーヒーがありそうなのは、'category_l_code': 'RSFST18000
# --------------------------------------

# 小カテゴリ ---------------------------
url = 'https://api.gnavi.co.jp/master/CategorySmallSearchAPI/v3/'
params = {
        'keyid':'1adeadfea9709941bac87f77415887b7',
        'lang':'ja',
        }    
result_api = requests.get(url, params)
result_api = result_api.json()
'''
  {'category_l_code': 'RSFST03000',
   'category_s_code': 'RSFST03014',
   'category_s_name': '海鮮丼'},
  {'category_l_code': 'RSFST03000',
   'category_s_code': 'RSFST03003',
   'category_s_name': '刺身・海鮮料理'},
  {'category_l_code': 'RSFST03000',
'''
#result_api.keys()  # dict_keys(['@attributes', 'category_s'])
for a in result_api['category_s']:
    if a['category_l_code']=='RSFST18000':
        print(a['category_s_name'], a['category_s_code'])
'''
カフェ RSFST18001
喫茶店・軽食 RSFST18002
クレープ RSFST18015
パフェ RSFST18016
甘味処 RSFST18003
フルーツパーラー RSFST18004
ケーキ屋・スイーツ RSFST18005
アイスクリーム RSFST18006
パン屋・サンドイッチ RSFST18007
ハンバーガー RSFST06011
コーヒー RSFST18008
紅茶 RSFST18009
日本茶 RSFST18010
中国茶 RSFST18011
ハーブティ RSFST18012
ジュース RSFST18013
カフェ・スイーツ その他 RSFST18014
'''
# コーヒーがありそうなのは
# カフェ RSFST18001
# 喫茶店・軽食 RSFST18002
# コーヒー RSFST18008
# カフェ・スイーツ その他 RSFST18014
# --------------------------------------