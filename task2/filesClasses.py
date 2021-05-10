import enum
import platform

PATH_SEPARATOR = "\\" if platform.system() == "Windows" else "/"

class FileStatus(enum.Enum):
    MISSING_ARGUMENT = 0
    UNSUPPORTED_HASH_ALGORITHM = 1
    READY_TO_CHECK = 2
    FILE_NOT_FOUND = 3
    FAIL = 4
    OK = 5

class Hash(enum.Enum):
    md5 = 0
    sha1 = 1
    sha256 = 2

class FileToCheck:
    def __init__(self):
        self.filename = None
        self.algorithm = None
        self.hashSum = None
        self.status = None