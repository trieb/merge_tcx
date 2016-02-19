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
```python
tcx_tacx = ParseTcx('my_file.txt')
tcx_tacx.parse()
tcx_tacx.get_info()
```

# Upload to Strava
Goto: https://www.strava.com/login to upoad the merged file.