import matplotlib.pyplot as plt
from collections import defaultdict

# 確保中文顯示
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei'] 
plt.rcParams['axes.unicode_minus'] = False

CHART_FILE = 'category_pie_chart.png'

def update_pie_chart(data):
    """ 更新費用類別圓餅圖。"""
    if not data:
        print("警告：資料列表為空，跳過圖表生成。")
        return

    category_totals = defaultdict(int)
    
    for amount, category, _ in data:
        category_totals[category] += amount

    if not category_totals:
        print("警告：無法計算總和，跳過圖表生成。")
        return

    # --- Matplotlib 繪圖 ---
    plt.figure() 
    
    labels = category_totals.keys()
    sizes = category_totals.values()

    plt.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=90
    )
    plt.title('費用類別分佈圓餅圖', fontsize=14)
    plt.axis('equal') 

    plt.savefig(CHART_FILE)
    
    plt.show() 
    
    plt.close() 

    print(f"圖表已更新並儲存為：{CHART_FILE}")

if __name__ == '__main__':
    print("本模組專注於圖表函式，請運行 input.py。")