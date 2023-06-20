# Pick a low configuration python base image
FROM python:alpine

#  Expose the port 5000 of the docker container
EXPOSE 5000

# Create a folder app in container and work inside it
WORKDIR /app

COPY requirements.txt .

# Install all the requirements
RUN pip3 install -r requirements.txt

# Copy all the flask project files into the WORKDIR
COPY . .

# Execute flask application inside the container
CMD python3 app/main.py