import fileinput
import datetime 

def parseInput(line):
	a,b,c = line.split("/")
	
	finalDate = datetime.date(int(a), int(b), int(c))
	return outputFormat(finalDate, line)

def isLegalDate(date):
	maxDate = datetime.date(2999, 12, 31)
	minDate = datetime.date(2000, 1, 1)
	
	if date > maxDate:
		return False
	elif date < minDate:
		return False
	else:
		return True

def outputFormat(date, originalDate):
	if isLegalDate(date):
		return date.strftime("%Y-%m-%d")
	else:
		return "%s is illegal" % originalDate

# Read in the file (defaults to stdin per exercise params)
for line in fileinput.input():
	print parseInput(line)