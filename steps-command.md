### 1. Login into azure account
    az login
### 2. creating resource group 
    az group create --name rg-acr-demo --location eastus
### 3. creating azure container registry 
    az acr create --resource-group rg-acr-demo --name marufacrdemo102126 --sku Basic
### 4. providing admin access right(Security Provision)
    az acr update --name marufacrdemo102126 --admin-enabled true
### 5. Login to acr 
    az acr login --name marufacrdemo102126

### 6. Building docker image 
        docker build -t marufuli707/marufacrdemo102126:1.0 . 
### 7 Tagging the docker image 
        docker tag marufacrdemo102126:1.0 marufacrdemo102126.azurecr.io/acr-demo-app:1.0 