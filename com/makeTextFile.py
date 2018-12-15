import ss_libs.getFile as getFile
import ss_libs.combineFile as combFile
import datetime

#################################
# 파일 읽은 후 전체파일 합치기
#################################
# source file 위치 지정
# dir = "." #"../data"
dir = "C:/Users/07174/Desktop/닭"

# source 파일 리스트 저장
sourceFiles = getFile.fileNameSearch(dir+"/")

# 결과파일명 생성
resultFileName = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+".txt"

# # 모든파일 합치기
for sourceFile in sourceFiles:
    combFile.combineTwoFile(sourceFile, resultFileName, dir+"/")
