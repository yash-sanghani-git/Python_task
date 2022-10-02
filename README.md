## Uploading and processing the CSV file in Django for automation ETL likewise flow

The task is complete dynamic which takes input of the user from is in the form of CSV file. It processes the data and stores it in the database dynamically. The complete App is designed in the Django Framework of python  with a MySQL database. It contains a test case with the use of the python library. The task is completely dynamic as it doesn’t use any inbuilt ORM of django rest framework or not using any inbuilt migration library. Below are the steps to run the application.I made it very simple, not too complex but tried to create dynamic migration. As we kept it simple we are not removing the existing data but adding newer data into the same database/table. 

- It is able to adapt any kind of user table in xlsx file.

- I used a Docker Compose tool that was developed to help define and share multi-container applications. With Compose, we can create a YAML file to define the services and with a single command, can spin everything up or tear it all down

Download the zip of the project, unzip and ready to go....

''Run Project''

1. Create a Dockerfile : `docker build -t task:latest .`
2. `docker pull mysql`
3. `docker-compose up`
4.  The API endpoints will be available at **http://127.0.0.1:8001/** by default.


''Run Testcase''

1. Open new terminal in project `pip install pytest-django`
2. Run your tests with `pytest`


Note : File must be in '.xlsx' format and data always be in sheet 1. Kindly change the database credentials in the environment file to connect with your database. If you face any difficulties while connection to database then may issue is due to your local python setup. In that case manually add your databse connections in to the proje ts and it will ready to go...
