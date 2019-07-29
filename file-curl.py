import glob

fileList = glob.glob("*.html")

file = open("curl.sh","w+")

for fileName in fileList:
    file.write("curl -X POST -F 'template=@" + fileName + "' https://services.dt-aegonlife.com/docstore/templates --header 'Content-Type:multipart/form-data' --header 'X-DS-DOCPOLICY:TEMPLATE'\n")