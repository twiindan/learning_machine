learning_machine
================

Learning Machine backend

### How to install

python manage.py sql geography
python manage.py syncdb 
If the system requests for create SuperUser, create it with qa / qa as a username and password
python manage.py runserver

### To populate DDBB with questions (Country / Capital)

cd testing 
nosetest question_test.py

### There is a client to play with the server. To execute it:

python client.py

IMPORTANT: In the client there is a bug when the software get the answer input and is requeired type a string with simple quotes. For example if the answer is SPAIN (is not case sensitive), please type 'SPAIN' with the simple quotes.

