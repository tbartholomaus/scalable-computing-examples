# Dockerfile for ADC Scalable Computing Course
FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]
WORKDIR /home/tcb-scomp
RUN apt update && apt -y install python3 pip virtualenvwrapper vim nano iproute2 tree
RUN groupadd -r tcb-scomp && useradd -r -g tcb-scomp tcb-scomp
RUN mkdir -p /home/tcb-scomp && chown tcb-scomp.tcb-scomp /home/tcb-scomp
RUN mkdir -p /var/data && chown tcb-scomp.tcb-scomp /var/data
USER tcb-scomp:tcb-scomp
RUN echo "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh" >> /home/tcb-scomp/.bashrc
COPY ./requirements.txt .
RUN source /usr/share/virtualenvwrapper/virtualenvwrapper.sh && \
    mkvirtualenv scomp-env && \
    pip install --no-cache-dir --upgrade -r requirements.txt && \
    echo "workon scomp-env" >> /home/tcb-scomp/.bashrc
