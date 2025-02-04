# BIS 471/571 - Docker Demonstration


## Definitions
- **Docker**: Docker is an open-source platform that enables developers to build, package, and distribute applications in containers.
- **Containers**: A container is a lightweight, portable, and isolated environment that runs an application along with all its dependencies, libraries, and configurations.

## Uses For Docker Containers
- Running microservices architectures
- Creating development and testing environments that match production (CI/CD)
- Deploying Cloud-Native applications seamlessly between different providers 

## Docker File
The **docker file** is the **blueprint** for the container. It is a script that **defines and automates** the process of building a docker image. It contains **instructions** on how to set up the **environment, install dependencies and configure** the application inside a docker container. There is a lot you can do to customize your container using the docker file but typically the basic structure is as following:

- ```FROM``` Specify a base image. There is a plethora of already create base image that can be found on [docker hub](https://hub.docker.com/). You traditionally with start with a image that has some core functionality that you need. For example if you are creating a python application you would start with the python image. 
- ```WORKDIR``` Set the working directory. This tells docker where the subsequently defined command should be run. 
- ```COPY``` Copies local files. This tells docker what files it should copy over into the container. 
- ```RUN``` Installs dependencies. This command will be followed by what needs to be run in install the dependencies of the project. 
- ```EXPOSE``` Exposes a port for the application. If we know our application will be using a specific port, then we explicitly expose that port here. 
- ```CMD``` Defines the command that will be used to run the application. This line will be proceeded by the command to run along with the file it should be run on. 





## How to Make a Docker Container
### 1. [**Install Docker**](https://docs.docker.com/desktop/setup/install/windows-install/)
Following the link and download docker desktop. This will download both the GUI and CLI along with all functionality needed to create and run a container. 
![Alt text](Images/docker_download.jpg)

### 2. **Create Application**
This could be any application but in this example we are just using Flask which is a web framework written in python. 
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 3. **Create Dependencies text file**
Create a file in the same directory that list all of the necessary requirements. In out example we only need the flask library. 
```
flask
```

### 4. **Create Docker File**
Create the docker file that will function as the blue print for this container. Anyone with this docker file will be able to recreate an identical container and run the application on any device. 
```
# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port (Flask runs on 5000)
EXPOSE 5000

# Define the command to run the app
CMD ["python", "app.py"]
```

### 5. **Build Docker Image**
Run the following command inside the project folder. This can also be done via the GUI on docker desktop. This command will find the DockerFile and use the information inside of it to create the container. 
```
docker build -t my-flask-app .
```
- ```-t``` allows us to name the container
- ```.``` tells docker to use the current directory as build context

You can check built images using this command
```
docker image ls
```
### 6. **Run the Container**
The following command will run the container that has just been built
```
docker run -d -p 5000:5000 --name my-running-app my-flask-app
```
- ```-d``` tells docker to run the container in the background
- ```p- 5000:5000``` maps host port 5000 to container's port 5000
- ```--name my-running-app my-flask-app``` assigns a name to the running container

Now we can check if the container is running using

``` docker ps```

If the container is running, we can access [http://localhost:5000](http://localhost:5000) we should see our text from our python program displayed

![Alt text](Images/docker_working.jpg)


