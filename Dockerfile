FROM python:3.11-rc-bullseye

WORKDIR app

RUN pip install pyyaml && \
    apt update && apt install -y python3-apt

COPY . app

ENTRYPOINT ["/bin/bash"]
