import os

def check_ping(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"
    return pingstatus


prefix = '192.168.1.'
active = []
error = []
other = []
for i in range(256):
	current = prefix + str(i)
	status = check_ping(current)
	if 'Error' in status:
		error.append(current)
	elif 'Active' in status:
		active.append(current)
	else:
		other.append(current)

print(active, '\n\n')
print(error, '\n\n')
print(other, '\n\n')

print(len(active), '\n\n')
print(len(error), '\n\n')
print(len(other), '\n\n')
