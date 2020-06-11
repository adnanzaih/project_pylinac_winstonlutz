#pip install pylinac

from pylinac import WinstonLutz

from adnan.adnan import adnan_code

my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/WL Data/u6/2020_03_16/Z20150323'
wl = WinstonLutz(my_directory)

#results
# plot all the images
#wl.plot_images()
print(wl.bb_shift_instructions())
# print to PDF
wl.publish_pdf('Report.pdf')

# print(wl.adnan_test())

# print(adnan_code())
