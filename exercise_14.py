"""14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days"""

import datetime
x=(datetime.date(2014,7,11)-datetime.date(2014,7,2))
print('{} days'.format(x.days))
