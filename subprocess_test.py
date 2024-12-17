import subprocess

print("popen3:")

proc = subprocess.Popen(
    'python test1.py - ;echo "to stderr"1>&2', #[[[[[(just give 'dir' or 'cat' to print out on stdout and stderr respectively)]]]]]]]
    shell = True,
    stdin= subprocess.PIPE,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
)

msg = 'through stdin to stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)

print('passout through:', repr(stdout_value.decode('utf-8')))
print('passerror through:', repr(stderr_value.decode('utf-8')))

'''
# for monitoring the log file
import time
import subprocess
import select

f = subprocess.Popen(['tail','-F',filename],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        
## without poll, and using only readline of stdout blocks the pgm till tail process closes.
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll(1):
        print f.stdout.readline()
    time.sleep(1)
'''