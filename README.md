# A.P Registration and Stamp Department Server

## Project Statement
The goal of this project is to create a A.P Registration and Stamp Department Server.

## Project Features - 
1. Basic Front-end as described in project description. (Similar to that of A.P Government Registration and Stamp Department Server
2. Login and User Authentication and ability to sign up as a new user.
3. Forms to add to different tables.
4. Ability to send SMS to person regarding Land Registration (still in Development)

## Project Implementation Details -

1. Database Used - MySQL
2. Created Login, User Authentication and Signup Features
3. Forms to add data into Databases

## -------------------------------------------------------------------------------------------------------

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This is a simple Phone book where we add, update, delete, and get all the contactthe s from the database using API.

## Technologies
Project is created with:
* Python 3.9
* Django 3.1.1
* Django Rest Framework 3.12.4
* Crispy forms
* MySQL Server

## Setup

1. Installation
      * Install Python 3.9 from [Python](https://www.python.org/downloads/).
      * To install Django, open Terminal/Command prompt and run the following command
      ```
      pip install django==3.1.1
      ```
      * To install Django Rest Framework, open Terminal/Command prompt and run the following command
      ```
      pip install djangorestframework==3.12.4
      ```
      * To install Crispy Forms, open Terminal/Command prompt and run the following command
      ```
      pip install django-crispy-forms
      ```
      * Install MySQL Server from [MySQL](https://dev.mysql.com/downloads/mysql/).
      * Install Postman from [Postman](https://www.postman.com/downloads/).

2. Download the zip and extract it.

3. After Setting up your MySQL server, create a Database with name "dev_project" and Enter the user and Password of root user in project/settings.py
    

4. Right click in the folder and select *Open in Terminal* and run the following command
      ```
      python manage.py makemigrations
      ```
      ```
      python manage.py migrate
      ```

      ```
      python manage.py runserver
      ```
5. Go to http://127.0.0.1:8000/ to access the website features

