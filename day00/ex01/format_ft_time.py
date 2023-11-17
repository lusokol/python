from datetime import date
import time

today = date.today()

print ("Seconds since January 1, 1970: " + '{:,.4f}'.format(time.time()) + " or " + '{:.2e}'.format(time.time()) + " in scientific notation")
print (today.strftime("%b %d %Y"))