import fileinput
import datetime
import itertools

def parseInput(line):
	dateAsList = line.split("/")
	a,b,c = dateAsList
	# Convert to ints for convenience/speed
	ai,bi,ci = int(dateAsList)
	int(dateAsList)
	#ai = int(a)
	#bi = int(b)
	#ci = int(c)
	
	# Check for obvious illegality
	#if ai > 12 and bi > 12 and ci > 12
	#	return outputFormat(datetime.date(ai, bi, ci), line, True)
	
	# Create list of all possible permutations
	dateList = list()
	dateList.append([ai,bi,ci])
	dateList.append([bi,ci,ai])
	dateList.append([ci,bi,ai])
	dateList.append([bi,ai,ci])
	dateList.append([ci,ai,bi])
	dateList.append([ai,ci,bi])
	
	filteredDateList = list()
	
	for possibleDates in dateList:
		try:
			datetime.date()
			datetime.date(possibleDates[0], possibleDates[1], possibleDates[2])
			filteredDateList.append(
		except ValueError:
			continue
	
	#dateList0 = [ai,bi,ci]
	#dateList1 = [bi,ci,ai]
	#dateList2 = [ci,bi,ai]
	#dateList3 = [bi,ai,ci]
	#dateList4 = [ci,ai,bi]
	#dateList5 = [ai,ci,bi]	
		
	#Skip all that do the following:
	# 1. put all combinations in a map key -> arrayList (there should only be six, look up how to map)
	# 2. iterate over map try parse first, then check for legality and remove if fails (look up error handling)
	# 3. iterate over map again to find smallest date
	
	finalDate = datetime.date(int(a), int(b), int(c))
	return outputFormat(finalDate, line, False)

def isLegalDate(date):
	maxDate = datetime.date(2999, 12, 31)
	minDate = datetime.date(2000, 1, 1)
	
	if date > maxDate:
		return False
	elif date < minDate:
		return False
	else:
		return True

def outputFormat(date, originalDate, isIllegal):
	if isIllegal:
		return date.strftime("%Y-%m-%d")
	else:
		return "%s is illegal" % originalDate

# Read in the file (defaults to stdin per exercise params)
for line in fileinput.input():
	print parseInput(line)