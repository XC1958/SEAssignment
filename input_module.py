from visualization_module import update_pie_chart 
import csv

data = [] 
CSV_FILE = 'expense_log.csv'

def save_data_to_csv(data):
    """ 將目前的費用資料寫入 CSV 檔案。"""
    try:
        with open(CSV_FILE, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['金額', '類別', '日期']) 
            writer.writerows(data)
        print(f"資料已同步儲存到：{CSV_FILE}")
    except Exception as e:
        print(f"寫入 CSV 檔案時發生錯誤：{e}")


def run_input_module():
    """ 運行費用追蹤輸入介面。"""
    print("=== 費用追蹤輸入模組 (輸入 'q' 結束) ===")
    print("輸入格式: [金額] [類別] [日期 YYYY-MM-DD]")

    update_pie_chart(data) 

    while True:
        try:
            user_input = input("費用 > ").strip()
            
            if user_input.lower() == 'q':
                break
            
            parts = user_input.split(' ')
            if len(parts) < 3:
                raise IndexError

            price = int(parts[0])
            category = parts[1]
            date = parts[2]
            
            if price <= 0:
                print("金額必須是正數。")
                continue

            data.append([price, category, date])
            
            save_data_to_csv(data)
            
            update_pie_chart(data) 
            
        except ValueError:
            print("輸入錯誤：金額必須是數字，且格式必須正確。")
        except IndexError:
            print("格式錯誤。請輸入: [金額] [類別] [日期 YYYY-MM-DD]")
        except Exception as e:
            print(f"發生未知錯誤：{e}")

if __name__ == '__main__':
    run_input_module()