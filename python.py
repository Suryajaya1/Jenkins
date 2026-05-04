import pandas as pd

file_path = r"C:\Users\p1345357\Downloads\New_folder\2026_04_27_V1.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

df['SiteID'] = df['LogFilename'].str.extract(r'_(\d+)\.log')

df = df[df['SiteID'].isin(['71','72','73','74','85'])]

result = df.groupby(['date', 'SiteID']).size().reset_index(name='Total')

print(result)