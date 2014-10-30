API
================

Learning Machine API

### USERS

## CREATE USER

URL: POST /user/
BASIC AUTHENTICATION
BODY: {
        username: <string>
        password: <string>
        email: <string>
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

    