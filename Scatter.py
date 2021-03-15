import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")

fig=px.scatter(df,x="Country",y="Population",title="Per capita income",color="InternetUsers",size="Percentage")


fig.show()