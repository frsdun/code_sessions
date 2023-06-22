# %%
import pandas as pd

df = pd.read_csv("titanic.csv")

# %%

# ------------------------------------
# Basic investigation
# ------------------------------------

# df.head()
# df.tail(3)
# df.columns
# df.columns.to_list()
# df.dtypes
# df.index
# df.describe()

# ------------------------------------
# Columns
# ------------------------------------

df.Name
df["Name"]
df[["Name", "Age"]]

# ------------------------------------
# Interactions
# ------------------------------------

# df.sort_values(by="Fare", ascending=True)

age_sex_df = df[["Age", "Sex"]]
# survived_df = df[["Name", "Survived"]]

# age_sex_df["Test"] = "example data"
# small_df = df.drop(columns=["PassengerId", "SibSp", "Parch", "Cabin", "Embarked"])

# survived_df = survived_df.astype({"Survived": bool})
# survived_df.rename(columns={"Survived": "survived", "Name": "name"})
# survived_df = survived_df.rename(columns={"Survived": "survived", "Name": "name"})

# survived_df.rename(columns={"Survived": "survived"}).astype({"survived": bool})

# ------------------------------------
# Rows
# ------------------------------------

# len(df)

# df.iloc[]
# df.iloc[3:6]

for index, row in df.iterrows():
    print(f"index: {index}, Name: {row[3]}")

# mask = df["Age"] > 18
# mask

# df_filtered = df[mask]
# df_filtered

# ------------------------------------
# Join (simple)
# ------------------------------------

# age_sex_df = df[["Age", "Sex"]]
# survived_df = df[["Name", "Survived"]]

# join_df = pd.concat([age_sex_df, survived_df], axis=1)
# join_df

# ------------------------------------
# Group by
# ------------------------------------
# 2 parts: groupby | aggregation
# df.groupby("Sex")["Sex"].count()
# df.groupby("Sex")["Age"].mean()

# df.groupby("Sex")["Fare"].mean()

# %%
# import matplotlib.pyplot as plt

# ------------------------------------
# Plots
# ------------------------------------
# df["Survived"].value_counts()
# df["Survived"].value_counts().plot(kind="bar")
# df[["Age", "Fare", "Pclass"]].hist(bins=10, figsize=(9, 7), grid=False)
# %%
