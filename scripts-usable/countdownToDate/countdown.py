# Countdown script that accepts date in format
#					dd <Month> yyyy [hh:mm]
#							[]: optional
# and counts down from current day to given date

import datetime, sys, re, time, math, os
from datetime import date

dates = {
	"January": 1, "Jan": 1,
	"February": 2, "Feb": 2,
	"March": 3, "Mar": 3,
	"April": 4, "Apr": 4,
	"May": 5,
	"June": 6, "Jun": 6,
	"July": 7, "Jul": 7,
	"August": 8, "Aug": 8,
	"September": 9, "Sep": 9,
	"October": 10, "Oct": 10,
	"November": 11, "Nov": 11,
	"December": 12, "Dec": 12
}

if len(sys.argv) > 1:
	args = sys.argv
	today = time.time()
	for i in range(1, len(args)):
		if args[i].isnumeric():
			if len(args[i]) == 4:
				year = int(args[i])
			elif len(args[i]) < 3 and len(args[i]) > 0:
				day = int(args[i])
		if args[i].isalpha():
			try:
				month = dates[args[i].capitalize()]
			except:
				print("Please use full date or three-letter equivalent...")
				exit()
		if ":" in args[i] or "h" in args[i]:
			hm = re.split("[:h]", args[i])
			if int(hm[0]) <= 23 and int(hm[1]) <= 59:
				hour = int(hm[0])
				minutes = int(hm[1])
			else:
				print("That's not correct. Don't waste my time...")

	try:
		hour
		minutes
	except:
		try:
			until = datetime.datetime(year, month, day).timestamp()
		except:
			print("You have to give me more information...")
			exit()
	else:
		until = datetime.datetime(year, month, day, hour, minutes).timestamp()

	diff = until - today

	while diff:
		try:
			print(datetime.timedelta(seconds=math.floor(diff)), end='\r')
			time.sleep(1)
			diff -= 1
		except KeyboardInterrupt:
			print('Stopping the countdown...')
			try:
				sys.exit(0)
			except SystemExit:
				os._exit(0)

