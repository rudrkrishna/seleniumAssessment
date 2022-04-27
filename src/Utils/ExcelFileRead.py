from openpyxl import load_workbook
from src.Utils.Constants import Constants

# class which have method to read data from data sheet
class ExcelFileRead:

    # Constant class instance
    const=Constants()

    # method to get data from excel sheet
    def getvalue(self, value):

        wb = load_workbook(self.const.TestDateSheet_Path)
        ws = wb.get_sheet_by_name(self.const.sheet_TestData)
        all_rows = list(ws.rows)
        for row in all_rows:
            if row[0].value == value:
                return row[1].value
