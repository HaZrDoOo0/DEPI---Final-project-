import pandas as pd


df = pd.read_excel('Superstore_Sales_Dataset.xls')
print(df.head())

# Setting column "Row ID" as the index of the dataset
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


# Converting both columns ("Order Date" , "Ship Date") to Datetime with format (day/month/year)
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d/%m/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%d/%m/%Y")

# Showing only Date values in both columns
df['Order Date'] = df['Order Date'].dt.strftime('%d/%m/%Y')
df['Ship Date'] = df['Ship Date'].dt.strftime('%d/%m/%Y')


print(df[df['Postal Code'] == '000000'])
print("------------------")

# A loop to iterate on object columns to remove white spaces
for col in df.select_dtypes(include=['object']):
    df[col] = df[col].str.strip()

df.to_excel('Cleaned_Superstore_Sales_Dataset_v3.xlsx')

