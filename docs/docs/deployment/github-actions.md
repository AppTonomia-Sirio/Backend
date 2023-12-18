# Desplegando la aplicación desde GitHub Actions en Azure App Service

Esta guía sirve para describir cómo se ha realizado la configuración para el despliegue automático de la aplicación en Azure App Service desde GitHub Actions.

- https://docs.github.com/es/actions/deployment/deploying-to-your-cloud-provider/deploying-to-azure/deploying-python-to-azure-app-service

1. Crear un plan de Azure (creo que ya está creado)
2. Crear una aplicación web (creo que ya está creada)
3. Configurar un perfil de publicación de Azure y crear un secreto AZURE_WEBAPP_PUBLISH_PROFILE

- https://learn.microsoft.com/es-es/azure/app-service/deploy-github-actions?tabs=applevel#generate-deployment-credentials

Ha sido entrar en la aplicación de AppService, en la pantalla principal hay una opción (menú superior, "Descargar perfil de publicación") que si le das descarga el fichero apptonomia.PublishSettings.

En el repositorio, vamos a Settings->Security->Secrets and variables->Actions, al botón New repository Secret.

El nombre del secreto es `AZURE_WEBAPP_PUBLISH_PROFILE`, y el valor es el contenido del fichero apptonomia.PublishSettings.

Indica "Agregue una configuración de aplicación denominada SCM_DO_BUILD_DURING_DEPLOYMENT y establezca el valor en 1." Ya estaba añadida, así que no he hecho nada.