# 기본 정보 데이터 저장하기
def create_info(BOM):
    info = {BOM[0][0]: BOM[1][0], BOM[0][1]: BOM[1][1], BOM[0][2]: BOM[1][2]}
    return info

# ID 데이터와 Version 데이터들을 리스트로 저장하기
def create_data(BOM):
    list_ID = []
    list_ver = []
    column = 5
    list_del = []
    try:
        while column >= 5 and len(list_ID) <= len(BOM[1:][4:]) and len(list_ver) <= len(BOM[1:][4:]):
            list_ID.append(str(BOM[1][column]))
            list_ver.append(str(BOM[2][column]))
            column += 1
    except (ValueError, KeyError):
        pass

    for index in range(len(list_ID)):
        # 버전 미입력시 경고문 출력
        if list_ID[index] == list_ver[index]:
            list_del.append(index)
        elif list_ID[index] == "":
            print("%s 버전인 이름이 입력되지 않았습니다." % list_ver[index])
        elif list_ver[index] == "":
            print("%s의 버전이 입력되지 않았습니다." % list_ID[index])
        index += 1

    list_del.reverse()
    for delete in list_del:
        del list_ID[delete]
        del list_ver[delete]
    return {"list_ID": list_ID, "list_ver": list_ver}
