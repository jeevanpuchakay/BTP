import pandas as pd

JSON_FILE_PATH = "/mnt/c/Users/jeeva/Documents/Work/Data/result_original.json"

if __name__=="__main__":
    df = pd.read_json(JSON_FILE_PATH)
    print("Info:")
    print(df.info())