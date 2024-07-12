# Introduction

Cookies is an Internet standard for storing states over HTTP.  Without cookies,
web sites would not be able to remember states such as if you are logged in or
shopping carts.

You can read all about cookies here: https://datatracker.ietf.org/doc/html/rfc6265

How do you use curl to test websites that require an active login?  

Start by installing this extension on chrome (don’t worry it’s safe, I wrote it):
https://chrome.google.com/webstore/detail/simple-curl-compatible-co/hacpnjlfmfaiedcejmognhhffdpooafe?hl=en 

The following video shows how you can use the extension to extract cookies so you can
use curl to visit websites protected by logins.

https://youtu.be/KH8VERTYz1g 

# Q1

Experiment with other websites (start with your own langara registration login) that
you regularly use.  List out websites that work and don't work and show your curl call
and http response in a text file called `q1.txt`

# Q2

We can store a JWT in a cookie after a successful login so the login information
is shared between all pages on the same site.

Modify https://github.com/env3d/jwt-lessons/blob/main/02-hmac-token.sh so that
it stores the generated JWT in a cookie.  Call this `q2.sh`

# Q3

Create a script `q3.sh` that returns 200 if a valid JWT is provided in a cookie (not
in the Authorization header).  Otherwise, the script returns a 401 Unauthorized.

If you use a browser to visit `q2.sh` it would put a JWT in the cookie.  If you then
visit `q3.sh`, it should return 200 since the cookie will automatically be inserted
in the cookie request header.

If you visit `q3.sh` without visiting `q2.sh` first, it will return an error.
