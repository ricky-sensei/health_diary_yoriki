from openpyxl import load_workbook
import os
import getpass


def opensheet(date):
    dir = f"C:\\Users\\{getpass.getuser()}\\OneDrive - 八幡平市教育委員会事務局\\ドキュメント - 寄木小職員\\保健日誌\\"
    print(date[5:7])
    if date[5:7] in ["01", "02", "03"]:
        year = str(int(date[:4]) - 1)
    else:
        year = date[:4]
    filename = year + "年度保健日誌.xlsm"
    print(filename)
    wb = load_workbook(dir + filename, keep_vba=True)
    wb["setsheet"]["A1"] = date
    wb.save(dir+filename)
    wb.close()
    os.chdir(dir)
    os.system(f"start excel.exe {filename}")
