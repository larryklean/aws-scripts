import xlrd

loc = "FormQuestions.xlsx"
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(1)
file = open("insert_ques_master.sql","w+")

for i in range(1, 47):
    file.write('INSERT INTO question_master (qcode, qtext, TYPE) VALUES ("' + str(sheet.cell_value(i, 1)) + '", "' 
    + str(sheet.cell_value(i, 2)) + '", "' + str(sheet.cell_value(i, 3)) + '");\n')
    
    print('INSERT INTO question_master (qcode, qtext, TYPE) VALUES ("' + str(sheet.cell_value(i, 1)) + '", "' 
    + str(sheet.cell_value(i, 2)) + '", "' + str(sheet.cell_value(i, 3)) + '");\n')