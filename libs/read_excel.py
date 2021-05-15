import xlrd


def read_input(source):
    wb = xlrd.open_workbook(source)
    sheet = wb.sheet_by_index(0)
    data = []
    for j in range(1, sheet.nrows):
        data.append(sheet.row_values(j))
        ##print(sheet.row_values(j))
    ##        for i in range(0, len(data)):
    ##            for k in range(0, len(data[i])):
    ##                print (data[i][k])
    return data
