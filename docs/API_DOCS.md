# Documentation for the API
# =========================

## [Authentication](#authentication)
#### - [Signing up](#signing-up)
#### - [Logging in](#logging-in)
#### - [Token management](#token-management)
## [Users](#users)
#### - [Getting data of the current user](#getting-data-of-the-current-user)
#### - [Getting list of users](#getting-list-of-users)
- [Filtering](#filtering)
#### - [Getting user details](#getting-user-details)
#### - [Updating user details](#updating-user-details)
#### - [Partially updating user details](#partially-updating-user-details)
#### - [Changing user status](#changing-user-status)
#### - [Deleting user](#deleting-user)
## [Homes and roles](#homes-and-roles)
#### - [Getting list of homes](#getting-list-of-homes)
#### - [Getting home details](#getting-home-details)
#### - [Getting list of roles](#getting-list-of-roles)
#### - [Getting role details](#getting-role-details)
## [Not found](#not-found)
#### - [Not found](#not-found)

## Authentication
To use the majority of the API endpoints, you need to be authenticated.
### Signing up
Let's first create a new user. To do that, we need to send a `POST` request to `/users/register/` with the following data:
```json
{
    "email": "...",
    "name": "...",	
    "surname": "...",
    "password": "...",
    "document": "...",
    "date_of_birth": "...",
    "home": "...",
    "roles": ["..."],
}
```
The `home` field is the ID of the home the user is going to be assigned to.

The `roles` field is a list of IDs of roles the user is going to be assigned to.

The `date_of_birth` field is a string in the format `YYYY-MM-DD`.

The `document` field is a string containing the document number of the user.

The `password` field is a string containing the password of the user.

The `email` field is a string containing the email of the user.

The `name` field is a string containing the name of the user. 

The `surname` field is a string containing the surname of the user.

The response will be:
```json
{
    "id": "...",
    "email": "...",
    "name": "...",
    "surname": "...",
    "document": "...",
    "date_of_birth": "...",
    "home": "...",
    "roles": ["..."],
    "created_at": "...",
    "status": "..."
}
```
## Logging in
To log in, we need to send a `POST` request to `/users/login/` with the following data:
```json
{
    "email": "...",
    "password": "..."
}
```
The `email` field is a string containing the email of the user.
The `password` field is a string containing the password of the user.

The response will be:
```json
{
    "token": "..."
}
```

## Token management
To use the majority of the API endpoints, you need to be authenticated. To do that, you need to send the token in the `Authorization` header of the request. The token is returned when you log in. The header should look like this:
```
[
    "Authorization": "Token <token>"
]
```

# Users
## Getting data of the current user
To get the data of the current user, we need to send a `GET` request to `/users/current/`. The response will be:
```json
{
    "id": "...",
    "email": "...",
    "name": "...",
    "surname": "...",
    "document": "...",
    "date_of_birth": "...",
    "home": "...",
    "roles": ["..."],
    "created_at": "...",
    "status": "..."
}
```
## Getting list of users
To get the list of users, we need to send a `GET` request to `/users/`. The response will be:
```json
[
    {
        "id": "...",
        "email": "...",
        "name": "...",
        "surname": "...",
        "document": "...",
        "date_of_birth": "...",
        "home": "...",
        "roles": ["..."],
        "created_at": "...",
        "status": "..."
    },
    {
        "id": "...",
        "email": "...",
        "name": "...",
        "surname": "...",
        "document": "...",
        "date_of_birth": "...",
        "home": "...",
        "roles": ["..."],
        "created_at": "...",
        "status": "..."
    },
  ...
]
```
### Filtering
You can filter the list of users by sending a `GET` request to `/users/?<filter>=<value>`. The response will be:
```json
[
    {
        "id": "...",
        "email": "...",
        "name": "...",
        "surname": "...",
        "document": "...",
        "date_of_birth": "...",
        "home": "...",
        "roles": ["..."],
        "created_at": "...",
        "status": "..."
    },
    {
        "id": "...",
        "email": "...",
        "name": "...",
        "surname": "...",
        "document": "...",
        "date_of_birth": "...",
        "home": "...",
        "roles": ["..."],
        "created_at": "...",
        "status": "..."
    },
  ...
]
```
The available filters are:
- `email`
- `name`
- `surname`
- `document`
- `date_of_birth`
- `home`
- `roles`
- `created_at`
- `status`

## Getting user details
To get the details of a user, we need to send a `GET` request to `/users/<id>/`. The response will be:
```json
{
    "id": "...",
    "email": "...",
    "name": "...",
    "surname": "...",
    "document": "...",
    "date_of_birth": "...",
    "home": "...",
    "roles": ["..."],
    "created_at": "...",
    "status": "..."
}
```
## Updating user details
To update the details of a user, we need to send a `PUT` request to `/users/<id>/` with the following data:
```json
{
    "email": "...",
    "name": "...",
    "surname": "...",
    "document": "...",
    "date_of_birth": "...",
    "home": "...",
    "roles": ["..."]
}
```

## Partially updating user details
To partially update the details of a user, we need to send a `PATCH` request to `/users/<id>/` with the following data:
```json
{
    "field_to_update": "...",
    ...
}
```

## Changing user status
To change the status of a user, we need to send a `POST` request to `/users/<id>/status/` with the following data:
```json
{
    "status": "..."
}
```
The `status` field is a string containing the new status of the user.

## Deleting user
To delete a user, we need to send a `DELETE` request to `/users/<id>/`.
You can only delete a user being a superuser.

# Homes and roles
## Getting list of homes
To get the list of homes, we need to send a `GET` request to `users/homes/`. The response will be:
```json
[
    {
        "id": "...",
        "name": "...",
        "address": "..."
    },
    {
        "id": "...",
        "name": "...",
        "address": "..."
    },
  ...
]
```
## Getting home details
To get the details of a home, we need to send a `GET` request to `users/homes/<id>/`. The response will be:
```json
{
    "id": "...",
    "name": "...",
    "address": "..."
}
```
## Getting list of roles
To get the list of roles, we need to send a `GET` request to `users/roles/`. The response will be:
```json
[
    {
        "id": "...",
        "name": "..."
    },
    {
        "id": "...",
        "name": "..."
    },
  ...
]
```
## Getting role details
To get the details of a role, we need to send a `GET` request to `users/roles/<id>/`. The response will be:
```json
{
    "id": "...",
    "name": "..."
}
```

## Not found
If you try to access an endpoint that doesn't exist, you will get a `404` response with the following data:
```json
{
    "error": "Not found"
}
```








