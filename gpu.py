import tkinter as tk
from tkinter import simpledialog
import create_new
# from tkinter import filedialog

root = tk.Tk()
root.title("保健日誌")
root.geometry("300x300")
year = tk.StringVar()


def enter_year():
    year.set(simpledialog.askstring("年度", "年度を西暦で半角で入力してください"))
    create_new.create_new(year.get())
    print("作成完了")


# 変換ボタンを作成
create_new_button = tk.Button(root, text="年次更新", command=enter_year)
create_new_button.pack(pady=20)

root.mainloop()
