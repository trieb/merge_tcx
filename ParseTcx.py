import timeit
from collections import namedtuple
try:
    import xml.etree.cElementTree as xml
except:
    import xml.etree.cElementTree as xml


ns = {'role': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}

TrackPoint = namedtuple('TrackPoint', 'Time HeartRateBpm AltitudeMeters DistanceMeters Cadence')

class ParseTcx:
    def __init__(self, file):
        self.file = file;
        self.root             = None
        self.Sport            = None
        self.StartTime        = None
        self.TotalTimeSeconds = None
        self.DistanceMeters   = None
        self.Calories         = None
        self.AverageHeartRate = None
        self.MaximumHeartRate = None
        self.Intensity        = None
        self.Cadence          = None
        self.TriggerMethod    = None
        self.TrackPoints      = []

    def parse(self):
        tree = xml.parse(self.file)
        self.root = tree.getroot()
        self.parse_root(self.root)

    def get_info(self):
        print('Sport: ', self.Sport)
        print('StartTime: ', self.StartTime)
        print('Duration: ', float(self.TotalTimeSeconds)/60, ' [minutes]')
        print('Distance: ', self.DistanceMeters, ' [meters]')
        print('Average HeartRate: ', self.AverageHeartRate, ' [BPM]')

    def get_text(self, item, name, default=None):
        try:
            return item.find(self.get_role(name)).text
        except:
            return default

    def get_role(self, role):
        return '{' + ns['role'] + '}' + role

    def parse_root(self, root):
        #print(root.tag, root.attrib)
        for child in root:
            if child.tag == self.get_role('Activities'):
                self.parse_activities(child)

    def parse_activities(self, actitivities):
        #print(actitivities.tag, actitivities.attrib)
        for child in actitivities:
            if child.tag == self.get_role('Activity'):
                self.parse_activity(child)

    def parse_activity(self, actitivity):
        #print(actitivity.tag, actitivity.attrib)
        self.Sport = actitivity.attrib['Sport']
        for child in actitivity:
            if child.tag == self.get_role('Lap'):
                self.parse_lap(child)

    def parse_lap(self, lap):
        #print(lap.tag, lap.attrib)
        self.get_lap_info(lap)
        for child in lap:
            if child.tag == self.get_role('Track'):
                for point in child.findall('role:Trackpoint', ns):
                    Time           = self.get_text(point, 'Time')
                    hr = point.find('role:HeartRateBpm', ns)
                    HeartRateBpm   = self.get_text(hr, 'Value')
                    AltitudeMeters = self.get_text(point, 'AltitudeMeters')
                    DistanceMeters = self.get_text(point, 'DistanceMeters')
                    Cadence        = self.get_text(point, 'Cadence')
                    trackpoint = TrackPoint(Time, HeartRateBpm, AltitudeMeters, DistanceMeters, Cadence)
                    self.TrackPoints.append(trackpoint)

    def get_lap_info(self, lap):
        self.StartTime = lap.attrib['StartTime']
        self.TotalTimeSeconds = self.get_text(lap, 'TotalTimeSeconds')
        self.DistanceMeters   = self.get_text(lap, 'DistanceMeters')
        self.Calories         = self.get_text(lap, 'Calories')
        self.AverageHeartRate = self.get_text(lap, 'AverageHeartRate')
        self.MaximumHeartRate = self.get_text(lap, 'MaximumHeartRate')
        self.Intensity        = self.get_text(lap, 'Intensity')
        self.Cadence          = self.get_text(lap, 'Cadence')
        self.TriggerMethod    = self.get_text(lap, 'TriggerMethod')


if __name__ == "__main__":

    file = 'Data/file_with_heartrate_data.tcx'
    tcx = ParseTcx(file)
    tcx.parse()
    tcx.get_info()