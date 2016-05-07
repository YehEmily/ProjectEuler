days_dict = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}

def days(month, year):
	"""Computes the number of days in each month."""
	if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
		days = 31
		return days
	elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
		days = 30
		return days
	elif (month == 2):
		if year % 4 == 0:
			if year % 100 != 0:
				if year % 400 == 0:
					days = 29
					return days
				else:
					days = 28
					return days
			days = 29
			return days
		else:
			days = 28
			return days

def sundays():
	"""Counts the number of Sundays."""
	counter = 1
	tally = 0
	for year in range(1901, 2001):         
		for month in range(1, 13):
			x = days(month, year)
			for month_days in range(1, (x + 1)):
				counter += 1
				if (month_days == 1) and days_dict[counter] == "Sunday":
					tally += 1
				if counter >= 7: # Days of the week
					counter = 0
	return tally

print sundays()