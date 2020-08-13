from pylinac import WinstonLutz

wl = WinstonLutz.from_zip('/Users/adnanhafeez/Downloads/QA Winston-Lutz U9.zip')

for k, v in (wl.plot_deltas()).items():
    print("{}: {}mm".format(k, v))

wl.publish_pdf("report.pdf", wl)
