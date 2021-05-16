from PIL.Image import ROTATE_270
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns

# remove warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

st.title('World Happiness Report 2021')
st.header('')

df = pd.read_csv('world-happiness-report-2021.csv')

a = []
for i in df.columns:
    a.append(i)

r = set()
for i in df.loc[:, a[1]]:
    r.add(i)

r = list(r)

st.sidebar.header("Regional Indicator")
regional = st.sidebar.selectbox('Regional Indicator is ', r)

d = df.loc[df[a[1]] == regional]
c = []
for i in d.loc[:, a[0]]:
    c.append(i)


country = st.selectbox('Country selected is', c)
# st.write(df.loc[df[a[0]] == country])
b = df.loc[df[a[0]] == country]
st.table(b[df.columns[:6]])

st.subheader('Visualization')

para = st.selectbox('Parameter selected is', a[2:])
st.subheader(para)

g = sns.barplot(x = a[0], y = para, data = d)
plt.xticks(rotation=45)
st.pyplot()

sns.displot(d[para])
st.pyplot()

sns.rugplot(d[para])
st.pyplot()