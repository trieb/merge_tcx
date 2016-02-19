from ParseTcx import ParseTcx
import os.path
import Config

from xml.etree.cElementTree import ElementTree
from xml.etree.cElementTree import Element
import xml.etree.cElementTree as etree

ns = {'role': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}
base_path = 'C:\\Users\\mikael\\Google Drive\\Träning\\Tacx\\Tcx combine\\'


class MergeTcx:
    def __init__(self, date):
        self.date = date
        try:
            garmin = Config.config[date].garmin_file
            tacx = Config.config[date].tacx_file
            self.tacx_tcx_file = os.path.join(base_path, date, tacx)
            self.hr_tcx_file = os.path.join(base_path, date, garmin)
            self.file_name = None
            self._create_out_file()
            self.merge()
        except:
            print('Check that .tcx files were added to Config.py!')


    def _create_heartrate(self, hr):
        heart_rate = Element('HeartRateBpm')
        value = Element('Value')
        value.text = hr
        heart_rate.append(value)
        return heart_rate

    def _parse_file(self, file):
        tcx = ParseTcx(file)
        tcx.parse()
        tcx.get_info()
        return tcx

    def _create_out_file(self):
        file_name = self.date + '_merged.tcx'
        self.file_name = os.path.join(base_path, self.date, file_name)

    def merge(self):
        last_hr = 0
        self.tacx_tcx = self._parse_file(self.tacx_tcx_file)
        self.hr_tcx = self._parse_file(self.hr_tcx_file)

        for tp in self.tacx_tcx.dom_trackpoints:
            timestamp = tp.find('role:Time', ns).text
            timestamp_key = timestamp[0:19]
            if timestamp_key in self.hr_tcx.TrackPoints.keys():
                heartrate_from_other_file = self.hr_tcx.TrackPoints[timestamp_key].HeartRateBpm
                if heartrate_from_other_file is not None:
                    hr_node = self._create_heartrate(heartrate_from_other_file)
                    tp.append(hr_node)
                    last_hr = heartrate_from_other_file
            else:
                hr_node = self._create_heartrate(last_hr)
                tp.append(hr_node)

        tree = ElementTree(self.tacx_tcx.root)

        tree.write(open(self.file_name, 'wb'), encoding="utf-8", xml_declaration=True)

        # Add UGLY! temporary fix for namespace "ns1-issue"
        f = open (self.file_name, "r")
        data = f.read()
        data = data.replace('ns1:TPX', 'TPX')
        data = data.replace('ns1:Speed', 'Speed')
        data = data.replace('ns1:Watts', 'Watts')
        f.close

        f = open(self.file_name, "w")
        f.write(data)
        f.close()
        return self.file_name
