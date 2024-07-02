# Intro

- for this homework asignment I chose Python+Flask
- pytest as testing tool
- application factory method for Flask structure, as it would be better suitable for testing and production env also


# Application: how to run locally

- clone repo and `cd` into `homework` directory
- activate virtual environment `python -m venv .`
`.\Scripts\activate` (this command is for windows)
- in `homework` directory run `pip install -r requirements.txt` (generated with `pip freeze`)
- in `homework` directory run `flask run`
- to run app enter url `http://127.0.0.1:5000/12` where 12 is nth index of the series


# Tests: how to run locally

- to run tests enter `cd .\fibonaci_calc\` and `pytest`
- to add new tests go to `tests/test_app.py` and add new functions with first word as `test_`


# How service could be run in PROD environment

- One way to deploy the service is to store the code in Azure Repos and use CI/CD pipeline such as in AzureDevops and post it straight into Azure Web App.
- Another way is to build Docker image of the service and store it into cloud storage like Azure Container Registry. Test and prod environments could pull it from there into designated VMs or webservices.
- If the usage load is big Azure Kubernetes Services could be handy.
- If Fibonaci series higher indexes are required external database could be provisioned to serve precalculated values as
recursion in calculation file `fibonaci.py` takes long time for that purpose.
- Monitoring would need to be enabled for example Azure Application logging/web server logging for app's logs, and azure monitor for VMs. Logs could be stored in blob storage.
- since application factory method is chosen its posible to scale this single instance app service into multi-instanced app service using single Docker image.
- all neccesary secrets (e.g. database connections) should be stored securely in Keyvault.

