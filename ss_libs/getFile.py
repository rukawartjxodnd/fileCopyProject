import os

# .TXT 파일을 탐색하고 이를 리턴한다.
def fileNameSearch(dirname):

    # return List
    resultFileName = []

    # 폴더내 파일 읽어서 리스트 저장
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.txt':
            resultFileName.append(full_filename.split("/")[-1])


    # 결과 정렬
    resultFileName.sort()

    # 리턴
    return resultFileName