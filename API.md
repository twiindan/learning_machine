API
================

Learning Machine API

### USERS

## CREATE USER

URL: POST /user/
BASIC AUTHENTICATION
BODY: {
        username: string
        password: string
        email: string
      }

RESPONSE:
    201 CREATED
    400 BAD REQUEST

## GET ALL USERS

URL: GET /user/
BASIC AUTHENTICATION

RESPONSE:
    200 OK including list of users


## GET USER

URL: GET /user/{userID}
BASIC AUTHENTICATION

RESPONSE:
    200 OK including users information
    404 Not Found


## DELETE USER

URL: DELETE /user/{userID}
BASIC AUTHENTICATION

RESPONSE:
    204 No Content
    404 Not Found

### QUESTIONS

## CREATE QUESTION

URL: POST /questions/
BASIC AUTHENTICATION
BODY: {
        question: string
        answer: string
      }

RESPONSE:
    201 CREATED including ID
    400 BAD REQUEST
    409 CONFLICT

## GET ALL QUESTIONS

URL: GET /questions/
BASIC AUTHENTICATION

RESPONSE:
    200 OK including list of questions

## GET QUESTION INFORMATION

URL: GET /questions/{questionID}
BASIC AUTHENTICATION

RESPONSE:
    200 OK including question information
    404 Not Found


## UPDATE QUESTION INFORMATION

URL: PUT /questions/{questionID}
BASIC AUTHENTICATION

BODY: {
        id: integer
        question: string
        answer: string
      }

RESPONSE:
    200 OK including question information
    400 BAD REQUEST
    404 Not Found
    409 CONFLICT


## DELETE QUESTION

URL: DELETE /questions/{questionID}
BASIC AUTHENTICATION

RESPONSE:
    204 Not Content
    404 Not Found

### PLAY

## Get Question to Play

URL: GET /play/
BASIC AUTHENTICATION

RESPONSE:
    200 OK including the questionID and the question

##Answer Question

URL: POST /play/
BASIC AUTHENTICATION

BODY:   {
        "id": integer,
        "answer": string
        }

RESPONSE:
    200 OK including information if the answe is correct and in witch box is



