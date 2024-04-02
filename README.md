# Backend <!-- omit in toc -->
# <!-- omit in toc -->
## Django backend for the AppTonomia Sirio application <!-- omit in toc -->
# <!-- omit in toc -->
![Python](https://img.shields.io/badge/python-3.10.-blue) ![Django](https://img.shields.io/badge/Django-4.x-blue) ![Rest Framework](https://img.shields.io/badge/RestFramework-4.x-blue) ![License](https://img.shields.io/badge/license-GNU-green)
# <!-- omit in toc -->
### Table of Contents <!-- omit in toc -->
- [About](#about)
- [Development Guide](#development-guide)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Authors and Contributors](#authors-and-contributors)
- [Code of Conduct](#code-of-conduct)
- [Change Log](#change-log)

### About
This is the backend for the AppTonomia Sirio application. It is a Django project that uses the Django Rest Framework to provide a REST API for the application.

### Development Guide
The development guide can be found in the [docs](docs) folder.

### Installation
To install the project, follow these steps:

1. Clone the repository
```
git clone https://github.com/AppTonomia-Sirio/Backend.git
```
2. Create a virtual environment
```
poetry shell
```
3. Install the requirements
```
poetry install
```
4. Configure and start postgresql
```
sudo -u postgres psql
```
```
CREATE DATABASE siriodb;
```
```
CREATE ROLE django WITH SUPERUSER LOGIN PASSWORD 'django';
```
```
GRANT ALL PRIVILEGES ON DATABASE siriodb TO django;
```

5. Run the migrations
```
python manage.py migrate
```
6. Create a superuser
```
python manage.py createsuperuser
```
7. Run the tests
```
python manage.py test
```
9. Run the server
```
python manage.py runserver
```
10. Compile the localization files
```
python manage.py compilemessages
```

### Usage
See the [API Documentation](docs/API_DOCS.md).

### License
This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.

### Authors and Contributors
- [**Fedor Kunin**](https://www.linkedin.com/in/fedor-kunin-015b9b254/)
- [**Adrián Puyet Muñoz**](https://github.com/Rowiz49)

### Code of Conduct

### Change Log




