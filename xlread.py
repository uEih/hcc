import os
import sqlite3
from win32com.client import constants, Dispatch
import sys

#----------------------------------------
# get data from excel file
#----------------------------------------

XLS_FILE = os.getcwd() + "\\CWPspreadsheet.xlsx"
print XLS_FILE
ROW_SPAN = (1, 410)
COL_SPAN = (2, 4)
app = Dispatch("Excel.Application")
app.Visible = True
ws = app.Workbooks.Open(XLS_FILE).Sheets(1)
exceldata = []
for col in xrange(COL_SPAN[0], COL_SPAN[1]):
	excelcolumn = [str(ws.Cells(row, col).Value) 
				 for row in xrange(ROW_SPAN[0], ROW_SPAN[1])]
	exceldata.append(excelcolumn)

	
#----------------------------------------
# create SQL table and fill it with data
#----------------------------------------


conn = sqlite3.connect('CWP.db')
c = conn.cursor()


# print exceldata
# sys.exit()
for row in exceldata:
	c.execute('INSERT INTO exceltable VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)

	
	
# conn.commit()

#----------------------------------------
# display SQL data
#----------------------------------------

c.execute('SELECT * FROM exceltable')
for row in c:
	print row
