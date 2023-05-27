# ejatlas

## Requirements

python 3.7 or greater
pip
virtualenv

## Install and activate virtualenv
Installing pip and virtualenv:

```
python3 -m pip install --upgrade pip
pip3 install virtualenv
```

Creating virtualenv:
```
virtualenv -p /home/username/opt/python-3.10.1/bin/python3 venv
```

virtualenv activation
```
source venv/bin/activate
```

After virtualenv activation you can install the libraries required 

## Requirements

In the projec's root is the requirements.txt. In this file are defined the whole libraries required by the project. To install them:
```
pip install -r requirements.txt
```

## Project configuration

The project has several configuration files regarding the environment:

- ejatlas/settings/base.py: Base project configurations 
- ejatlas/settings/local.py: Local configurations 
- ejatlas/settings/development.py: Development config
- ejatlas/settings/prodcution.py: Prod config

## Local environment

To work in local environment it will be necessary to modify these files:

ejatlas/settings/local.py: 

- Database configuration (using sqlite3 as base)
- Mail configuration: it will be necessary to populate to send mails during development

manage.py

- On local environment it will be necessary set on `manage.py` the correct `settings.py`

```
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejatlas.settings.local')
```

## Initializing and updating the database

To set the models in database
```
    python manage.py makemigrations
    python manage.py migrate
```

## Execution on local

```
    python manage.py runserver 0.0.0.0:8001
```

## Run Django tasks

```shell
export PYTHONPATH=$PWD/ejatlas
export DJANGO_SETTINGS_MODULE=ejatlas.settings.development

django-admin
```

## Conecting to PostGIS database in development

First, you will need install and configure Postgis in your environment. We recommend to use PostGIS on Docker. 

Then you will need to change the databases configuration to adapt it to use PostGIS.

In `development.py` you will need to set the database connection:

```python
DATABASES = {
     'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'ejatlas_devel',
         'USER': 'ejatlas',
         'PASSWORD': 'ejatlas',
         'HOST': 'localhost',
         'PORT': '5432'
     }
}
```

You will need get installed correct version of GDAL. We recommend to use Conda to manage Python dependencies and GDAL.
To install GDAL in Conda environments, after conda environment creation:

```shell
conda activate <the_conda_environment_name>
conda install -c conda-forge gdal
```

Now you will need install the POSTGIS extension into the database:

```sql
CREATE EXTENSION POSTGIS;
```
## How to generate a new version

Install `auto-changelog`

```shell
npm install -g auto-changelog
```

create a new release using `bump2version`:

```shell
bump2version --current-version 0.0.2 minor
```

where:

- `--current-version 0.0.2` is the current version set in `setup.py`
- `minor` is the type of release: `major`, `minor` or `patch`

This command will update the `setup.py`, `setup.cfg` and the `client/package.json` files with the new version.

Then, it will generate a new commit with the message `Bump version: {current_version} → {new_version}` and a new tag with the version number.

Now you will need to update the `CHANGELOG.md` and add it to the commit created by `bump2version`.

```shell
auto-changelog --template keepachangelog

git add CHANGELOG.md
git commit --amend --no-edit
```

Finally, push the new commit and tag to the remote repository:

```shell
git push --follow-tags
```

## Installing and configure pre-commit

Install pre-commit:

```shell
pip install pre-commit
```

Install pre-commit hooks:

```shell
pre-commit install
```
