# DevGripOpenWeatherService
This project was made by Ozzy to Dev Grid Crue evaluation. 


This project have intention to proof my knowledge in Python language and to be a test about.

The project have be a service to run as a back end software which collect data from Open Weather Map and must store this data as JSON file.

Start here:

To install this project, you must follow the instructions below on your terminal:

1. Clone the repository:

    git clone https://github.com/ozzysp/DevGridOpenWeatherService.git

2. Create virtual environment:

    python3 -m venv venv

3. Activate virtual environment:

    source venv/bin/activate

4. Install requirements:

    pip install -r requirements.txt
 
5. run the application:

    python3 manage.py runserver

6. Launch your browser:

    navigate to http://localhost:8000/



# Decisions about the project:


When I started this project, I was thinking about the following:

   To reach the goal of this project, I must create a service that will collect data from Open Weather Map and store this data as JSON file.
   
So, I decide to build a main file with the following structure:
   
Requests library is used to make the request to Open Weather Map.
   
The data is stored in a JSON file.
   
The data is converted to human readable format with the help of the library humanize.
   
To make multiple requests to Open Weather Map, the library used is threading.
   
To register the date and time of the request, the library used is datetime.

To create a CRUD application, the library used is Django.
   
To create a database, the standard library used in Django SQLite.
   
