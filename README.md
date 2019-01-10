# questioner

[![Coverage Status](https://coveralls.io/repos/github/b0nbon1/questioner/badge.svg?branch=develop)](https://coveralls.io/github/b0nbon1/questioner?branch=develop)  [![Build Status](https://travis-ci.org/b0nbon1/questioner.svg?branch=develop)](https://travis-ci.org/b0nbon1/questioner)

this is crowd platform where meetups are created questions are asked


# API-endpoints


## The following are API endpoints enabling one to: 
* Create a meetup record.
* Create a question record.
* Get a specific meetup record.
* Get all meetup records.
* Upvote or downvote a question.
* Rsvp for a meetup.
## Here is a list of the functioning endpoints

| EndPoint                | Functionality        | Routes            |
| :---                    |     :---:            | :---              |
| POST /meetup            | post a meetup       | /api/v1/meetup    |
| GET /meetups/< meetup_id >   | Get a specific meetup by meetup id| /api/v1/meetups/< meetup_id > |
| GET /meetups/upcoming            | Get upcoming meetups        | /api/v1/orders    |
| POST /Questions            | Post questions          | /api/v1/meetups/upcoming |
| PATCH /questions/< question_id>/upvote             | Vote for question          | /api/v1/questions/< question_id>/upvote  |
| PATCH /questions/< question_id>/downvote   | Vote for question     | /api/v1/questions/< question_id>/downvote  |
| POST /meetups/< meetup_id >/rsvp             | post meetups rasvp          | /api/v1/meetups/< meetup_id >/rsvp|

  
## Testing the endpoints

* Install python then using pip instal .. install flask
* clone the repo
* Ensure that postman is installed
* From your terminal locate the repo and run: python run.py
* open postman and test the endpoints
* Use pytest to run the the tests

# Written by: Bonvic Bundi
#### Copyright © Andela 2019 
