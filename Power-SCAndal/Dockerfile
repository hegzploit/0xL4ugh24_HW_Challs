FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install socat python3 python3-pip -y
RUN pip install numpy

WORKDIR /app
COPY main.py server.py
COPY first_part.pkl .
COPY second_part.pkl .

ENTRYPOINT ["socat", "TCP-LISTEN:22222,reuseaddr,fork", "EXEC:python3 server.py,stderr"]
