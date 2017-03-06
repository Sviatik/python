import sys

import dockermap.api

docker_url = 'unix://var/run/docker.sock'
tag_name = sys.argv[1]


docker_conn = dockermap.api.DockerClientWrapper(docker_url)
docker_file = dockermap.api.DockerFile('centos7/hw:latest')

docker_file.run_all('yum install -y httpd')
docker_file.run_all('echo Homework6! > /var/www/html/index.html')

docker_file.entrypoint = ['/usr/sbin/httpd']
docker_file.command = ['-D', 'FOREGROUND']


docker_conn.build_from_file(docker_file, tag_name)
