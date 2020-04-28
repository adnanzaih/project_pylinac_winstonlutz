#pip install pylinac

from pylinac import WinstonLutz

my_directory = 'N:/MedicalPhysics/Quality Control Program/Treatment/Weekly/Winston-Lutz/Unit 01/2020_04_28/Z20190814'
wl = WinstonLutz(my_directory)

#results
# plot all the images
wl.plot_images()
print(wl.bb_shift_instructions())
# print to PDF
wl.publish_pdf('u6.pdf')

