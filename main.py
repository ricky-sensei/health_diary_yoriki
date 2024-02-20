import shutil
import openpyxl
import os


original_file_path = "./original/保健日誌　改訂版.xlsm"
copy_file_path = "./copied/保健日誌　コピー.xlsm"
year = str(input("年度："))


def new_empty_file(file_path):
    wb = openpyxl.load_workbook(file_path)
    print(wb.sheetnames)


if not os.path.exists(copy_file_path):
    shutil.copy(original_file_path, copy_file_path)
    print("ready")
    new_empty_file(copy_file_path)

