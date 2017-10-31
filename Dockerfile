FROM python:3.6.2-slim
COPY * /
RUN pip install html2text && pip install urllib3 && pip install sh
ENV NumWords=10 MinLength=0
CMD python wordcount.py http://shakespeare.mit.edu/hamlet/full.html
