import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def analyze_data(df):
    print("Data Info:")
    print(df.info())

    print("\nData Preview:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nSummary Statistics:")
    print(df.describe())

    if 'Year' in df.columns and 'Value' in df.columns:
        yearly_avg = df.groupby('Year')['Value'].mean()
        print("\nAverage Value per Year:")
        print(yearly_avg)

def main():
    filepath = "F:\master\Total_Growing_Degree_Days_for_10C__days.csv"
    df = load_data(filepath)
    analyze_data(df)

if __name__ == "__main__":
    main()
