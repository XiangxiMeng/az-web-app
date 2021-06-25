FROM mcr.microsoft.com/appsvc/python:3.6_20201229.1

USER root

# install dependencies
RUN pip install gevent

# app code and port
COPY application.py /src/application.py

# init container
COPY init_container.sh /opt/startup/init_container.sh
ENTRYPOINT ["/opt/startup/init_container.sh"]
