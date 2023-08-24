import streamlit as st
import pandas as pd
import numpy as np
import datetime

from functions import sort_expiration
import os

# カスタムスタイリング
st.markdown(
    """
    <style>
        .highlight {
            color: #E694FF;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# アプリのタイトル
st.markdown("<h1 style='text-align: center;'>ホーム</h1>", unsafe_allow_html=True)

# 現在のスクリプトファイルのディレクトリを取得
current_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(current_dir, "pages", "data", "stock.sqlite")

if not os.path.exists(filepath):
    st.error(f"{filepath} が存在しません。")
    exit()

df, food_list = sort_expiration(filepath=filepath, limit=3)

dt_now = datetime.datetime.now()
expiration_date = dt_now + datetime.timedelta(days=7)
expiration_date = expiration_date.strftime("%Y%m%d")

notice_df = df[df['expiration_date'] <= int(expiration_date)]
notice_df['expiration_date'] = pd.to_datetime(notice_df['expiration_date'].astype(str))
notice_df['expiration_date'] = notice_df['expiration_date'].dt.date

if len(notice_df) == 0:
    expanded = False
    comment = "消費期限が近いものはありません"
else:
    expanded = True
    comment = "消費期限が近いです！レシピを確認してください！"

with st.expander(comment, expanded=expanded):
    for _, row in notice_df.iterrows():
        st.markdown(f"<span class='highlight'>{row['food_name']}</span> の消費期限は <span class='highlight'>{row['expiration_date']}</span> です。", unsafe_allow_html=True)

# ダミーデータの作成
data = np.random.rand(50, 2)
df = pd.DataFrame(data, columns=["サンプル1", "サンプル2"])

# グラフの描画
st.markdown("<h3 style='text-align: center;'>廃棄金額</h3>", unsafe_allow_html=True)
st.line_chart(data=df, use_container_width=True)
st.area_chart(data=df, use_container_width=True)
st.bar_chart(data=df, use_container_width=True)
