# Flask-RESTful_postgresql_dockerize
A skeleton framework for creating a Flask REST API in docker with a postgresql database also in docker.

## What does it do?
- You can add objects to the database
  - Go to http://localhost:5000/add/ᐸnameᐳ to add an object with the given name
- You can view all objects in the database
  - Go to http://localhost:5000/all to view all the objects currently in the database
## That's it?
Yes, but this should give a clear idea on how it works and how to expand it! 

You can easily add more tables to the database and write new logic and endpoints to fit your own REST api needs.
## How to use it?
clone or download the project and build it using docker using the command
```
docker-compose build
```
This will create the api docker container and it will put the python flask code in it and install the requirements on the container.

You can now run the container by using the command.
```
docker-compose up
```
This will run the api container, and it will start the postgres database container. 

Now that the backend and database both are running we want to add the tables in the database. This can be done by running the scripts in the migrations folder. Keep the docker containers running and start a new terminal. To see the 2 containers which are now running you can run the command. 
```
docker ps
```
You should see both the backend and the database containers listed along with their container id's. To run the migration database scripts on the database container we want to run the flask database upgrade command on the backend container. We can do that using the following command (The container id can be a partial container id, enough to correctly identify which container is meant.)
```
docker exec -it <backend container Id> flask db upgrade
```
This will add the table by running the scripts in the migrations folder.
It should now be running and operational.
## How to expand it?
You can add your own models by adding another object in the app.models folder and defining it similarly like the PlaceHolder object.
When the new model is imported by adding a line in the init file of the app.models folder it can be used. 
In order to add it to the database you need to create a migration script for the new object. This can be done using the command
```
docker exec -it <backend container Id> flask db migrate -m "<message>"
```
This will scan the project for new models and create a migration script for the changes. This script will be added to the migrations folder and can be executed using the following command while the database container is running.
```
docker exec -it <backend container Id> flask db upgrade
```
Similarly, you can add more rest endpoints by looking in the app.rest folder. You can add your own and import them in the init file of the app.rest folder to include them in the project.
