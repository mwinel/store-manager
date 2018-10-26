[![Build Status](https://travis-ci.org/mwinel/store-manager.svg?branch=develop)](https://travis-ci.org/mwinel/store-manager)    [![Coverage Status](https://coveralls.io/repos/github/mwinel/store-manager/badge.svg?branch=ch-coveralls-161271860)](https://coveralls.io/github/mwinel/store-manager?branch=develop)    [![Maintainability](https://api.codeclimate.com/v1/badges/91a97110a33301d5a42f/maintainability)](https://codeclimate.com/github/mwinel/store-manager/maintainability)

# store-manager
This application helps store owners avoid selling products that have run out of stock.

### Installation and Set Up

Clone the repo from GitHub:

https://github.com/mwinel/store-manager.git

Create and activate virtualenv

```
python3 -p venv sm-venv
source sm-venv/bin/activate
```

Install necessary requirements

```
pip install -r requirements.txt
```

Run the app and access the application at the address **http://localhost:5000/**

```
python3 manage.py runserver
```

Run unit tests

```
python3 manage.py tests
```

Index;
```

http GET http://localhost:5000/api/v1/index

HTTP/1.0 200 OK
Content-Length: 45
Content-Type: application/json
Date: Fri, 26 October 2018 11:06:36 GMT
Server: Werkzeug/0.14.1 Python/3.6.5

{
    "message": "Welcome to Store Manager"
}

```

### API Endpoints

| Resource URL | Methods | Description | Requires Auth |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/index` | `GET`  | The index | `FALSE` |
| `/api/v1/auth/admin/signup` | `POST`  | Admin Signup | `FALSE` |
| `/api/v1/auth/admin/login` | `POST`  | Admin Login | `TRUE` |
| `/api/v1/auth/signup` | `POST`  | Attendant Signup | `FALSE` |
| `/api/v1/auth/login` | `POST`  | Attendant Login | `TRUE` |
| `/api/v1/products` | `POST`  | Add product | `TRUE` |
| `/api/v1/products` | `GET`  | Fetch products | `TRUE` |
| `/api/v1/products/<id>` | `GET`  | Fetch product | `TRUE` |
| `/api/v1/sales` | `POST`  | Add sale | `TRUE` |
| `/api/v1/sales` | `GET`  | Fetch sales | `TRUE` |
| `/api/v1/sales/<id>` | `GET`  | Fetch sale | `TRUE` |

### Contribution

[See how to contribute.]()
