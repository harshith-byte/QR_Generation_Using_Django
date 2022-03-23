# QR_Generation_Using_Django

## About the project

- A project based on Generating QR Code which links to other URL using Django

- Project has **home page** which has a form containing Name as a field.

- On submitting the form **QR Code** is generated based on the Name and a mail is sent to Static User Gmail Id

- On scanning the QR Code it generates a unique URL which links to **doctor details page**

- In this project we have two Database tables 
  - doctor_name
  - doctor_details
  
- Frontend
  - HTML
  - CSS
  - JS 

- Docker Container is used to run this project

- Framework
  - Django 

- Django provides it's default admin panel where superuser can create, update or delete data

## Steps to Run the Project(only for win/linux):

- Install docker and docker-compose *if not installed*
  - [docker-installation](https://docs.docker.com/compose/install/)


- Pull git repo to local machine 
```
  - git clone git@github.com:harshith-byte/QR_Generation_Using_Django.git
```

- make changes in /QR_to_Website/QR_to_Website/setting.py file by adding Email Address and Password.

- make changes in /QR_to_Website/main/views.py file by adding custom Email Address to send mail to.

- open terminal and Change directory to QR_to_Website
```
  - cd QR_to_Website/
```


- run docker-compose 
```
  - docker-compose up
```


- To create superuser 
```
  - docker-compose run web python manage.py createsuperuser
```


- Open any browser and type 
```
  - 0.0.0.0:8000/
```


- To stop docker type in terminal
```
  - ctrl+c
```


- To shut down the container
```
  - docker-compose down
```
