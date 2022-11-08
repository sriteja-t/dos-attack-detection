import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import itertools

@st.cache
def read_data():
    return pd.read_csv("final.csv")

df = read_data()

st.title("http request method")
request_method_data = dict(df["request_method"].value_counts())
# plt.title("Request method count")
# plt.xlabel("Request method")
# plt.ylabel("Number of requests")
requestMethod = pd.DataFrame(request_method_data.values(), request_method_data.keys())
st.bar_chart(requestMethod)

st.title("http request status codes")
statusCodeCounts = dict(df["status"].value_counts())
statusCodes = list(map(str, list(statusCodeCounts.keys())))
statusCounts = list(statusCodeCounts.values())
patches, texts = plt.pie(statusCounts)
plt.legend(patches, statusCodes, loc="best")
plt.axis('equal')
plt.tight_layout()
st.pyplot(plt)


st.title("Top remote hosts")
remote_host_data = dict(df["remote_host"].value_counts())
asdf = {k: v for k, v in sorted(remote_host_data.items(), reverse=True, key=lambda item: item[1])}
zxcv = dict(itertools.islice(asdf.items(), 10))
top_remote_hosts = list(zxcv.keys())
df_remotehost_country = df[["remote_host", "Country"]]
df_new = df_remotehost_country[df_remotehost_country["remote_host"].isin(top_remote_hosts)]
df_new["new_col"] = df_new["remote_host"] + "\n" + df_new["Country"]
gg = dict(df_new["new_col"].value_counts())
remoteHosts = pd.DataFrame(gg.values(), gg.keys())
st.bar_chart(remoteHosts)