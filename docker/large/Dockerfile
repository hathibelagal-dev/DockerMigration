FROM ubuntu:16.04

COPY run.sh /tmp
RUN apt-get update && apt-get install -y bash
CMD ["/bin/sh", "/tmp/run.sh"]
