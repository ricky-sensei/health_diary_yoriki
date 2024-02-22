import shutil
import openpyxl
import os
import getpass
from datetime import datetime, timedelta


def create_new(year):
    start_date = datetime(int(year), 4, 1)
    end_date = datetime(int(year) + 1, 3, 31)
    date_list = []
    current_date = start_date
    wb_title = year + "年度保健日誌"
    new_filepath = f"C:\\Users\\{getpass.getuser()}\\OneDrive - 八幡平市教育委員会事務局\\ドキュメント - 寄木小職員\\保健日誌\\{wb_title}.xlsm"

    while current_date <= end_date:
        date_list.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)

    if not os.path.exists(new_filepath):
        shutil.copy("./original/original_sheet.xlsm", new_filepath)
        wb = openpyxl.load_workbook(new_filepath, keep_vba=True)
        for date in date_list:
            wb.copy_worksheet(wb["コピー用"])
            ws = wb.worksheets[-1]
            ws.title = date
            for i in range(17, 23):
                ws["T" + str(i)] = f"=SUM('{year}-04-01:{date}'!S{str(i)})"

    wb.save(new_filepath)
