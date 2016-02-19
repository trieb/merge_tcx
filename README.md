# merge_tcx

This script was develop with the very specific purpose of merging HeartRate data from one .tcx-file into another .tcx-file.

However...
The class **ParseTcx.py** is a generic class that can parse any .tcx-file.
This can be very useful if one would like to use Python to analyze the data in one way or another.

## Background
I use a Tacx Bushido trainer and a Garmin 920XT. I get almost all the data collected in the files that
are exported from the Tacx Cycling App, but since my HeartRate monitor only connects to my watch (Garmin 920XT)
a need to merge that data into the file from the Tacx Cycling App.

## Usage
 Edit: Config.py
```python
# Add .tcx file from the Tacx trainer and your Garmin device to a new row
...
config['2016-02-18'] = Session('BRH-16-Full course(6).tcx', 'activity_1055207164.tcx')
config['2016-02-09'] = Session('BRH - 17 - Full course(1).tcx', 'activity_1045149528.tcx')
...
```
Edit: run.py
```python
# 1) Add current date to MergeTcx('date')
# 2) Run run.py

merged = MergeTcx('2016-02-01')
tcx = ParseTcx(merged.file_name)
tcx.parse()
tcx.plot_signal('HeartRateBpm')
```
This will give you a new file `2016-02-01_merged.txt` with to original .tcx from the trainer merged with HeartBeatData from your Garmin device. 

# Upload to Strava
Goto: https://www.strava.com/login to upoad the merged file.
