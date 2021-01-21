# The-PyBo

## Preview

![QuestionListView](./assets/QuestionListView.jpg)  

![QuestionDetailView](./assets/QuestionDetailView.jpg)  
 
## Create Cloud Instance 
1. [Create AWS lightsail instance & static IP][1]
   
## Dev setting for Django
1. Set timezone to Asia/Seoul
    - `sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime`
1. `sudo apt update`
1. `sudo apt install python3-venv`
1. `mkdir projects & mkdir venvs`
1. `cd projects & git clone https://github.com/hwanseok-dev/The-PyBo.git mysite`
1. `cd ../venvs`
1. Create venv name with mysite
   - `python3 -m venv mysite`
1. `cd mysite/bin`
1. `. activate`

## Install prerequisites
1. `pip install wheel`
1. `pip install django==3.1.3`
   - If you got stuck with some errors, try follow belows.
        1. `sudo apt-get install python3-pip`
        1. `pip3 install psycopg2`
        1. `pip3 install django==3.1.3`
1. `pip install markdown`

## Create postgreSQL database in instance

1. Change user
    - `su - postgres`
1. `CREATE DATABASE mysite;`
1. `CREATE USER user_id WITH PASSWORD 'password';`
1. `ALTER ROLE user_id SET client_encoding TO 'utf8';`
1. `ALTER ROLE user_id SET default_transaction_isolation TO 'read committed'`; 
1. `ALTER ROLE user_id SET TIME ZONE 'Asia/Seoul';`
1. `GRANT ALL PRIVILEGES ON DATABASE mysite To user_id;`
1. Make `dev_settings.py` in root directory
    ```python
    # /dev_settings.py
    SECRET_KEY = '*************************'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '*********',
            'USER': '*********',
            'PASSWORD': '*******',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```

## Launch Project in instance console

1. Activate venv
1. `cd projects/mysite`
1. `python manage.py migrate`
1. Make sure the static IP address is set as [here][2]
1. `python manage.py runserver 0:8000`

# Reference

[Do it! 점프 투 장고][1]

[1]: https://wikidocs.net/75559
[2]: https://github.com/hwanseok-dev/The-PyBo/blob/master/config/settings.py#L24