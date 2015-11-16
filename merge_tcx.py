from ParseTcx import ParseTcx

G920XT_tcx_file = 'Data/file_with_heartrate_data.tcx'
tacx_tcx_file = 'Data/file_without_heartrate_data.tcx'

# Parse data from the Tacx Trainer
tcx_tacx = ParseTcx(tacx_tcx_file)
tcx_tacx.parse()
tcx_tacx.get_info()

# Parse data from the Garmin 920XT
tcx_920XT = ParseTcx(G920XT_tcx_file)
tcx_920XT.parse()
tcx_920XT.get_info()

