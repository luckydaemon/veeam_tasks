import enum
import platform

PATH_SEPARATOR = "\\" if platform.system() == "Windows" else "/"

class FileStatus(enum.Enum):
    OK = 0
    MISSING_SOURCE_IN_XML = 1
    INVALID_SOURCE = 2
    MISSING_DESTINATION_IN_XML = 3
    INVALID_DESTINATION = 4
    MISSING_FILENAME_IN_XML = 5
    MISSING_FILE = 6

class FileToProcess:

    def __init__(self):
        self.source = None
        self.destination = None
        self.filename = None
        self.status = None