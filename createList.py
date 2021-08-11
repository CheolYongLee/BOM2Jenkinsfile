# 기본 정보 데이터 저장하기
def create_info(BOM):
    info = {BOM[0][0]: BOM[1][0], BOM[0][1]: BOM[1][1], BOM[0][2]: BOM[1][2]}
    return info

# ID 데이터들을 리스트로 저장하기
def create_ID(BOM, column=5):
    try:
        list_ID = []
        while column >= 5 and len(list_ID) <= len(BOM[1:][4:]):
            # 이름 미입력시 경고문 출력
            if BOM[1][column] == "":
                print("%s 버전인 이름이 입력되지 않았습니다." % BOM[2][column])
                list_ID.append("")
            else:
                list_ID.append(str(BOM[1][column]))
            column += 1
    except (ValueError, KeyError):
        pass
    return list_ID

# Version 데이터들을 리스트로 저장하기
def create_ver(BOM, column=5):
    try:
        list_ver = []
        while column >= 5 and len(list_ver) <= len(BOM[1:][4:]):
            # 버전 미입력시 경고문 출력
            if BOM[2][column] == "":
                print("%s의 버전이 입력되지 않았습니다." % BOM[1][column])
                list_ver.append("")
            else:
                list_ver.append(str(BOM[2][column]))
            column += 1
    except (ValueError, KeyError):
        pass
    return list_ver
