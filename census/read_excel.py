import xlrd

book = xlrd.open_workbook('2011-income-distribution.xlsx')

print book.nsheets
print book.sheet_names()

sh = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols
print type(sh.cell(rowx=1,colx=0).value)
print sh.cell(rowx=0,colx=0).value,"\t",
for col in range(1, 7, 2 ) :
    print sh.cell(rowx=0,colx=col).value,"\t",
print
for row in range(1,sh.nrows) :
    print sh.cell(rowx=row,colx=0).value,"\t",
    for col in range(1,7,2) :
        print sh.cell(rowx=row,colx=col).value,"\t",
    print



