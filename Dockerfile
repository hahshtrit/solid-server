FROM python:3.9

ENV HOME /root
WORKDIR /root

COPY . .

# Download dependencies
RUN pip3 install --no-cache-dir -r requirements.txt


EXPOSE 80

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait

RUN chmod +x /wait


CMD /wait && python run.py