# Treadmill_run_distance_adjuster
If you are using your SmartWatch (e.g. Garmin watch) while running on treadmill, you will see there is a discrepancy between the distance shown on the treadmill and the distance on your smartwatch. The running activity .tcx file can be exported/downloaded from the online smartwatch webpage (i.e. Garmin Connect) or exported from Strava. 
After running the python code, in the opened file selector window, chose your running activity .tcx file. Then in the input area of python interpreter enter the correct distance (shown on the treadmill) and the wrong distance (shown on the watch). 
The pace-adjusted activity .tcx file will be saved with the same file name and added "corrected.tcx" in the same folder. You can re-upload the corrected activity to Strava, etc. 

-Code by AZangiabadi 
Dec. 2022
