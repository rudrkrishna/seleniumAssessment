import os

import xlrd
import openpyxl
from openpyxl import load_workbook
from src.Utils.Constants import Constants
class ExcelFileRead:

    const=Constants()

    # method to get data from excel sheet
    def getvalue(self, value):
        #data_file = "/Users/rudrkrishna/PycharmProjects/seleniumAssessment/src/TestData/TestData.xlsx"
        wb = load_workbook(self.const.TestDateSheet_Path)
        ws = wb.get_sheet_by_name(self.const.sheet_TestData)
        all_rows = list(ws.rows)
        for row in all_rows:
            if row[0].value == value:
                return row[1].value

    # def OpenExcelFile(self,path):
    #       self.workbook=xlrd.open_workbook(path)
    #
    # def CloseExcelFile(self):
    #       self.workbook.release_resources()
    #
    # def getrowcount(self,sheetname):
    #     self.worksheet=self.workbook.sheet_by_name(sheetname)
    #     rowcount=self.worksheet.nrows+1
    #     return rowcount
    #
    # def getcellData(self,rownumber,columnnumber,sheetname):
    #     self.worksheet = self.workbook.sheet_by_name(sheetname)
    #     self.CellData=str(self.worksheet.cell_value(rownumber,columnnumber))
    #
    #     return self.CellData
    #
    # def getrowcontains(self,testname,columnname,sheetname):
    #     rownumber=0
    #     try:
    #         rowcount=0
    #         rowcount=self.getrowcount(sheetname)
    #         for rownumber in range(0,rowcount):
    #             if self.getcellData(rownumber,columnname,sheetname)==testname:
    #                 break
    #     finally:
    #         print()
    #     return rownumber
    #
    # def getTeststepscount(self,sheetname,testname,stepstart):
    #     try:
    #         rowcount = 0
    #         rowcount = self.getrowcount(sheetname)
    #         for i in range(stepstart, rowcount):
    #             if str(testname)!=str(self.getcellData(i,0,sheetname)):
    #                 return i
    #     finally:
    #         print()



