import subprocess
import time
import cleaner 
import publisher
import recorder
import os

CURRENT_FOLDER = '/home/pi/Documents/noise-meter/'
CURRENT_TIME = str(time.time())
SOUND_METER_TIME = 60*5

recorder.record(CURRENT_TIME)

#push recording to s3
publisher.push_recordings()
publisher.push_logs()

cleaner.remove_files_in_directory("recordings")
cleaner.remove_files_in_directory("logs")

cmd = 'soundmeter -t 3000 50 -a exec-stop --exec /home/pi/Documents/noise-meter/noise_record.sh --log ' + CURRENT_FOLDER + 'logs/' +CURRENT_TIME+ '.log'
subprocess.Popen(cmd, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)

print("done.")
		
