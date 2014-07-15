import subprocess

for i in xrange(1001):
    p = subprocess.Popen('echo %i | ./bomb defuser-partial.txt' % (i,), stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    if "BOOM" not in out:
        print i
        break
