# 日経電子版の決算発表スケジュールからスクレイピング
import datetime
from dateutil.relativedelta import relativedelta
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import os

output_dir = '../../data/kessan/out/'

def get_soup(url):
    # HTMLテキスト取得
    time.sleep(1)
    with urllib.request.urlopen(url) as f:
        html_doc = f.read().decode('utf-8')
    return BeautifulSoup(html_doc, 'html.parser')
def get_schdule(soup):
    '''
    return df
    '''
    resultSet = soup.findAll('table', {'summary':'決算発表スケジュール表'})
    return pd.read_html(str(resultSet[0]))[0]

def main():
    # URL生成
    # 共通
    url_base = 'https://www.nikkei.com/markets/kigyo/money-schedule/kessan/'
    params = {
            'ResultFlag':'1',
            'SearchDate2':'選択なし',
            }

    # 今月と来月を指定する文字列を生成
    dt = datetime.datetime.now()  # 現在日時
    fmt = '%Y年%m'
    str_this_month = dt.strftime(fmt)
    str_next_month = (dt + relativedelta(months=1)).strftime(fmt)

    # 今月分のURL
    params['SearchDate1'] = str_this_month
    url_this_month = url_base + '?' + urllib.parse.urlencode(params)

    # 来月分のURL
    params['SearchDate1'] = str_next_month
    url_next_month = url_base + '?' + urllib.parse.urlencode(params)
    df = pd.DataFrame()

    for url_month in [url_this_month, url_next_month]:
        print(url_month)
        soup = get_soup(url_month)
        df = pd.concat([df, get_schdule(soup)], axis=0)
        print(df.shape)

        # 次ページ以降対応
        resultSet = soup.findAll('li', {'class':'pageIndexNum'})
        pagelinks = []
        for tag in resultSet:
            pagelinks.append(tag.find('a')['href'])
        pagelinks = list(set(pagelinks))  # to unique
        if len(pagelinks) > 1: # 次ページ以降が存在
            print('len(pagelinks):', len(pagelinks))
            pagelinks = np.sort(pagelinks)[1:]
            for i, pagelink in enumerate(pagelinks):
                print(i, pagelink)
                url_page = url_base + urllib.parse.quote(pagelink)
                soup = get_soup(url_page)
                df = pd.concat([df, get_schdule(soup)], axis=0)
                print(df.shape)

    # output
    name = str_this_month + '-' + str_next_month + '.tsv'
    path = os.path.join(output_dir, name)
    df.to_csv(path, sep='\t', index=False)
    print('output:', path)

if __name__=='__main__':
    main()
