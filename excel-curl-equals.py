import pandas

file = open("enforced.sh","w+")

df = pandas.read_excel("Book1.xlsx")

for i in range(0, 163):
    if df.iloc[i, 1] == 'In Force-New Issue':
        print str(df.iloc[i, 0]) + ' -> ' + str(df.iloc[i, 1])
        file.write('curl -X POST "http://10.21.20.44:8090/issuance/admin/patch/policy/' + str(df.iloc[i, 0]) + '?nextTaskType=CANCELED" -H  "accept: */*"')
        file.write('\n')