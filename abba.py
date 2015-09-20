def isPattern(mystr, pattern, matches):
	if len(pattern) == 1:
		if pattern not in matches or matches[pattern] == mystr:
			matches[pattern] = mystr
			return True
		return False

	maxMatchLen = len(mystr) - len(pattern) + 1
	for i in range(1,maxMatchLen+1):
		proposedMatch = mystr[:i]
		if pattern[0] in matches and matches[pattern[0]] != proposedMatch:
			continue
		matches[pattern[0]] = proposedMatch
		ret = isPattern(mystr[i:], pattern[1:], matches)
		if ret == True:
			return True
		if pattern[0] in matches:
			del matches[pattern[0]] 
	return False

def main():
	mystr = 'redblueredblue'
	pattern = 'abab'
	print("%s - %s - %s"%(mystr, pattern, isPattern(mystr, pattern, {})))

main()