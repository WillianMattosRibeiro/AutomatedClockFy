import pandas as pd

df = pd.read_json("json/parameters.json", lines=True)
print(df)