#pip install pylinac

from pylinac import WinstonLutz

my_directory = '/Users/adnanhafeez/Documents/TBCC Work/PyLinac Project/Data/WL Data/u3/2020_02_19/QA Winston-Lutz U3'
wl = WinstonLutz(my_directory)

#results
# plot all the images
#wl.plot_images()
print(wl.bb_shift_instructions())
# print to PDF
wl.publish_pdf('test.pdf')

