import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime

def special_boss(date):
    bosses = ['掘墓', '铁匠', '嚣嘈', '神罚', '古铁']
    index = date % len(bosses)
    return bosses[index]
 
def parse_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y/%m/%d")
        return date.year, date.month, date.day
    except ValueError:
        raise ValueError("日期格式错误，请使用形如 '20xx/xx/xx' 的格式。")
      
def on_date_select():
    selected_date = cal.get_date()
    try:
        # 将日期格式转换为 "20xx/xx/xx" 的格式
        year, month, day = map(int, selected_date.split("-"))
        formatted_date = f"{year:02d}/{month:02d}/{day:02d}"
        
        year, month, day = parse_date(formatted_date)
        init_date = datetime(2023, 8, 2)
        input_date = datetime(year, month, day)

        date_difference = (input_date - init_date).days
        result = special_boss(date_difference)
        result_label.config(text=f"当日特殊拦截boss为：{result}")
   
    except ValueError as e:
        result_label.config(text=str(e))
        
# 创建主窗口
root = tk.Tk()
root.title("特殊拦截BOSS查询")

# 添加日历控件
cal = Calendar(root, selectmode="day", date_pattern="y-mm-dd")
cal.pack(padx=10, pady=10)

# 添加日期选择按钮
select_button = ttk.Button(root, text="选择", command=on_date_select)
select_button.pack(pady=5)

# 添加结果显示标签
result_label = ttk.Label(root, text="")
result_label.pack(pady=5)

# 运行主循环
root.mainloop()
