import dogGroups as dg
import datetime as dt
import re

def hasName(x):
        return 2 if isinstance(x, str) else -1

def getNameLength(x):
    return len(x) if isinstance(x, str) else -1

def getColourLength(x):
    return len(re.findall(r"[\w]+", x))

def convertAnimalType(x):
    if x.lower() == 'cat':
        return 1
    if x.lower() == 'dog':
        return -1
    return 0

def timeToYear(x):
    return getDateTimeObject(x).year

def timeToSeason(x):
    seasons = [1,1,1,2,2,2,3,3,3,4,4,4]
    return seasons[monthOfYear(x) - 1]

def dayOfWeek(x):
    return getDateTimeObject(x).day

def monthOfYear(x):
    return getDateTimeObject(x).month
    
def timeToHourOfDay(x):
    return getDateTimeObject(x).hour

def getDateTimeObject(x):
    return dt.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    
def intact(x):
    x = x.lower()
    if x == "unknown":
        return 0
    if ("spayed" in x or "neutered" in x):
        return 3
    return 1

def gender(x):
    if "Male" in x:
        return 1
    if "Female" in x:
        return -1
    return 0

def convertAgeToMonths(x):
    x = x.split()
    x[0] = int(x[0])
    if len(x) == 1:
        return -1
    if "year" in x[1]:
        return x[0] * 12
    if "week" in x[1]:
        return x[0] / 4
    if "day" in x[1]:
        return x[0] / 30
    return x[0]

def convertAgeToWeeks(x):
    x = x.split()
    x[0] = int(x[0])
    if len(x) == 1:
        return -1
    if "year" in x[1]:
        return x[0] * 48
    if "month" in x[1]:
        return x[0] * 4
    if "day" in x[1]:
        return x[0] / 7
    return x[0]

def convertAgeToYears(x):
    x = x.split()
    x[0] = int(x[0])
    if len(x) == 1:
        return -1
    if "month" in x[1]:
        return x[0] / 12
    if "week" in x[1]:
        return x[0] / 48
    if "day" in x[1]:
        return x[0] / 365
    return x[0]

def convertAgeToDays(x):
    x = x.split()
    x[0] = int(x[0])
    if len(x) == 1:
        return -1
    if "month" in x[1]:
        return x[0] * 30
    if "week" in x[1]:
        return x[0] * 7
    if "year" in x[1]:
        return x[0] * 365
    return x[0]

def isYoung(x):
    if int(x) < 10:
        return 1
    return -1

def isShihTzu(x):
    return 1 if "Shih Tzu" in x else 0

def isAggressive(x):
    aggressive = ["rottweiler", "pit", "bull", "siberian", "husky"]
    return 1 if any(match in x.lower() for match in aggressive) else 0

def isMix(x):
    return 1 if "mix" in x.lower() else 0

#Dog groups. Column for each where 0 is unknown or cat.
#NOTE: Should try to condense this if possible since all using same statement.
def isTerrier(x):
    return 1 if any(match in x.lower() for match in dg.dogGroups['terrier']) else 0
def isToy(x):
    return 1 if any(match in x.lower() for match in dg.dogGroups['toy']) else 0
def isWorking(x):
    return 1 if any(match in x.lower() for match in dg.dogGroups['working']) else 0
def isSporting(x):
    return 1 if any(match in x.lower() for match in dg.dogGroups['sporting']) else 0
def isHound(x):
    return 1 if any(match in x.lower() for match in dg.dogGroups['hound']) else 0
def isNonSporting(x):
    return 1 if any(match in x.lower() for match in dg.dogGroups['nonSporting']) else 0
def isHerding(x):
    return 1 if any(match in x.lower() for match in dg.dogGroups['herding']) else 0

def isShortHair(x):
    return 1 if "short" in x.lower() else 0
def isMediumHair(x):
    return 1 if "medium" in x.lower() else 0
def isLongHair(x):
    return 1 if "long" in x.lower() else 0

# Most of the multicolour names contain a forward slash aside a few exceptions such as
# the unique cat coats e.g. calico and tortie.
def isMultiColour(x):
    multiColour = ["calico", "tortie", "torbie", "tricolor", "/"]
    return 1 if any(match in x.lower() for match in multiColour) else 0

def isTabby(x):
    return 1 if "tabby" in x.lower() else 0