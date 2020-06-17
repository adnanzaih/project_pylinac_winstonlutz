from pylinac import WinstonLutz



my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/WL/2020_01_27/U6/WL/Z20150323'
wl = WinstonLutz(my_directory)

print((wl.plot_deltas()).keys())