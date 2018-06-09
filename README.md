# convenience-store
review products and share your own recipe with convenience store

[![Build Status](https://travis-ci.org/swpp-team1/c-vs.svg?branch=master)](https://travis-ci.org/swpp-team1/c-vs)

## Setting Virtual Environment for Django
### 1. install virtualenv
django의 python의 version과 다른 library의 version을 유지해주기 위하여 가상환경을 사용한다. virtualenv를 이용하여 python3을 기반으로 한 가상환경을 설치한다.
reference : [virtualenv](https://virtualenv.pypa.io/en/latest/index.html)
### 2. install libraries
가상환경의 설치가 끝나면 설치후 python의 library들을 설치해줘야 한다.
 - `pip install django`
 - `pip install djangorestframework`
 - `pip install pillow` for image field
 - `pip install django-filter` for Filtering

#### For Crawler
 - `pip install request`
 - `pip install bs4`

#### For Deploy
 - `pip install uwsgi`

### 3. Running Server
 - It needs secret folder .config_secret which is not in git hub
#### Debug
 - `python manage.py runserver --settings=config.settings.debug`

#### Deploy
 - `python manage.py runserver --settings=config.settings.deploy`

#### Setting files
 - `config/settings/base.py` and `cvs_server/settings.py` should be syncronized
