import os

# 파일명을 입력 받아서 해당 파일을 열고 목적파일에 추가하여 쓴다.
def combineTwoFile (sFile, rFile, dirname):

    # 하위폴더 없으면 만들기기
    if not (os.path.isdir(dirname+"result/")):
        os.makedirs(os.path.join(dirname+"result/"))

    # 소스파일 및 결과파일 open
    sourceFile = open(dirname+sFile, "r+", encoding="euc_kr")
    resultFile = open(dirname+"result/"+rFile, "a+", encoding="euc_kr")

    # 소스파일에서 data 읽기
    sData = sourceFile.read()

    # 결과 파일에 읽은 결과 덮어쓰기
    resultFile.write(sData)

    # 파일 닫기
    sourceFile.close()
    resultFile.close()

