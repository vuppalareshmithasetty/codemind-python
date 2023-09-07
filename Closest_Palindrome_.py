def isPalindrome(n):
	for i in range(len(n) // 2):
		if (n[i] != n[-1 - i]):
			return False
	return True
def convertNumIntoString(num):
	Snum = str(num)
	return Snum
def closestPalindrome(num):
	bNum = num - 1
	while (not isPalindrome(convertNumIntoString(abs(bNum)))):
		bNum -= 1
	aNum = num + 1
	while (not isPalindrome(convertNumIntoString(aNum))):
		aNum += 1
	if (abs(num - bNum) > abs(num - aNum)):
		return aNum
	elif (abs(num - bNum) < abs(num - aNum)):
		return bNum
	else:
	    c = str (bNum) +" "+ str (aNum)
	    return c
num = int(input())
print(closestPalindrome(num))