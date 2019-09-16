import os
import sys
import time
import io
import re

import hachoir
from hachoir import core
from hachoir import metadata
from hachoir import parser
from hachoir import stream
from hachoir import subfile


def getCreationDate(file):
    parserFile = parser.createParser(file)
    if not parserFile:
        print("创建解析器失败：" + file)
        return False

    try:
        meta = metadata.extractMetadata(parserFile)
        parserFile.stream._input.close() # close the file
    except ValueError:
        print('捕获到异常：ValueError')
        meta = None

    if not meta:
        print('提取Meta信息失败：' + file)
        return False

    metaDic = meta.exportDictionary()

    # 2017-02-09 12:53:05
    return time.strptime(metaDic['Metadata']['Creation date'],"%Y-%m-%d %H:%M:%S")


def organizeFileByYear(file):
    createTime = getCreationDate(file)
    if not createTime:
        return False

    year = time.strftime("%Y", createTime)

    if not os.path.exists(year):
        os.mkdir(year)

    os.rename(file, year + '/' + file)
    print(file + " --> " + year)


def organizeDir(dir):
    for file in os.listdir(dir):
        if os.path.isfile(file):
            organizeFileByYear(file)


def usage():
    print('\n'.join([
            'Usage:',
            '   python organize-album.py <directory>',
            '   python organize-album.py <file>'
        ]))




if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    if os.path.isdir(argv[1]):
        organizeDir(argv[1])
    elif os.path.isfile(argv[1]):
        organizeFileByYear(argv[1])
    else:
        usage()

    sys.exit(0)