import pandas as pd
import os
import clipboard

# 파일 불러오기
BOMfile = "BOM_20210804.xlsx"
BOM = pd.read_excel(BOMfile, header=None)

# 데이터 추출
ver = BOM[1][0]
data = BOM[1][1]
Author = BOM[1][2]

try:
    column = 5
    list_ID = []
    while column >= 5 and BOM[1][column]:
        list_ID.append(str(BOM[1][column]))
        column += 1
except (ValueError, KeyError):
    pass

try:
    column = 5
    list_ver = []
    while column >= 5 and BOM[2][column]:
        list_ver.append(str(BOM[2][column]))
        column += 1
except (ValueError, KeyError):
    pass

# 파일 내용 복사
f = open('JenkinsBuildSetting.txt', 'r')
clipboard.copy(f.read())
f.close()

# Jenkins 파일 이름 중복 검사
jenkinsname = "jenkinsfile"
filename = jenkinsname
number = 0

while os.path.isfile(os.path.join("./", filename)):
    overlap = str(input("같은 이름의 파일이 이미 있습니다. 덮어쓰시겠습니까?(y/n)\n"))
    if overlap == "n":
        number += 1
        filename = jenkinsname + str(number)
    elif overlap == "y":
        break

# 복사한 내용 붙여넣기
f = open(jenkinsname, 'w')
f.write("# Ver : %s\n# Data : %s\n# Author : %s\n\n" % (ver, data, Author))
for i in range(len(list_ID)):
    f.write("def %s = '%s'\n" % (list_ID[i], list_ver[i]))
    i += 1
f.write("\n\n" + clipboard.paste())
f.close()

print("Jenkinsfile is converted successfully!")