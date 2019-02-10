import openpyxl
import json

daysCount = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
filenamesList = []
for m in range(3, 12):
    for d in range(1, daysCount[m-1]+1):
        filename = '%02d'%m+'%02d'%d+'18.xlsx'
        filenamesList.append(filename)
filenamesList = filenamesList[24:-14]
# print(filenamesList)
gameNameList = set()
for f in filenamesList:
    print("Processing "+f)
    wb = openpyxl.load_workbook('.//data//'+f)
    sh = wb.get_active_sheet()
    for gn in list(sh.columns)[3]:
        gameNameList.add(gn.value)
    wb.close()
    print("Closing "+f)

gameNameList.remove('Games')

# print(gameNameList)
file = open('.//gamenames.json', 'w+', encoding='utf8')
json.dump(list(gameNameList), file)