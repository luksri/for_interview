import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(['python', 'child_signal.py'])
print('PARENT      : Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
print('PARENT      : Signaling child')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGTERM)