from MergeTcx import MergeTcx
from ParseTcx import ParseTcx

# 1) Add new files to Config.py
# 2) Add date to 'date' below
# 3) Run script!

merged = MergeTcx('2016-02-01')
tcx = ParseTcx(merged.file_name)
tcx.parse()
tcx.plot_signal('HeartRateBpm')



