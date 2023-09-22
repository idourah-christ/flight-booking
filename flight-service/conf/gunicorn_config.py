import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname) 

command = '/c/Users/ybahamboulaidourah/my-desktop/mobembo-proj/mobembo-api/backend/env/Scripts'
pythonpath='/c/Users/ybahamboulaidourah/my-desktop/mobembo-proj/'

bind='{0}:8000'.format(IPAddr)

workers = 3