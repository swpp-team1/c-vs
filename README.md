# convenience-store
review products and share your own recipe with convenience store

## Setting Virtual Environment for Django
### 1. install virtualenv
django의 python의 version과 다른 library의 version을 유지해주기 위하여 가상환경을 사용한다. virtualenv를 이용하여 python3을 기반으로 한 가상환경을 설치한다.
reference : [virtualenv]("https://virtualenv.pypa.io/en/latest/index.html")
### 2. install libraries
가상환경의 설치가 끝나면 설치후 python의 library들을 설치해줘야 한다.
 - `pip install django`
 - `pip install djangorestframework`
 - `pip install pillow` for image field
 - `pip install django-filter` for Filtering
