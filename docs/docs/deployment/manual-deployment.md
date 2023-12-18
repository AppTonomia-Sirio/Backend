# Deploying the Django Backend on Azure App Service

In this guide, we will go through the steps required to deploy a Django
backend on an Azure Platform as a Service (PaaS). This guide follows the
Microsoft training available at
<https://learn.microsoft.com/es-es/training/modules/django-deployment/>,
albeit shorter and straight to the point (and tested). It also includes
the peculiarities of the AppTonomia project instead of working with a
dummy project.

This document assumes the use of a GNU/Linux operating system and the
VisualStudio Code IDE, but operations can be carried out from other
platforms and with other tools (or the command line). If you know how to
do it or do it, please document it here so that we can all learn.

## Paso 1: Project download and installation

The backend of the application is hosted at
<https://github.com/AppTonomia-Sirio/Backend>. Clone this repository to
your local machine and navigate to the root directory of the Django
project.

```bash
git clone git@github.com:AppTonomia-Sirio/Backend.git && cd Backend/app
```

The project manages Python dependencies through poetry. To install
poetry on our system, we'll follow the instructions from the
[official documentation](https://python-poetry.org/docs/#installation).
In summary, execute the following command:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Once poetry is installed, install the project dependencies with the command:

```bash
poetry install
```

Now, all the project dependencies are installed in a Python virtual
environment with the correct versions.

Lastly, verify that the project works correctly by launching Django's
development server:

```bash
poetry run python manage.py runserver
```

If you can access <localhost:8000> and see Django's welcome page,
everything is in order.

## Step 2: Installing Azure Extensions for Visual Studio Code

Deployment can be done in several different ways. One of them is from
Visual Studio Code using specific extensions. Since we are using Azure
App Service for the application and Azure Database for PostgreSQL for
the database, we'll install two specific extensions handling these:

- [Azure App Service](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azureappservice)
- [Azure Databases](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-cosmosdb)

With these two tools, we can deploy the application and ensure that the database is correctly created and updated.

## Paso 3: Añadir los recursos de Azure a VisualStudio Code


With the extensions, we can connect Azure resources to our IDE, and from
there we can deploy the application and access its information (and the
database's).

To do this, open the Azure tab and click on the _Sign in to Azure_
button. After authentication, we need to connect to the two resources we
created on Azure: The App Service application and the PostgreSQL
database. Both are done in their respective sections through the add key
or `+`.

After selecting both resources, we should see them in the Azure tab (the
backend under _App Services_ and the database under _PostgreSQL servers
(Flexible)_). In reality, for deployment, we'll only use App Services,
but the database will help us to check the correct migration of the
schema.

## Step 4: Application Deployment

As expected, this part is easy but still manual. The process is as
follows:

1. Right-click on the application under _App Services_ and select the
   option _Deploy to Web App..._.
2. Once deployed, and if it's necessary to update the database,
   right-click on the application under _App Services_ and select the
   option _SSH into Web App..._. Once inside, execute the command
   `python manage.py migrate` to update the database.


With this, the application will be deployed and available under the URL
<https://apptonomia.azurewebsites.net>.
