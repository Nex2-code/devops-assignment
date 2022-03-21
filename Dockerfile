FROM python:alpine3.14
RUN pip3 install flask \
    python-dotenv
RUN mkdir flask
WORKDIR /flask
COPY app.py .
COPY .env .
EXPOSE 80
CMD ["python3","app.py"]
