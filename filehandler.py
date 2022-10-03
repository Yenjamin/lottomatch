import os

def checkEmpty(path):
    """check if the file is empty, for putting in the heading lines in 
    matched.csv"""
    return os.stat(path).st_size==0

def folderScanner():
    """scan the whole srcs folder and return lists of entry files and result files"""
    results = []
    entries = []
    for root, dirs, files in os.walk("srcs"):
        for fn in files:
            if fn.split(".")[1] == "csv":
                if "result" in fn:
                    results.append(fn)
                else:
                    entries.append(fn)
    return(results, entries)

def fileCheck(name, results):
    """check if the entry file has a corresponding result file"""
    for res in results:
        if name in res:
            return True
    return False