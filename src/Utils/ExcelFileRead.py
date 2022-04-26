import xlrd

from Utilities.Constants import Constants
class ExcelFileRead():

    Constants=Constants()

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










