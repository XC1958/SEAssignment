# 費用追蹤與視覺化系統

## 專案概述 (Project Overview)

這是一個基於 Python 的輕量級費用追蹤工具。它允許使用者透過命令列介面輸入日常開支的金額、類別和日期，並即時完成兩項操作：

1. 視覺化分析：即時生成並顯示費用的圓餅圖 (Pie Chart)，展示類別分佈。

2. 資料持久化：將所有歷史紀錄同步儲存至 CSV 文件，便於後續分析。

## 專案功能 (Features)

* 互動式輸入：簡單的命令列介面輸入格式 `[金額] [類別] [日期 YYYY-MM-DD]`。

* 即時視覺化：使用 Matplotlib 生成費用類別圓餅圖，自動儲存為 `category_pie_chart.png`。

* 數據導出：所有費用資料自動同步寫入 `expense_log.csv` 文件。

* 中文支援：圖表和輸出皆能正確顯示中文字符。

* 錯誤處理：驗證輸入格式和金額有效性。

* Excel 兼容性：CSV 文件使用 `utf-8-sig` 編碼，以確保在 Windows 環境下使用 Excel 雙擊開啟時，中文字符能正確顯示。

## 環境設定與依賴 (Setup and Dependencies)

### 1. 必備環境
您需要安裝 Python 3.x。

### 2. 安裝依賴庫
本專案需要 `matplotlib` 庫來繪製圖表。請打開您的終端機或命令提示字元，執行以下指令：

```bash
pip install matplotlib
```

### 3. 中文字型
由於程式碼中使用了中文字型 (`Microsoft JhengHei` 或 `SimHei`)，為確保圖表上的中文標題和類別名稱能正確顯示，請確認您的作業系統已安裝至少一種中文字型。

## 執行步驟 (How to Run)

### 1. 準備文件
請將 `input_module.py` 和 `visualization_module.py` 這兩個程式碼文件保存在同一個資料夾內。

### 2. 啟動程式
在該資料夾的路徑下，打開終端機或命令提示字元，執行主程式：

```bash
python input_module.py
```

### 3. 輸入費用
程式啟動後，您會看到提示： 

```
=== 費用追蹤輸入模組 (輸入 'q' 結束) === 
輸入格式: [金額] [類別] [日期 YYYY-MM-DD] 
費用 >
```

請按照指定的格式輸入費用，例如：

```
費用 > 500 食物 2025-12-14
資料已同步儲存到：expense_log.csv
圖表已更新並儲存為：category_pie_chart.png
```

每次輸入後，系統會：

1. 彈出 Matplotlib 繪製的圓餅圖視窗。

2. 同步更新 expense_log.csv 文件。

### 4. 結束程式
輸入 q 並按下 Enter 鍵即可結束程式。

## 輸出文件 (Output Files)

程式運行後將會生成以下兩個文件：

文件名稱: expense_log.csv
內容描述: 包含所有輸入費用紀錄的表格數據。

文件名稱: category_pie_chart.png
內容描述: 根據當前所有資料繪製的費用類別圓餅圖。
