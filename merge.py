from ParseTcx import ParseTcx
import os.path

from xml.etree.cElementTree import ElementTree
from xml.etree.cElementTree import Element
import xml.etree.cElementTree as etree

ns = {'role': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}

base_path = 'C:\\Users\\mikael\\Google Drive\\Träning\\Tacx\\Tcx combine\\'

# 2015-11-06
#date = '2015-11-06'
#tacx = 'BRA 14 - Full course_20151106.tcx'
#garmin = 'activity_949025308.tcx'

# 2015-11-14
date = '2015-11-14'
tacx = 'BRA 14 - Full course2015-11-14.tcx'
garmin   = 'activity_957021924.tcx'

# 2015-11-17
#date = '2015-11-17'
#tacx = 'BRA 14 - Full course(3).tcx'
#garmin = 'activity_959578204.tcx'

tacx_tcx_file = os.path.join(base_path, date, tacx)
hr_tcx_file = os.path.join(base_path, date, garmin)
merged_file = date + '.tcx'

def create_heartrate(hr):
    heart_rate = Element('HeartRateBpm')
    value = Element('Value')
    value.text = hr
    heart_rate.append(value)
    return heart_rate

def parse_file(file):
    # Parse data from the Tacx Trainer
    tcx  = ParseTcx(file)
    tcx.parse()
    tcx.get_info()
    return tcx

tacx_tcx = parse_file(tacx_tcx_file)
hr_tcx = parse_file(hr_tcx_file)

for tp in tacx_tcx.dom_trackpoints:
    timestamp = tp.find('role:Time', ns).text
    timestampKey = timestamp[0:19]
    if timestampKey in hr_tcx.TrackPoints.keys():
        heartrate_from_other_file = hr_tcx.TrackPoints[timestampKey].HeartRateBpm
        if heartrate_from_other_file is not None:
            hr_node = create_heartrate(heartrate_from_other_file)
            tp.append(hr_node)

tree = ElementTree(tacx_tcx.root)
tree.write(open(merged_file, 'wb'), encoding="utf-8", xml_declaration=True)


# Add UGLY! temporary fix for namespace "ns1-issue"

f = open (merged_file, "r")
data=f.read()
data = data.replace('ns1:TPX', 'TPX')
data = data.replace('ns1:Speed', 'Speed')
data = data.replace('ns1:Watts', 'Watts')
f.close

f = open(merged_file, "w")
f.write(data)
f.close()
