import pandas as pd
import sys
import createList
import overlaptest
import copypaste

# 파일 불러오기
BOMfile = sys.argv[1]
BOM = pd.read_excel(BOMfile, header=None).fillna("") # 값이 없는 빈 셀은 공백처리

# 데이터 추출
info = createList.create_info(BOM)
list_info = list(info.items())


list_ID = createList.create_data(BOM)["list_ID"]
list_ver = createList.create_data(BOM)["list_ver"]

# Jenkins 파일 이름 중복 검사
filename = overlaptest.test_overlap()

# 텍스트 파일 내용 복사하여 다른 파일에 붙여넣기
copypaste.text_copypaste(list_info, list_ID, list_ver, filename)

print("Jenkinsfile is converted successfully!")