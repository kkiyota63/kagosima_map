# 必要なライブラリをインポート
import streamlit as st
import pandas as pd

# データを読み込む
data = pd.read_csv("data.csv")

# 列名をStreamlitが認識できる形式に変更
data = data.rename(columns={"Latitude": "lat", "Longitude": "lon"})

# タイトルを表示
st.title("Kagoshima Tourism Map")

# カテゴリ選択ボックス
category = st.selectbox("Choose a category", ["All", "Tourist Spots", "Restaurants", "Hotels", "Transportation"])

# カテゴリに基づいてデータをフィルタリング
if category != "All":
    filtered_data = data[data["Category"] == category]
else:
    filtered_data = data

# マップを表示
st.map(filtered_data)

# 詳細情報を表示するオプション
if st.checkbox("Show Details"):
    st.write(filtered_data)
