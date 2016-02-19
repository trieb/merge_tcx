from collections import namedtuple

Session = namedtuple('Session', ['tacx_file', 'garmin_file'])

config = dict()

config['2016-02-18'] = Session('BRH-16-Full course(6).tcx', 'activity_1055207164.tcx')
config['2016-02-09'] = Session('BRH - 17 - Full course(1).tcx', 'activity_1045149528.tcx')
config['2016-02-03'] = Session('BRA 14 - Full course(12).tcx', 'activity_1037689688.tcx')
config['2016-02-01'] = Session('2016-02-01-BRH - 16.tcx', 'activity_1035478057.tcx') # Dubbelkolla!
config['2016-01-28'] = Session('BRH - 16 - Full course(1).tcx', 'activity_1030276897.tcx')
config['2016-01-21'] = Session('BRA 14 - Full course(10).tcx', 'activity_1022578289.tcx')
config['2016-01-15'] = Session('BRA 14 - Full course(8).tcx', 'activity_1015621878.tcx')
config['2016-01-07'] = Session('BRA 14 - Full course(11).tcx', 'activity_1006636813.tcx')
config['2016-01-02'] = Session('BRA 14 - Full course(6).tcx', 'activity_1000222103.tcx')
config['2015-12-23'] = Session('BRA 14 - Full course(5).tcx', 'activity_990289774.tcx')
config['2015-12-09:2'] = Session('BRA 14_2015-12-09.tcx', 'activity_978388430.tcx') # Dubbelkolla!
config['2015-12-09:1'] = Session('Fitness Test Astrand 180 watt-2015-12-09.tcx', 'activity_978388430.tcx')
config['2015-11-17'] = Session('BRA 14 - Full course(3).tcx', 'activity_959578204.tcx')
config['2015-11-14'] = Session('BRA 14 - Full course2015-11-14.tcx', 'activity_957021924.tcx')
config['2015-11-06'] = Session('BRA 14 - Full course_20151106.tcx', 'activity_949025308.tcx')
