import subprocess

# Run cgps command and capture output
output = subprocess.check_output(["cgps", "-s"]).decode("utf-8")

# Print the raw data
print(output)
