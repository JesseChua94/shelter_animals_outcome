import dogGroups as dg

def hasName(x):
        if isinstance(x, str):
            return 1
        return 0
    
def intact(x):
    x = x.lower()
    if x == "unknown":
        return 0
    if ("spayed" in x or "neutered" in x):
        return -1
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
    if x[1] == "years":
        return x[0] / 12
    if x[1] == "weeks":
        return x[0] / 4
    if x[1] == "days":
        return x[0] / 30
    return x[0]

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