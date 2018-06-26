
[![Coverage Status](https://coveralls.io/repos/github/Dygn/Ride-My-Way/badge.svg?branch=master)](https://coveralls.io/github/Dygn/Ride-My-Way?branch=master)
[![Build Status](https://travis-ci.org/Dygn/Ride-My-Way.svg?branch=ft_API_test_fetchall_rides)](https://travis-ci.org/Dygn/Ride-My-Way)
<a href="https://codeclimate.com/github/Dygn/Ride-My-Way/test_coverage"><img src="https://api.codeclimate.com/v1/badges/6f6bf67aa1748353d433/test_coverage" /></a>
<a href="https://codeclimate.com/github/Dygn/Ride-My-Way/maintainability"><img src="https://api.codeclimate.com/v1/badges/6f6bf67aa1748353d433/maintainability" /></a>

# Ride-My-Way
Ride-My-Way App is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers

----
## Required Features
1. Users can create an account and log in.
2. Drivers can add ride offers..
3. Passengers can view all available ride offers.
4. Passengers can see the details of a ride offer and request to join the ride. E.g What time the ride leaves, where it is headed e.t.c
5. Drivers can view the requests to the ride offer they created.
6. Drivers can either accept or reject a ride request.

---
## Endpoints

Test on Postman 
## API Endpoints
GET all rides
https://riddemyway.herokuapp.com/api/v1/rides

GET rides by Id
https://riddemyway.herokuapp.com/api/v1/rides/1
https://riddemyway.herokuapp.com/api/v1/rides/2

POST create ride
https://riddemyway.herokuapp.com/api/v1/rides

PUT request ride
https://riddemyway.herokuapp.com/api/v1/rides

---
## Installation

<p><code>$ git clone https://github.com/dygn/Ride-My-Way.git</code></p>

cd into the folder

<p><code>$ cd Ride-My-Way</code></p>

---
## Dependencies
Install dependencies
<p><code>$ pip install -r ./project-API/APP/requirements/dev.txt</p></code>

---
## Testing
set up unit testing environment:

<p><code>$ pip install pytest</p></code>
<p><code>$ pip install coverage</p></code>

run tests
<p><code>$ pytest</p></code>

start server
<p><code> $ python run.py</p></code>

---
## UI Templates
[http://dygn.github.io/Ride-My-Way/UI](http://dygn.github.io/Ride-My-Way/UI/)

---
## API Documentation

### Authors
1. Dickens Onyango

---
## Acknowledgment


Pivot tracker https://www.pivotaltracker.com/n/projects/217849

