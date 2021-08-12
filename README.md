BOM2Jenkinsfile
=========================
1.개요
-------------------------
임베디드 SW의 SW Integration을 위해, MS 엑셀로 작성된 SW BOM을 기반으로 Jenkins에서 SW Integration을 자동화하는 도구.
SW BOM에 정의된 컴포넌트 ID와 버전을 확인해서, 해당 버전을 SCM(Git/SVN/PTC CM) 등에서 Clone/Checkout 해서 Jenkins 빌드를 위한 Jenkinsfile을 생성
SW BOM과 사전 정의된 빌드 로직을 조합해서 Jenkinsfile을 생성하며, 세부 통합은 각 프로젝트에 맞게 변경 필요

2.설치 방법 (필요시)
-------------------------
* 가상 환경 설정: requirements.txt 다운 => 커맨드 창에서 파일이 존재하는 경로로 이동 => pip install -r requirements.txt 실행

3.파일 구성
-------------------------
* BOM2Jenkinsfile.py: BOM구성.xlsx 파일을 Jenkinsfile로 변환하는 로직 파일
* BOM구성.xlsx: SW-BOM을 정의한 파일. 각 컴포넌트 ID와 Ver이 포함된다.
* JenkinsBuildSetting.txt: Jenkinsfile에서 로직을 정의하는 파일로, BOM구성.xlsx와 합쳐져 Jenkins가 자동 빌드하기 위한 Jenkinsfile의 일부분이 됨

4.실행 방법
-------------------------
* 커맨드 창에서 파일이 존재하는 경로로 이동 => python BOM2Jenkinsfile.py <BOM구성.xlsx> (-s)
  * 경고 무시하고 덮어쓰기 할 시에는 -s를 작성

5.실행 사전 조건 (필요시)
-------------------------
* BOM2Jenkinsfile.py, <BOM구성.xlsx>, JenkinsBuildSetting.txt 3가지 파일이 한 폴더 안에 존재해야함
