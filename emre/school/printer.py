class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printText(text):
    print(bcolors.OKBLUE + text + bcolors.ENDC)


def printInfo(text):
    print(bcolors.OKGREEN + text + bcolors.ENDC)

def printPurple(text):
    print(bcolors.OKCYAN + text + bcolors.ENDC)

def printError(error):
    print(bcolors.FAIL + error + bcolors.ENDC)


def printWARNING(warning):
    print(bcolors.WARNING + warning + bcolors.ENDC)
def printList(value:str,objList:[]):
        for s in objList:
            s.writer()



if __name__ == "__main__":
    print()
