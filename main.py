from entries import lottoEntry
from results import lottoResult
from filehandler import checkEmpty, folderScanner, fileCheck
import concurrent.futures

def matchedNum(lst1, lst2):
    """checking how many numbers are matched. from entry to result,
    ballsets only"""
    n = 0
    for i in lst1:
        if i in lst2:
            n += 1
    return(n)

def matchedSub(lst1, lst2):
    """check if the additional numbers are matching"""
    m = 0
    i = 0
    while i != len(lst2):
        if lst1[i] == lst2[i]:
            m += 1
        i += 1
    return(m)

def compare(entryFile, results):
    """main matching loop, loop through the entry file to match entry to
    result one by one, and write into the matched.csv file one by one"""
    strings = entryFile.split(".")
    if fileCheck(strings[0], results):
        file = open(f"srcs/{entryFile}", "r")
        resFile = open(f"srcs/{strings[0]} result.csv", 'r')
        res = lottoResult(resFile)
        resFile.close()
        f = open(f"{strings[0]} matched.csv", "a")
        if checkEmpty(f"{strings[0]} matched.csv"):
            f.write(f"ticket_id;balls_matched;additional_balls_matched;jackpot  \n")
        while file:
            entry = lottoEntry(file)
            jackpot = False
            n = matchedNum(entry.ballset, res.ballset)
            if n == len(entry.ballset):
                jackpot = True
            s = matchedSub(entry.additionals, res.additionals)
            final = f"{entry.ID};{n};{s}"
            if jackpot:
                final = final + ";jackpot\n"
            else:
                final = final + "\n"
            f.write(final)
        file.close()
        f.close()
    else:
        print(f"no result file for {entryFile}")

if __name__ == "__main__":
    """main loop, make threads for each entry file, so the matching loop
    for each file can run concurrently"""
    results, entries = folderScanner()
    for entryFile in entries:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(compare, entryFile, results)