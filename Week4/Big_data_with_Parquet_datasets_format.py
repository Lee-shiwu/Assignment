import pandas as pd
def main():
    file_path="F:\master\Sample-1m.parquet"
    try:
        df=pd.read_parquet(file_path)
        record_count=len(df)
        print(f"Total number of records is {record_count}")
    except Exception as e:
        print(f"Error reading Parquet file :{e}")
        
if __name__ == "__main__":
    main()
