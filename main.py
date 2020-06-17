from pylinac import WinstonLutz



my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/WL Data/u3/2019_11_29/QA Winston-Lutz U3'
wl = WinstonLutz(my_directory)

wl.plot_images()
print(wl.results())
print(wl.plot_deltas())