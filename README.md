Stock app.

# Installation

## Prerequisites

```
python3.6
```

## Setup

To install other requirements first create python env and then use:

#### Python

```
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements/local.txt
```

#### Django

To configure database copy `db.base.py` file and rename it to `db.py` and add your settings.
Then migrate migrations with:

```
./manage.py migrate
./manage.py createsuperuser
```

### Javascript
To install javascript dependencies and build static files.

```
npm install
npm run build
```

To run use:

```
./manage.py runserver
```

# Authors
Team Yuml
