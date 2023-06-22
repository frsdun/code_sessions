# %%

import pandas as pd
import numpy as np

# %%
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

# %%

dates = pd.date_range("20130101", periods=6)
dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df

# %%

import plotly.express as px


# Creating the Figure instance
fig = px.line(x=[1, 2, 3], y=[1, 2, 3])

# printing the figure instance
fig


# %%
