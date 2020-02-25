# ぐるなびレストラン検索APIで用いるエリアコード取得
# ぐるなびエリアsマスタ https://api.gnavi.co.jp/api/manual/areasmaster/

import requests
import json

url = 'https://api.gnavi.co.jp/master/GAreaSmallSearchAPI/v3/'
keyid = '1adeadfea9709941bac87f77415887b7'
lang='ja'

params = {}
params['keyid'] = keyid
params['lang'] = lang

result_api = requests.get(url, params)
result_api = result_api.json()

'''
  {'areacode_s': 'AREAS7806',
   'areaname_s': '伊予・砥部',
   'garea_large': {'areacode_l': 'AREAL7803', 'areaname_l': '伊予・砥部'},
   'garea_middle': {'areacode_m': 'AREAM7803', 'areaname_m': '伊予・砥部'},
   'pref': {'pref_code': 'PREF38', 'pref_name': '愛媛県'}},
'''
# エリアコードsを取得（東京都のみ）
areacode_s_list = []
cnt = 0
for a in result_api['garea_small']:
    if a['pref']['pref_name']=='東京都':
        print(cnt, a['areaname_s'])
        areacode_s_list.append(a['areacode_s'])
        cnt +=1 
'''
0 銀座（和光・マロニエゲート銀座方面）
1 銀座（ギンザシックス・銀座コア方面）
2 新橋
3 汐留
4 赤坂
5 永田町
6 虎ノ門
7 浜松町・大門
8 芝浦
9 芝公園・東京タワー周辺
10 田町・三田
'''
