# start by pulling the python image 
FROM python:3.8-alpine 

# Copy the requirements file into the image 
COPY ./requirements.txt /app/requirements.txt 

# switch working directory 
WORKDIR /app 

# Install the dependencies and packages in the requirements file 
RUN pip install -r requirements.txt 

# Copy every content from local code base to the image 
COPY . /app 

# configure the container to run in an executed manner 
ENTRYPOINT [ "python" ]

# When we run commands, we execute on entry point, which becomes "python view.py"
CMD ["main.py"]