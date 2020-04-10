# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# #-----3-----
# #Write a class to represent date (day, month, year).
# Don’t use datetime module. Implement #comparison operator
# for equality and hash function for instances of this class.

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        if not self.is_valid_date(self.year, self.month, self.day):
            raise ValueError

    def __str__(self) -> str:
        return f"{self.year}-{self.month}-{self.day}"

    def __repr__(self) -> str:
        return f"Date({self.year}, {self.month}, {self.day})"

    def __eq__(self, other) -> bool:
        return self.year == other.year and \
               self.month == other.month and \
               self.day == other.day

    def __hash__(self) -> int:
        return hash((self.year, self.month, self.day))

    @staticmethod
    def is_valid_date(year, month, day) -> bool:
        day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day_count_for_month[2] = 29
        return 1 <= month <= 12 and 1 <= day <= day_count_for_month[month]


date = Date(30, 12, 2030)
print(date)
# date2 = Date(36, 13, 2030)
# print(date2)
