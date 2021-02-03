FROM tiangolo/uwsgi-nginx:python2.7
RUN pip install flask

# Add demo app
ADD . /app

WORKDIR /app
CMD ["python", "app.py" ]
