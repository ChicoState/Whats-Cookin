FROM python:3.8.10
COPY requirements.txt ./
RUN pip3 install -r --user requirements.txt
COPY . ./
RUN chmod +x docker_run_server.sh
ENTRYPOINT ["./docker_run_server.sh"]
