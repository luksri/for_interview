import io
import subprocess

print("one line at a time")

proc = subprocess.Popen(
    'python repeater.py',
    shell = True,
    stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,
)

stdin = io.TextIOWrapper(
    proc.stdin,
    encoding = 'utf-8',
    line_buffering = True,
)

stdout = io.TextIOWrapper(
    proc.stdout,
    encoding = 'utf-8',
)

for i in range(10):
    line = '{}\n'.format(i)
    stdin.write(line)
    output = stdout.readline()

remainder = proc.communicate()[0].decode('utf-8')
print(remainder)