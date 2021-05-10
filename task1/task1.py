from filesClasses import *

import lxml.etree
import sys
import os
import shutil


def xmlRead(XmlFile):
    try :
        xml_file = lxml.etree.parse(XmlFile)
    except lxml.etree.XMLSyntaxError as e:
        sys.exit(e)
    xml_validator = lxml.etree.XMLSchema(file="example_schema.xsd")
    is_valid = xml_validator.validate(xml_file) # general xml structure checking
    if not is_valid:
        sys.exit("XML file not well formed")
    root = xml_file.getroot()
    files = []
    for fileTag in root.findall('file'):  # checking each element and its attributes, setting status
        file = FileToProcess()
        attribs = dict(fileTag.attrib)
        if "source_path" in attribs.keys():
            file.source = attribs["source_path"]
            if not os.path.exists(file.source):
                file.status = FileStatus.INVALID_SOURCE
                files.append(file)
                continue
        else :
            file.status = FileStatus.MISSING_SOURCE_IN_XML
            files.append(file)
            continue
        if "destination_path" in attribs.keys():
            file.destination = attribs["destination_path"]
            if not os.path.exists(file.destination):
                file.status = FileStatus.INVALID_DESTINATION
                files.append(file)
                continue
        else :
            file.status = FileStatus.MISSING_DESTINATION_IN_XML
            files.append(file)
            continue
        if "file_name" in attribs.keys():
            file.filename = attribs["file_name"]
            if not os.path.isfile(file.source+PATH_SEPARATOR+file.filename):
                file.status = FileStatus.MISSING_FILE
                files.append(file)
                continue
        else :
            file.status = FileStatus.MISSING_FILENAME_IN_XML
            files.append(file)
            continue
        file.status = FileStatus.OK
        files.append(file)
    return files

def copyFiles(XmlFile):
    files = xmlRead(XmlFile)
    for i in range(len(files)):
        if not files[i].status == FileStatus.OK:
            print ("Unable to copy file №"+ str(i+1) + " " + files[i].status.name)
            continue
        fullSourcePath = files[i].source + PATH_SEPARATOR + files[i].filename
        fullDestinationPath = files[i].destination + PATH_SEPARATOR + files[i].filename
        try:
            shutil.copyfile(fullSourcePath,fullDestinationPath)
        except IOError as e:
            sys.exit(e)
        except  shutil.SameFileError as e:
            sys.exit(e)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ("Invalid number of arguments")
        sys.exit()
    copyFiles(sys.argv[1])
