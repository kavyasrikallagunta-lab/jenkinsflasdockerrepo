FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install flask flask-restful flask-sqlalchemy flask-cors
EXPOSE 5000
CMD ["python", "userresource.py"]