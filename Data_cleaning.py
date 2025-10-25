import pandas as pd


df = pd.read_csv('Superstore Sales Dataset.csv')
df.set_index('Row ID', inplace=True)
print(df.isnull().sum())
print("------------------")
print(df.nunique())
print("------------------")

# Dropped "Country" column as it has redundant values (all values are "United States")
df.drop(columns="Country",inplace=True)
df["Postal Code"] = df["Postal Code"].fillna('000000')

# function for casting postal code to string
def postal_to_str(code):
    if code == '000000':
        return '000000'

    try:
        return str(int(code))
    except ValueError:
        return str(code)

# Casting Postal Code column to string
df['Postal Code'] = df['Postal Code'].apply(postal_to_str)



df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")

print(df[df['Postal Code'] == '000000'])
print("------------------")

# A loop to iterate on object columns to remove white spaces
for col in df.select_dtypes(include=['object']):
    df[col] = df[col].str.strip()

df.to_csv('Cleaned_Superstore_Sales_Dataset_v1.csv')