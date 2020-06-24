from pylinac import WinstonLutz


my_directory = '/Users/adnanhafeez/Downloads/Z20130715'
#my_directory = "/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/WL Data/Unit 06/2020_01_27/U6/WL/Z20150323"
wl = WinstonLutz(my_directory)

wl.plot_images()
print(wl.results())
print("----------------------------------------------------------------------------------")
#print(wl.plot_deltas()["G0C90T315 x delta"])