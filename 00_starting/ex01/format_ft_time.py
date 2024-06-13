import datetime

dt = datetime.datetime.now()
seconds = dt.timestamp()


print('Seconds since January 1, 1970:', seconds, ' or ', "{:e}".format(seconds), ' in scientific notation')
print (dt.strftime("%B"), dt.day, dt.year)