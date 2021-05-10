from filesClasses import *

import sys
import os
import hashlib


def fileRead(file):
    try:
        f = open(file, "r")
    except Exception as e:
        print("Cannot read file with sums")
        sys.exit(e)
    lines = f.readlines()
    files = None
    for line in lines:
        file = FileToCheck()
        words = lines.split()
        if len(words) < 3:
            file.status = FileStatus.MISSING_ARGUMENT
            continue
        file.filename = words[0]
        file.algorithm = words[1]
        if not (file.algorithm in Hash.__members__):
            file.status = FileStatus.UNSUPPORTED_HASH_ALGORITHM
            continue
        file.hashSum = words[2]
        file.status = FileStatus.READY_TO_CHECK
        files.append(file)
    return files

def sumCheck(dir_path, files_info):
    files_to_check = fileRead(files_info)
    for file in files_to_check:
        if file.status == FileStatus.READY_TO_CHECK:
            file_full_name = dir_path+PATH_SEPARATOR+file.filename
            if not os.path.isfile(file_full_name):
                file.status = FileStatus.FILE_NOT_FOUND
                print (file.filename +" "+ file.status)
                continue
            if file.algorithm.value == 0:
                if file.hashSum == hashlib.md5(file_full_name.read()).hexdigest():
                    file.status = FileStatus.OK
                else: file.status = FileStatus.FAIL
            if file.algorithm.value == 1:
                if file.hashSum == hashlib.sha1(file_full_name.read()).hexdigest():
                    file.status = FileStatus.OK
                else: file.status = FileStatus.FAIL
            if file.algorithm.value == 0:
                if file.hashSum == hashlib.sha256(file_full_name.read()).hexdigest():
                    file.status = FileStatus.OK
                else: file.status = FileStatus.FAIL
            print(file.filename + " " + file.status)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ("Invalid number of arguments")
        sys.exit()
    sumCheck(sys.argv[2], sys.argv[1])