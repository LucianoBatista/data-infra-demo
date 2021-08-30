import pandas as pd


lms_df = pd.read_csv("../data/query_result_2021-08-28T08_00_17.45991Z.csv")
lms_columns = lms_df.columns
print(lms_columns)
