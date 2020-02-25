import os
import re
import pandas as pd

dir_livedoor = '../../data/livedoor/in/news'
output_path = '../../data/livedoor/out/df_livedoor.tsv'

def main():
    rec = re.compile('\n')  # 改行位置を取得するための正規表現パターンをコンパイル
    ls_genre = []
    ls_title = []
    ls_article = []
    for name in os.listdir(dir_livedoor):# 指定ディレクトリ内のループ
        path = os.path.join(dir_livedoor, name) 
        flg_dir = os.path.isdir(path)    

        if not flg_dir: 
            print(name, 'not flg_dir')
            continue # ディレクトリではない場合スキップ
        
        # -入りのファイル名リスト（# LICENCE.TXTを除く意図）
        ls = [s for s in os.listdir(path) if s.__contains__('-')]
        for txtname in ls:
            # テキストファイル読み込み
            txtpath = os.path.join(path, txtname) 
            with open(txtpath, 'r', encoding='utf-8') as f:
                txt = f.read()

            # 改行位置を取得、タイトルと本文を分けて取得
            pos = [m.start() for i, m in enumerate(rec.finditer(txt))]
            #url = txt[:pos[0]]
            #date = txt[pos[0]+1:pos[1]]  # stringでは\nは1文字でカウントされるので+1 
            title = txt[pos[1]+1:pos[2]]
            article = txt[pos[2]+1:]

            # リストに格納
            ls_genre.append(name)
            ls_title.append(title)
            ls_article.append(article)

    # データフレームに格納し、出力
    df = pd.DataFrame()
    df['genre'] = ls_genre
    df['title'] = ls_title
    df['article'] = ls_article
    df.to_csv(output_path, sep='\t', index=False)
    print('output:', output_path)
    
if __name__=='__main__':
    main()
