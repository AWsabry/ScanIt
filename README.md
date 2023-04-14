# ScanIt

## What is added in this branch ?

When you call the url "http://localhost:8000/login" it returns a token expeired after 40 seconds
- This token will be accessable as a Bearer auth in the header of the url of "http://localhost:8000/user" and return user data.
- "http://localhost:8000/register" will create another user with this fields required :

-- email
-- first_name
-- last_name
-- password
-- city
-- PhoneNumber

Otherwise the api will return "serializer not valid" with status_code 400.
