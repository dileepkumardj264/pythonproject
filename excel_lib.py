import xlrd


def read_locators(sheetname):
    workbook = xlrd.open_workbook(r'C:\DILEEP\test locator.xls')
    worksheet = workbook.sheet_by_name(sheetname)
    rows = worksheet.get_rows()
    next(rows)
    locator = {row[0].value: (row[1].value, row[2].value) for row in rows}
    return locator


def read_data(datasheet):
    workbook = xlrd.open_workbook(r'C:\DILEEP\datapage.xls')
    worksheet = workbook.sheet_by_name(datasheet)
    rows = worksheet.get_rows()
    next(rows)
    datas = [(row[0].value, row[1].value) for row in rows]
    return datas
