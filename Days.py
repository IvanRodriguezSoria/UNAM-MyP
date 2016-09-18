import calendar
import math

class Days():

	def __init__(self):
		self.pre_sum = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
	
	def days_in_years(self, year):
		year_leap = year + math.ceil(year / 4) - math.ceil(year / 100) + math.ceil((year - 100) / 400)
		result = 365 * year_leap
		return result

	def days_in_months(self, year, month, days):
		year = self.days_in_years(year)
		if calendar.isleap(year) and month > 2:
			return self.pre_sum[month - 1] + days + 1 
		return self.pre_sum[month - 1] + days

	def days_in_date(self, year_1, month_1, day_1, year_2, month_2, day_2):
		firts_date_days = self.days_in_months(year_1, month_1, day_1)
		second_date_days = self.days_in_months(year_2, month_2, day_2)
		return second_date_days - firts_date_days

if __name__ == '__main__':
	first_date = input()
	second_date = input()
	first = first_date.split()
	second = second_date.split()
	d = Days()
	print(d.days_in_date(int(first[0]), int(first[1]), int(first[2]), int(second[0]), int(second[1]), int(second[2]) ) )