from pylinac import WinstonLutz


my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/WL/WL Data/Unit 03/2019_11_29/QA Winston-Lutz U3' #unit 3
#my_directory = '/Users/adnanhafeez/Downloads/2020_05_22/QA Winston-Lutz U6' #downloads
#my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/WL Data/Unit 06/2019_10_07/Z20150323'
wl = WinstonLutz(my_directory)

wl.plot_images()
print(wl.results())
#print(wl.plot_deltas())