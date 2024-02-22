 
from calendardialog import CalendarDialog
import tkinter
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import simpledialog
from opensheet import opensheet
from datetime import datetime
import create_new


class Test:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("300x300")
        frame = Frame(self.root, bd=4, relief="groove")
        opensheet_label = Label(frame, text="シートを開く")
        opensheet_label.grid(padx=2, sticky="w", row=0, column=0)
        self.entry = Entry(frame, width=20)
        self.entry.grid(sticky="w", row=1, column=0)
        date_select_button = Button(frame, text="日付を指定", width=8, command=self.set_date)
        date_select_button.grid(sticky="w", row=1, column=1)
        today_button = Button(frame, text="今日のシート", width=8, command=self.set_today)
        today_button.grid(sticky="w", row=1, column=2)
        get_sheet_selected_button = Button(frame, text="シートを開く", width=8, command=self.open_sheet)
        get_sheet_selected_button.grid(sticky="w", row=1, column=3)
        update_label = Label(frame, text="年次更新")
        update_label.grid(padx=2, sticky="w", row=2, column=0)
        yealy_update_button = Button(frame, text="年度を選択", width=8, command=self.enter_year)
        yealy_update_button.grid(sticky="w", row=3, column=1)
        frame.pack()

    def set_date(self) -> None:
        dialog = CalendarDialog(self.root, title="calendar")
        date = dialog.get_date()
        if date != "":
            self.entry.delete(0, tkinter.END)
            self.entry.insert(0, date)
    
    def open_sheet(self):
        if self.entry.get():
            date = self.entry.get()
            opensheet(date)
        else:
            print("日付が設定されていません")

    def set_today(self):
        date = datetime.today().strftime('%Y-%m-%d')
        self.entry.delete(0, tkinter.END)
        self.entry.insert(0, date)
    
    def enter_year(self):
        year = tkinter.StringVar()
        year.set(simpledialog.askstring("年度", "年度を西暦で半角で入力してください"))
        create_new.create_new(year.get())
        print("作成完了")
    
    def run(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    test = Test()
    test.run()
