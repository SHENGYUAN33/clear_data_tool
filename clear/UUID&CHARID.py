import pandas as pd

# 讀取 CSV 檔案（請替換成實際檔名）
df1 = pd.read_csv(r"C:\Users\vghuser\Downloads\ID.csv")  # 包含 a, b 欄
df2 = pd.read_csv(
    r"C:\Users\vghuser\Downloads\dementia_chartids.csv")  # 包含 c 欄

# 清洗欄位資料（轉為字串並移除空白）
df1['UUID'] = df1['UUID'].astype(str).str.strip()
df1['CHARTID'] = df1['CHARTID'].astype(str).str.strip()
df2['CHARTID'] = df2['CHARTID'].astype(str).str.strip()

# .astype(str)：將欄位轉成字串型別
# .str.strip()：去除前後的空白、不可見符號，避免對應失敗


# 用 df1['b'] 對應 df2['c']，並取出對應的 df1['a'] 填入 df2['d']
mapping = dict(zip(df1['UUID'], df1['CHARTID']))
df2['UUID'] = df2['CHARTID'].map(mapping)

# 儲存結果
df2.to_csv(r'C:\Users\vghuser\Downloads\dementia_chartids.csv', index=False)

print("合併完成，已儲存為 merged_output.csv")
