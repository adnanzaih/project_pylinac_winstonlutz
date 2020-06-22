from pylinac import WinstonLutz


my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/WL Data/Unit 01/2020_02_19' #unit 3
#my_directory = '/Users/adnanhafeez/Downloads/2020_05_22/QA Winston-Lutz U6' #downloads
#my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/WL Data/Unit 06/2019_10_07/Z20150323'
wl = WinstonLutz(my_directory)

wl.plot_images()
wl.save_images('test.png')
print(wl.results())
print("----------------------------------------------------------------------------------")
print(wl.plot_deltas()["G0C90T315 x delta"])