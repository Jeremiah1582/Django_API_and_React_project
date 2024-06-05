


# step1: environment setup--init
	- set up venv, 
	- git init, 
	- $source venv/Script/activate


 <!-- install dependencies
		$pip install 
			django 
			psycopg2-binary  
			djangorestframework 
			django-filter
			djangorestframework-simplejwt  #handles jwt auth
			django-cors-headers
			Pillow
 
  -->
	

	- initiate Project 
	- migrate
	- ensure server is running

# step1: part 2- cross origin resource sharing (CORS): 
	- add to INSTALLED_APPS in settings.py
		...
			"corsheaders" 
		...

	- add to MIDDLEWARE in settings.py 
		...
			"corsheaders.middleware.CorsMiddleware",
			"django.middleware.common.CommonMiddleware",
		...

	add to the end of settings.py

		CORS_ALLOWED_ORIGINS = ["https://<FRONTEND_SERVER_URL>:<PORT>"]


# step 2: Environment setup -- creating postgresql DB 
	- ensure you have psql 
	- sign into postgress database 
	- CREATE DATABASE coredb
	- configure DB in settings.py to for postgress


	$ psql -U postgres -d postgres

	$ CREATE DATABASE <DBname>

	$ CREATE USER <username> WITH PASSWORD '<string_password>';

	$ 	GRANT ALL PRIVILEGES ON DATABASE <DBname> TO <username>;
		GRANT ALL PRIVILEGES ON SCHEMA public TO <username>;
		GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO <username>;
		GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO <username>;


	$ ALTER USER core CREATEDB; <!-- this will enable the <username> to create DBs also-->


done creating the DB

# step 3: Connect db to Django project

	- open settings.py in project folder
	- modify DATABASES setting. Configure to DB (in this case it will be postgresQL )

	DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<DBNAME>',
        'USER': '<USERNAME>', 
        'HOST': '<localhost or IP of host>', 
        'PASSWORD':'<STRING_PASSWORD>', 
        'PORT': '5342',
    }
	}
# step 4: create app 

	- $py manage.py startapp <app_name> 
	- remove all files in <app_name> folder
	-add label = '<app_name>' to you the apps.py file 
	-  

# step 5: Create User and UserManager Models
	- Create UserManager class that extends BaseUserManager class to manage functionality--create_user() and create_superuser()

	- create User Class that extends AbstractBaseUser, PermissionsMixin classes to structure user data 
	- assign objects= UserManager --now the User class has its own custom manager via User.objects 

# step 6: Create Serializer
	- serializer will extend the ModelSerializer class from Serializer module

	-create Meta class 
		- define model 
		- define api fields 
		- define readonly fields 


# step : Authentication and Authorization with JWT

	- configure settings.py 






