# Use an official Python runtime as a parent image
FROM ksketo/python-pillow

# Set the working directory to /exile
WORKDIR /exile

# Copy the current directory contents into the container at /exile
ADD . /exile

# Install any needed packages specified in dependencias.txt
RUN pip install -r dependencias.txt

# Run python when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#To REmove Zombies use: docker rmi $(docker images -f "dangling=true" -q)