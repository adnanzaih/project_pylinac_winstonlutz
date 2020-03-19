#pip install pylinac

from pylinac import WinstonLutz

my_directory = 'N:/MedicalPhysics/Quality Control Program/Treatment/Weekly/Winston-Lutz/Unit 01/2020_03_16/Z20190814'
wl = WinstonLutz(my_directory)

#results
# plot all the images
wl.plot_images()
# print to PDF
wl.publish_pdf('mywl.pdf')