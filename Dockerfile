FROM resin/rpi-raspbian:stretch

MAINTAINER Ericmas001

ENV PIN=23
ENV KEY=PROVIDE_ME

VOLUME /config/

RUN apt-get update
RUN apt-get install \
	python \
	python-dev \
	python-setuptools \
	python-pip \
    git \
	pigpio \
	-y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade wheel
RUN pip install pip-upgrade-outdated
RUN pip_upgrade_outdated

RUN pip install git+https://github.com/Ericmas001/HVAC-IR-Control
RUN pip install flask
RUN pip install pigpio

ADD entrypoint.sh /entrypoint.sh
ADD default_config.json /default_config.json
COPY exec/*.py /exec/

CMD ["/bin/bash", "/entrypoint.sh"]