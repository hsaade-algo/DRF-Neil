# DRF

<br>
<br>


**Project Requirements (as received)**
1. REST API that exposes CRUD methods on classes Foo and FooBar
2. All methods on API require user to be securely authenticated and authorized (HTTPS)
3. Provide a login API through which a user can attempt to login.
4. Registered users: foo and foobar.

User foo has permission to invoke methods on Foo.
<br>
User foobar has permission to invoke methods on FooBar

<br><br>
Authentication errors must be handled gracefully.
<br>
Permission exceptions are handled gracefully.


## :anchor: Installation

```sh
git clone https://github.com/hsaade-algo/DRF-Neil.git
cd drf-neil
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt


# To start the server:
python manage.py runserver
```





<br>

[Hussein Saade][website]






[website]: https://maranello.hopto.org