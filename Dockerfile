FROM python:3.8

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
ADD ./requirements.txt /usr/src/app/requirements.txt

RUN python -m pip install --upgrade pip

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app

# run server
CMD python app.py runserver -h 0.0.0.0