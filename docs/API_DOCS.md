# Documentation for the API
# =========================
#
## Table of Contents
#
# - [Introduction](#introduction)
# - [Authentication](#authentication)
# - [Creating users](#users)
# - [List of locations](#locations)
# - [List of therapists](#therapists)
# - [Docs](#docs)

## Introduction
This document describes the API of the project.

## Authentication
The API uses token authentication. To authenticate, make a POST request to the `/login/` endpoint with the user's credentials. If the credentials are valid, the server will return a JSON response with the access token and status code 200, otherwise it will return a JSON response with an error message and status code 400.

If user is 'Student' the `/login/` endpoint will also return his/her `status`. **Note:** To be argued if this is the right way to do it.

Possible `status` values are:
- `P` for `Pending`
- `A` for `Active`
- `F` for `Frozen`

### Example
#### Request
```
POST /login/
{
    "username": "user",
    "password": "password"
}
```
#### Response
```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "status": "A"
}
```

## Users
For the moment, the API only supports creating 'Student' users. To create a 'Student' user, make a POST request to the `/register/` endpoint with the user's data.

If the credentials are valid, the server will return a JSON response with user's data.
#### fields:
- `email` (string) (unique)
- `password` (string)
- `name` (string)
- `surname` (string)
- `location` (int) (pk of the location, see [Locations](#locations))
- `date_of_birth` (date) (format: YYYY-MM-DD)
- `mentor` (int) (pk of the mentor, see [Therapists](#therapists))
#### All fields are required.
### Example
#### Request
```
POST /register/
{
    "email": "example@example.com",
    "password": "password",
    "name": "John",
    "surname": "Doe",
    "location": 1,
    "date_of_birth": "1990-01-01",
    "mentor": 1
}
```
#### Response
```
{
    "email": "example@example.com",
    "name": "John",
    "surname": "Doe",
    "location": 1,
    "date_of_birth": "1990-01-01",
    "mentor": 1
}
```

## Locations
The API supports getting list of locations. To get the list of locations, make a GET request to the `/locations/` endpoint. 
### Example
#### Request
```
GET /locations/
```
#### Response
```
[
    {
        "id": 1,
        "name": "Location 1"
    },
    {
        "id": 2,
        "name": "Location 2"
    }
]
```
## Therapists
The API supports getting list of therapists. To get the list of therapists, make a GET request to the `/therapists/` endpoint.
### Example
#### Request
```
GET /therapists/
```
#### Response
```
[
    {
        "email": "example1@gmail.com",
        "name": "John",
        "surname": "Doe",
        "id": 1
    },
    {
        "email": "example2@gmail.com",
        "name": "Marry",
        "surname": "Smith",
        "id": 2
    }
    
]
```
## Docs
The API supports getting list of docs. To get the list of autodocs made with coreAPI, make a GET request to the `/docs/` endpoint.



