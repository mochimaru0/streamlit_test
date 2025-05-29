# import streamlit as st
# import pandas as pd

# st.write("Hello World")

# st.write("Hello :blue[World]")

# st.title("Hello World")

# st.title("Hello World:sunglasses:")

# st.write(
#     pd.DataFrame(
#         {
#             'first column': [1, 2, 3, 4],
#             'second column': [10, 20, 30, 40]
#         }
#     )
# )

# st.link_button('click here', 'https://docs.streamlit.io/develop/api-reference')

# st.header('Hello World', divider='rainbow')

# code = """print("hello")"""
# st.code(code, language='python')

# agree = st.checkbox("I agree")
# if agree:
#     st.write("Okay!")

# options = st.multiselect(
#     '好きな色は何ですか？',
#     ['赤', '青', '緑', '黄色']
# )

# st.write('あなたが選択した色は：', options)

# options = st.radio(
#     '好きな色は何ですか？',
#     ['赤', '青', '緑', '黄色']
# )

# st.write('あなたが選択した色は：', options)

# # 修正できるデータフレーム
# df = pd.DataFrame(
#     [
#         {'colors': '赤', 'rating':4, 'mark': True},
#         {'colors': '青', 'rating':5, 'mark': True},
#         {'colors': '緑', 'rating':3, 'mark': True},
#     ]
# )

# edited_df =st.data_editor(df)
# edited_df = edited_df[edited_df['mark'] == True]
# st.write(edited_df.loc[edited_df['rating'].idxmax()]['colors'])

# # ダウンロードボタン
# csv = edited_df.to_csv().encode('utf-8')

# st.download_button(
#     label='CSVをダウンロード',
#     data=csv,
#     file_name='edited_df.csv',
#     mime='text/csv',
# )

# # プログレスバー表示
# df = pd.DataFrame(
#     {
#         'sales': [20, 55, 100, 80],
#         'progress_sales': [20, 55, 100, 80]
#     }
# )

# st.data_editor(
#     df,
#     column_config={
#         'progress_sales': st.column_config.ProgressColumn(
#             min_value=0,
#             max_value=100,
#         ), 
#     }
# )

# # 時系列バー表示
# df = pd.DataFrame(
#     {
#         'sales':[
#             [0, 4, 26, 30, 60, 80, 100],
#             [3, 50, 0, 80, 40, 30, 100]
#         ]
#     }
# )
# st.data_editor(df)

# st.data_editor(
#     df,
#     column_config={
#         'sales': st.column_config.BarChartColumn(
#             y_min=0,
#             y_max=100,
#         ), 
#     }
# )

# # 時系列折れ線グラフ
# st.data_editor(
#     df,
#     column_config={
#         'sales': st.column_config.LineChartColumn(
#             y_min=0,
#             y_max=100,
#         ), 
#     }
# )

# # スライダー
# age = st.slider('あなたは何歳ですか？', 0, 130, 40)
# st.write('私は', age, '歳です')

# # 日付選択
# import datetime
# date = st.date_input('あなたが生まれたのはいつですか？', datetime.date(2000, 1, 1))
# st.write('私は', date, 'に生まれました')

# # ユーザーの自由記述
# text = st.text_input('入力してください', 'xxxxxxx')
# st.write(text)

# # カラムを分ける
# col1, col2 = st.columns(2)
# with col1:
#     st.title('Column1')
#     st.write('これはカラムの1です')
# with col2:
#     st.title('Columns2')
#     st.write('これはカラム2です')

# # タブを分ける
# tab1, tab2 = st.tabs(['tab1', 'tab2'])
# with tab1:
#     st.title('tab1')
#     st.write('これはタブの1です')
# with tab2:
#     st.title('tab2')
#     st.write('これはタブの2です')

# # アコーディオン表示
# with st.expander('もっと詳しく見る'):
#     st.write('xxxxxx')

# # ポップアップ表示
# with st.popover('もっと詳しく見る'):
#     st.write('xxxxx')

# # サイドバー
# with st.sidebar:
#     st.title("Streamlit Demo")
#     st.write("このアプリは様々なStreamlit機能のデモです")

# # notification
# agree = st.checkbox('同意しますか？')
# if agree:
#     st.toast('Thank you', icon='👍')

# # 特殊な表示
# birthday = st.checkbox('今日はあなたの誕生日ですか？')
# if birthday:
#     st.toast('誕生日おめでとう！', icon='👍')
#     st.balloons()

# 複数ページ実装
# st.subheader("ナビゲーション")
# st.page_link('app.py', label='Home', icon='🏠')
# st.page_link('pages/page1.py', label="📊 データ可視化")
# st.page_link('pages/page2.py',  label="📝 データ編集")
# st.page_link("pages/page3.py", label="📋 フォーム")


# # 外部リンク
# st.divider()
# st.caption("参考リンク")
# st.page_link("https://docs.streamlit.io/develop/api-reference", label="🔗 Streamlit APIドキュメント")

import streamlit as st
import pandas as pd

# ページ設定
st.set_page_config(
    page_title="Streamlit Demo",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# サイドバー
with st.sidebar:
    st.title("Streamlit Demo")
    st.write("このアプリは様々なStreamlit機能のデモです")
    
  # 複数ページ実装
st.subheader("ナビゲーション")
st.page_link('app.py', label='Home', icon='🏠')
st.page_link('pages/page1.py', label="📊 データ可視化")
st.page_link('pages/page2.py',  label="📝 データ編集")
st.page_link("pages/page3.py", label="📋 フォーム")
    
    # 外部リンク
    st.divider()
    st.caption("参考リンク")
    st.page_link("https://docs.streamlit.io/develop/api-reference", label="🔗 Streamlit APIドキュメント")

# メインコンテンツ
st.title("Streamlit デモアプリケーション 👋")
st.markdown("""
このアプリケーションはStreamlitの様々な機能をデモンストレーションします。
サイドバーから各ページに移動して、それぞれの機能を試してみてください。
""")

# タブを使った基本デモ
tab1, tab2, tab3 = st.tabs(["テキスト表示", "データ表示", "スタイル例"])

with tab1:
    st.header("テキスト表示", divider="rainbow")
    
    st.subheader("基本的なテキスト")
    st.write("Hello World")
    st.write("Hello :blue[World]")
    
    st.subheader("コード表示")
    code = """
    import streamlit as st
    
    st.title("Hello Streamlit")
    st.write("This is a simple Streamlit app")
    """
    st.code(code, language="python")

with tab2:
    st.header("データ表示")
    
    st.subheader("シンプルなデータフレーム")
    df = pd.DataFrame({
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
    })
    st.write(df)
    
    st.subheader("インタラクティブな表示")
    with st.expander("データフレームの詳細を見る"):
        st.dataframe(df, use_container_width=True)
        st.info("サイドバーのナビゲーションから「データ編集」ページに移動すると、より高度なデータ操作が可能です")

with tab3:
    st.header("UI要素とスタイル")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("カラムレイアウト")
        st.write("これはカラム1です")
        
        if st.button("通知を表示"):
            st.toast("通知が表示されました！")
            st.balloons()
    
    with col2:
        st.subheader("ポップオーバー")
        with st.popover("詳細を表示"):
            st.write("ポップオーバーの中身です")
            st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)

# フッター
st.divider()
st.caption("Streamlitデモアプリケーション © 2025")
