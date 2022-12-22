# syntax=docker/dockerfile:1
# Get ubuntu image
FROM ubuntu:latest
# Install system dependencies
RUN apt update -y; apt install -y curl supervisor 
# Switch working environment
WORKDIR /tmp
# Install ghostscript-9.23
RUN curl -L -O https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs923/ghostscript-9.23-linux-x86_64.tgz \
    && tar -xzf ghostscript-9.23-linux-x86_64.tgz \
    && mv ghostscript-9.23-linux-x86_64/gs-923-linux-x86_64 /usr/local/bin/gs && rm -rf /tmp/ghost*
# Setup app
RUN mkdir -p /app
WORKDIR /app
# Add application
COPY . .
# Setup venv
RUN apt install python3.10-venv -y
# install pip
RUN apt install python3-pip -y
# Install Python dependencies
RUN pip install flask Pillow
RUN pip install bs4
RUN pip install requests
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
# Expose port the server is reachable on
EXPOSE 5000
# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1
# Run app
CMD ["flask", "run"]
