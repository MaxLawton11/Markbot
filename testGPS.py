import subprocess
process = subprocess.Popen('cgps', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate()
print(out)