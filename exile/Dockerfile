# Use an official Python runtime as a parent image
FROM ksketo/python-pillow
ENV PYTHONUNBUFFERED 1
ENV REDIS_HOST "redis"
ENV MONGO_HOST "mongodb"
RUN mkdir /exile
# Set the working directory to /exile
WORKDIR /exile

# Copy the current directory contents into the container at /exile
ADD . /exile

# Install any needed packages specified in dependencias.txt
RUN pip install --upgrade pip
RUN pip install -r dependencias.txt
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# Run python when the container launches
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# RUN /bin/sh -c python manage.py celery -A picha worker -l info
# RUN /bin/sh -c python manage.py celery -A picha beat -l info

#To REmove Zombies use: docker rmi $(docker images -f "dangling=true" -q)
