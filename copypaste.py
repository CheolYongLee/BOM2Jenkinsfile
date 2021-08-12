import clipboard
# 텍스트 파일에서 내용을 복사하여 다른 파일에 붙여넣기
def text_copypaste(list_info, list_ID, list_ver, filename, jenkinssetting='JenkinsBuildSetting.txt'):
    # 파일 내용 복사
    f = open(jenkinssetting, 'r')
    clipboard.copy(f.read())
    f.close()
    # 복사한 내용 붙여넣기
    f = open(filename, 'w')
    for data in range(len(list_info)):
        f.write("# %s : %s\n" % (list_info[data][0], list_info[data][1]))
    f.write("\n")
    for number in range(len(list_ID)):
        f.write("def %s = '%s'\n" % (list_ID[number], list_ver[number]))
        number += 1
    f.write("\n\n" + clipboard.paste())
    f.close()
    return print("Copy and Paste success!!")