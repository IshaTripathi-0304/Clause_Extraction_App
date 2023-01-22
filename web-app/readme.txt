This module contains:
1. [mysite]: Folder which contains Django webapp master files
2. [crt]: Folder with main django website of 2 pages. [1: to upload pdf, 	2: to view uploaded pdf]
3. [media]: Folder where pdfs uploaded by django webapp are stored
4. [manage.py]: Default Django file which runs the webapp
5. [sqlite3.exe, db.sqlite3]: sql lite exe and database, where we store the list of uploaded files on the webapp. This db is updated through crt>views.py>BookUploadView() & the DB info is stored in web-app>mysite>setting.py>DATABASES
6. [screens]: Folder containing screens of the webapp

=================== TO run this WebApp ==================
########## Navigate to this folder on CMD using below command:
cd web-app
########## Run below command
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8080

then open webApp at: http://localhost:8080/
=================================================
python -m pip install --upgrade 

pip install -r requirements.txt

django-admin startproject mysite .

python manage.py migrate
python manage.py runserver 0.0.0.0:8080

http://localhost:8080/

python manage.py startapp crt

https://www.askpython.com/django/upload-files-to-django


===== SQLite Installtion & commands============
https://www.sqlite.org/download.html
sqlite-tools-win32-x86-3390400.zip: copy sqlite3.exe to root

>>python manage.py dbshell
>>.tables
>>.schema --indent crt_ebooksmodel;
>>select * from crt_ebooksmodel;
>>Delete from crt_ebooksmodel
>>DELETE FROM SQLITE_SEQUENCE WHERE name='crt_ebooksmodel';
>>Ctrl + Z

