import shutil, os, sys, re

def removeAlphaDirs(fnD, dictVals):
	return [value for value in fnD if value not in dictVals]

def chooseAlphaDir(fileName, filePath):
	if fileName[0].lower() in dirs["a-d"]:
		print("moving "+ fileName+" to a-d")
		moveAndCreateDir(filePath, os.path.join(inDir, "a-d"))
	elif fileName[0].lower() in dirs["e-h"]:
		print('moving '+fileName+' to e-h')
		moveAndCreateDir(filePath, os.path.join(inDir, "e-h"))
	elif fileName[0].lower() in dirs["i-l"]:
		print('moving '+fileName+' to i-l')
		moveAndCreateDir(filePath, os.path.join(inDir, "i-l"))
	elif fileName[0].lower() in dirs["m-p"]:
		print('moving '+fileName+' to m-p')
		moveAndCreateDir(filePath, os.path.join(inDir, "m-p"))
	elif fileName[0].lower() in dirs["q-t"]:
		print('moving '+fileName+' to q-t')
		moveAndCreateDir(filePath, os.path.join(inDir, "q-t"))
	elif fileName[0].lower() in dirs["u-w"]:
		print('moving '+fileName+' to u-w')
		moveAndCreateDir(filePath, os.path.join(inDir, "u-w"))
	elif fileName[0].lower() in dirs["x-z"]:
		print('moving '+fileName+' to x-z')
		moveAndCreateDir(filePath, os.path.join(inDir, "x-z"))

def moveAndCreateDir(src, dst):
	if os.path.isdir(dst) == False:
		os.makedirs(dst)
	shutil.move(src, dst)


inDir = str(sys.argv[1])
if os.path.isdir(inDir) == False:
	sys.exit("That doesn't look like a valid file path...")
else:
	print("checking "+inDir)

filesAndDirs = os.listdir(inDir)

dirs = {
	"a-d": ['a','b','c','d'],
	"e-h": ['e','f','g','h'],
	"i-l": ['i','j','k','l'],
	"m-p": ['m','n','o','p'],
	"q-t": ['q','r','s','t'],
	"u-w": ['u','v','w'],
	"x-z": ['x','y','z']
}

filesAndDirs = removeAlphaDirs(filesAndDirs, dirs)

for f in filesAndDirs:
	chooseAlphaDir(f, os.path.join(inDir, f))
