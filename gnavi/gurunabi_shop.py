import json
import urllib.request

def get_rest(areacode_s, offset, hit_per_page):
  url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'    
  params = {
          'keyid':'1adeadfea9709941bac87f77415887b7',
  #        'category_l':'RSFST18000',  # カフェ・スイーツ
          'category_s':'RSFST18001,RSFST18002,RSFST18008,RSFST18014',  
          'areacode_s':areacode_s,  # 自由が丘
          'hit_per_page':hit_per_page,
          'offset':offset,
          }
  url = url + '?' + urllib.parse.urlencode(params, safe=',')
  req = urllib.request.Request(url)
  with urllib.request.urlopen(req) as res:
      return json.load(res)
# get total hit count
areacode_s = 'AREAS2164' # 自由が丘
offset = 1
hit_per_page = 10
result_api = get_rest(areacode_s, offset, hit_per_page)
total_hit_count = result_api['total_hit_count']
print(total_hit_count)

# get shop list for area
loop_num = int(total_hit_count/100) + 1
hit_per_page = 100
ls_shop = []
for i in range(loop_num):
  print(i)
  offset = 1 + i * hit_per_page
  dct = get_rest(areacode_s, offset, hit_per_page)
  ls_shop = ls_shop + dct['rest']
print(len(ls_shop))

# get station set
set_station = set()
for shop in ls_shop:
  set_station = set_station | {shop['access']['station']}

# count for station 
dct_station = {st:i for i, st in enumerate(set_station)}
ls_st_cnt = [0] * len(dct_station) 
for shop in ls_shop:
  ls_st_cnt[dct_station[shop['access']['station']]] += 1
for k, v in dct_station.items():
  print(k, ls_st_cnt[v])
'''
4
等々力駅 6
田園調布駅 2
奥沢駅 12
自由が丘駅 21
大岡山駅 12
北千束駅 2
洗足駅 1
尾山台駅 13
緑が丘（東京都）駅 3
九品仏駅 12
都立大学駅 18
駒沢大学駅 2
自由が丘（東京都）駅 49
# 表記揺れあり
'''