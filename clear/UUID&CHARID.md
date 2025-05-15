
---

## ✅ 完整程式碼 + 詳解：

```python
import pandas as pd
```

🔹 載入 `pandas` 套件，這是 Python 處理表格資料（例如 Excel、CSV）最常用的工具。

---

```python
# 讀取 CSV 檔案（請替換成實際檔名）
df1 = pd.read_csv('data1.csv')  # 包含 a, b 欄
df2 = pd.read_csv('data2.csv')  # 包含 c 欄
```

🔹 用 `pandas.read_csv()` 讀取兩個 CSV 檔案：

* `df1`：原始資料，包含欄位 `a`（你要找的值）和 `b`（UUID）
* `df2`：查詢資料，只有 `c` 欄（UUID），你要根據它找出對應的 `a`

---

```python
# 清洗欄位資料（轉為字串並移除空白）
df1['a'] = df1['a'].astype(str).str.strip()
df1['b'] = df1['b'].astype(str).str.strip()
df2['c'] = df2['c'].astype(str).str.strip()
```

🔹 為了確保資料能準確比對：

* `.astype(str)`：將欄位轉成字串型別
* `.str.strip()`：去除前後的空白、不可見符號，避免對應失敗

---

```python
# 用 df1['b'] 對應 df2['c']，並取出對應的 df1['a'] 填入 df2['d']
mapping = dict(zip(df1['b'], df1['a']))
df2['d'] = df2['c'].map(mapping)
```

🔹 **這是核心邏輯**：

1. `zip(df1['b'], df1['a'])`
   把兩個欄位配對起來，例如：

   ```python
   ('00008190-xxx', 40007758)
   ('0004f1cd-xxx', 7235065)
   ```

2. `dict(...)`：把配對轉成查找表（dictionary），像這樣：

   ```python
   {
       '00008190-xxx': '40007758',
       '0004f1cd-xxx': '7235065'
   }
   ```

3. `df2['c'].map(mapping)`：根據 `c` 去查找對應的值（就是 `a`），結果放進 `df2['d']`

---

```python
# 儲存結果
df2.to_csv('merged_output.csv', index=False)
```

🔹 把合併後的 `df2` 存成新的 CSV 檔案，命名為 `merged_output.csv`

* `index=False` 表示不儲存 pandas 的索引欄位（0, 1, 2...）

---

```python
print("合併完成，已儲存為 merged_output.csv")
```

🔹 終端機提示訊息，讓你知道程式執行成功。

---

## 🔚 最終輸出會長這樣：

| c                                    | d        |
| ------------------------------------ | -------- |
| 00008190-1e30-4319-b3d2-b3363222a3ae | 40007758 |
| 0004f1cd-a035-4f92-8c5e-dac12f487421 | 7235065  |
| ...                                  | ...      |

