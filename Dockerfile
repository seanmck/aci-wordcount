FROM python:alpine3.17

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY * /

ENV NumWords=10 MinLength=0
CMD python wordcount.py http://shakespeare.mit.edu/hamlet/full.html
