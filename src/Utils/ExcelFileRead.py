import xlrd
import openpyxl
from openpyxl import load_workbook


from Utilities.Constants import Constants
class ExcelFileRead:

    const=Constants()

    def OpenExcelFile(self,path):
          self.workbook=xlrd.open_workbook(path)

    def CloseExcelFile(self):
          self.workbook.release_resources()

    def getrowcount(self,sheetname):
        self.worksheet=self.workbook.sheet_by_name(sheetname)
        rowcount=self.worksheet.nrows+1
        return rowcount

    def getcellData(self,rownumber,columnnumber,sheetname):
        self.worksheet = self.workbook.sheet_by_name(sheetname)
        self.CellData=str(self.worksheet.cell_value(rownumber,columnnumber))

        return self.CellData

    def getrowcontains(self,testname,columnname,sheetname):
        rownumber=0
        try:
            rowcount=0
            rowcount=self.getrowcount(sheetname)
            for rownumber in range(0,rowcount):
                if self.getcellData(rownumber,columnname,sheetname)==testname:
                    break
        finally:
            print()
        return rownumber

    def getTeststepscount(self,sheetname,testname,stepstart):
        try:
            rowcount = 0
            rowcount = self.getrowcount(sheetname)
            for i in range(stepstart, rowcount):
                if str(testname)!=str(self.getcellData(i,0,sheetname)):
                    return i
        finally:
            print()

    def getvalue(self, value):
        data_file =  ("/Users/rudrkrishna/PycharmProjects/seleniumAssessment/src/TestData/TestData.xlsx")
        wb = load_workbook(data_file)
        ws = wb.get_sheet_by_name(self.const.sheet_TestData)
        all_rows = list(ws.rows)
        for row in all_rows:
            if row[0].value == value:
                   return row[1].value


#
# class ExcelUtil:
#
#     @staticmethod
#     def getTestData(test_case_name):
#         Dict = {}
#         book = openpyxl.load_workbook("/Users/rudrkrishna/PycharmProjects/seleniumAssessment/src/TestData/TestData.xlsx")
#         sheet = book.active
#         for i in range(1, sheet.max_row + 1):  # to get rows
#             if sheet.cell(row=i, column=1).value == test_case_name:
#
#                 for j in range(2, sheet.max_column + 1):  # to get columns
#                     Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
#                 print[Dict]
#         return [Dict]
#
#
#
# ExcelUtil().getTestData()

