import os
import sys
# Jenkins 파일 이름 중복 검사
def test_overlap(jenkinsname="jenkinsfile"):
    filename = jenkinsname
    number = 0
    while os.path.isfile(os.path.join("./", filename)) and (len(sys.argv) == 2 or sys.argv[2] != "-s"):
        overlap = str(input("%s 파일이 이미 있습니다. 덮어쓰시겠습니까?(y/n)\n" % filename))
        if overlap == "n":
            number += 1
            filename = jenkinsname + str(number)
        else:
            break
    return filename