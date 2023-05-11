import streamlit as st
st.title("Hello, Streamlit!")
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is plain text")
st.markdown("This is **markdown** text")

import pandas as pd
data = {
'Column1': [1, 2, 3],
'Column2': ['A', 'B', 'C']}
df = pd.DataFrame(data)
st.table(df)
st.dataframe(df)

code = '''
def hello_world():
print("Hello, World!")'''
st.code(code, language='python')


st.button('Click me')