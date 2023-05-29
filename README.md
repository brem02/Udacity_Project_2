# Udacity_Project_2
Building a CI/CD Pipeline


Sections:
----------
Overview of the project

Architectural Diagram

Instructions for running the Python project

A short description of how to improve the project in the future

Screenshots demonstrating key steps

Badge


# Overview

In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both, Continuous Integration and Continuous Delivery. You will use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. After that, you will integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.


## Project Plan

It is important to have an effective project plan and task tracking. In this section you can find:

* Trello Board
* Spreadsheet including original and final project plan

## Instructions
![architectural-diagram](https://github.com/brem02/Udacity_Project_2/assets/122722304/f55f537e-b9d2-4ba0-8f18-62e2028292a7)


## Deploy the app in Azure Power/Cloud Shell


Create a new repository:

![Create_New_Repository](https://github.com/brem02/Udacity_Project_2/assets/122722304/64add23b-e27b-4435-8b49-b2736b1fb500)



Go to the azure portal (portal.azure.com) in your browser and open power or cloud shell: 

![Open_Cloud_Shell](https://github.com/brem02/Udacity_Project_2/assets/122722304/c5b8cdc6-8802-48e8-ae03-a8544b81494a)


Generate, copy and add SSH-Key in Github

![Generate_SSH_Key](https://github.com/brem02/Udacity_Project_2/assets/122722304/21a98664-c304-4106-a02f-30b29115a14e)

![Copying_SSH_Key](https://github.com/brem02/Udacity_Project_2/assets/122722304/54f5b218-c7b5-44b8-b123-5f5ba5cf2483)

![Add_SSH_Key_in_Github](https://github.com/brem02/Udacity_Project_2/assets/122722304/7ca8ab72-e010-4c24-90f0-0dcfe1287b42)


Clone the repo with git clone https://github.com/brem02/Udacity_Project_2.git

![Cloning_Project_into_Azure_Cloud_Shell](https://github.com/brem02/Udacity_Project_2/assets/122722304/5820860f-67ca-4a0c-b124-4866ddec5b95)


Generate necessary files in Project:

![Generate_Files_in_Project](https://github.com/brem02/Udacity_Project_2/assets/122722304/0ac5929e-8e16-4767-9281-eaaa1b0738dd)


Define hello.py via bash editor

![Define_Hello_py](https://github.com/brem02/Udacity_Project_2/assets/122722304/bcb86d82-3f58-461b-be88-f9ae1488a9e8)


Define test_hello.py

![Define_test_Hello_py](https://github.com/brem02/Udacity_Project_2/assets/122722304/a3c5ada9-8088-4ec4-994b-e7efce67334d)


Define requirements.txt

![Define_requirements_txt](https://github.com/brem02/Udacity_Project_2/assets/122722304/6fd94cb7-5d0b-4ee6-a7c7-cd5b6ef737da)


Prepare Makefile in Visual Studio

![Prepare_Makefile_in_Visual_Studio_with_Tab](https://github.com/brem02/Udacity_Project_2/assets/122722304/063f3634-71e0-463d-b4b8-33dc1aa1c377)


Define Makefile

![Define_Makefile](https://github.com/brem02/Udacity_Project_2/assets/122722304/355de6ba-c127-4dd5-974e-6d28ef92fdb4)


Create and Activate Virtual Environment

![Creating_Virtual_Environment](https://github.com/brem02/Udacity_Project_2/assets/122722304/e919d00b-c175-414d-ab7c-4cc3ec582db5)


Install dependencies and run make all in the VM and check, if test has passed

![Passing_Test_After_Make_All](https://github.com/brem02/Udacity_Project_2/assets/122722304/a7d8998f-9e44-4a38-92cb-89e212ec14b3)


Deactivate Virtual Environment

![Deactivate_Virtual_Environment](https://github.com/brem02/Udacity_Project_2/assets/122722304/abbff754-5940-488b-bced-d40341863cfe)


In order to validate the application before deploy to app service, start the application in the virtual environment:
```
python app.py
```
![python-app](evidence/screenshot-python-app.PNG)

Open other Cloud Shell:
![new-cloud-shell](evidence/screenshot-new-cloud-shell.PNG)

In the new Cloud Shell, go to the repository directory and test that the app is working:
```
cd Building-a-CI-CD-Pipeline
./make_prediction.sh
```
![local-prediction](evidence/screenshot-local-prediction.PNG)

Close the second cloud console, and press "Ctrl + c" to stop the local app in the first console:

![stop-app](evidence/screenshot-stop-app.PNG)


Push Files to Github:

![Git_Push_Files](https://github.com/brem02/Udacity_Project_2/assets/122722304/175c821e-ab0f-4d58-b9c2-c216783756a8)


Result of Push:

![Result_Git_Push_Files](https://github.com/brem02/Udacity_Project_2/assets/122722304/8dc1c48c-317a-4d08-aa46-628beb962620)


Get Started with Github Actions:

![Get_Started_With_GitHub_Actions](https://github.com/brem02/Udacity_Project_2/assets/122722304/78a882fc-0a49-411a-a363-7c91a46756d1)


Create Pythonapp.yml

![Create_Pythonapp_yml](https://github.com/brem02/Udacity_Project_2/assets/122722304/f383c9d2-88f5-4027-b79e-44ae07fd6cf7)


Passing GitHub Actions Build:

![Passing_GitHub_Actions_Build](https://github.com/brem02/Udacity_Project_2/assets/122722304/4e310c63-0db0-4a6b-974b-1b41bb348c99)


Git Clone Starter Code:

![Git_Clone_Starter_Code](https://github.com/brem02/Udacity_Project_2/assets/122722304/db6df712-173e-463e-bf1e-ebb5da327e2a)



## Deploy the app to an Azure App Service

Create an App Service in Azure. In this example the App Service is called uda-azuredevops-p2 and the resource group is called Azuredevops. In the first Cloud Console run the follow command, the result takes a few minutes:

az webapp up --name uda-azuredevops-p2 --resource-group Azuredevops --sku B1 --logs --runtime "PYTHON:3.8"

![Create_Web_App](https://github.com/brem02/Udacity_Project_2/assets/122722304/db51f2d1-dfe0-4b7a-ab2f-573a6332badf)


This is the webapp on the azure portal:

![Web_App_Details](https://github.com/brem02/Udacity_Project_2/assets/122722304/a122a245-dae2-4b60-8887-970ac7659780)



Create and configure the pipeline in Azure DevOps. More information on this process can be found [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops&WT.mc_id=udacity_learn-wwl). The basic steps to set up the pipeline are:

- Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
- Create a new project.
- Under Project Settings create a new service connection to Azure Resource Manager, scoped to your subscription and resource group.
- Create a new pipeline (python to linux web app on azure) linked to your GitHub repo.

In the following every step is described in more detail:


Create a new project:

![Create_New_Project_in_Azure_DevOps](https://github.com/brem02/Udacity_Project_2/assets/122722304/25dbeddc-fe7d-4144-93a0-c97ef0307ed2)


Create a new Service Connection:

![Service_Connection](https://github.com/brem02/Udacity_Project_2/assets/122722304/e4d91066-aecd-4e79-9fd8-d9033d4defee)


Create Pipeline:

![Create_Azure_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/16dbc62b-6c38-4ac7-928c-6c0f268e0e4e)


Edit Pipeline:

![Edit_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/6a43d1cc-f2dc-49a0-bb6d-e49defe74c12)



Build Pipeline:

![Build_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/b649761e-2aa4-4e38-8fb5-0f181cb0f635)



Create Environment:

![Create_New_Environment](https://github.com/brem02/Udacity_Project_2/assets/122722304/545d0f34-25ef-45a3-8daf-dd70b46a709b)


Create Agent Pool:

![Create_Agent_Pool](https://github.com/brem02/Udacity_Project_2/assets/122722304/21d0f65d-e4b0-423d-9788-298bc607592e)


Create Virtual Machine:

![Create_Virtual_Machine](https://github.com/brem02/Udacity_Project_2/assets/122722304/4fbf382d-ea2d-461a-a2e6-5531aeed2651)



Virtual Machine Details:

![Virtual_Machine_Details](https://github.com/brem02/Udacity_Project_2/assets/122722304/990b4b31-76ea-4ffb-a7de-d2742ac7f240)


Configure Virtual Machine --> Install Docker:

![Configure_VM_Install_Docker](https://github.com/brem02/Udacity_Project_2/assets/122722304/80cfc6b2-b40f-49ac-a3c9-384d6ab905bc)


Create new Agent:

![Create_New_Agent](https://github.com/brem02/Udacity_Project_2/assets/122722304/70e4ca46-414a-4cf9-9ad8-2e290f89e189)


Configure Virtual Machine --> Install Agent Services:

![Configure_VM_Install_Agent_Services](https://github.com/brem02/Udacity_Project_2/assets/122722304/9dac8139-ff3b-4119-8094-ab284f78eddd)


Check, if Agent has been registered:

![Agent_Registered](https://github.com/brem02/Udacity_Project_2/assets/122722304/28b0046c-3680-44d3-9755-ba17071e538d)


Run Pipeline:

![Run_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/eef18c0e-4c85-4344-93aa-e604095ae745)


WebApp has been started:

![Run_Web_App](https://github.com/brem02/Udacity_Project_2/assets/122722304/ed04a4a8-f2a7-448c-a22a-ff0c2b2eca6c)


WebApp Result:

![Web_App_Result](https://github.com/brem02/Udacity_Project_2/assets/122722304/f2f12e75-2c81-4e60-8476-f3eee5b89f93)


WebApp Logs:

![Web_App_Log_1](https://github.com/brem02/Udacity_Project_2/assets/122722304/a4a6e700-c5c6-4ee4-9e11-9c7a6005435d)
![Web_App_Log_2](https://github.com/brem02/Udacity_Project_2/assets/122722304/2f2ba5de-4cac-4774-a3a3-b702ab02a77e)
![Web_App_Deploy_Log](https://github.com/brem02/Udacity_Project_2/assets/122722304/84a44970-72f2-4cc0-8daa-c2a20e6cf036)
![Application_Log](https://github.com/brem02/Udacity_Project_2/assets/122722304/bfe0201d-722b-496c-bc90-db21f66b8c78)


Locust Run:

![Locust_Run_01](https://github.com/brem02/Udacity_Project_2/assets/122722304/d8aeab4c-2c0b-4940-82f8-48727fe02975)
![Locust_Run_02](https://github.com/brem02/Udacity_Project_2/assets/122722304/f8fcdce2-d917-4d1c-8803-13e00ebc5bce)
![Locust_Run_03](https://github.com/brem02/Udacity_Project_2/assets/122722304/d6fd9b3b-4c11-4a30-8dda-88b0d362e1ac)



Now, we can test the app. For you case, edit the line 28 of the make_predict_azure_app.sh script with the DNS name of your app. Then run the script on the cloud shell:

```
./make_predict_azure_app.sh 
```
![webapp-prediction](evidence/screenshot-webapp-prediction.PNG)


If you like, you can go to the webapp url:

![webapp-url](evidence/screenshot-webapp-url.PNG)

And view the logs with the following command:
```
az webapp log tail -n jose-flaskpipelines -g jose-udacity-project
```
![webapp-logs](evidence/screenshot-webapp-logs.PNG)

## Load Test

We can use locust to do a load test against our application. In this example we will do a load test against the app running in azure rather than locally.

Install locust and then run locust:
```
pip install locust
locust
```
![locust](evidence/screenshot-install-locust.PNG)

Open a browser and go to http://localhost:8089. Enter the total number of users to simulate, spawn rate, set the host to https://jose-flaskpipelines.azurewebsites.net/, and click Start Swarming:

![locust](evidence/screenshot-locust-a.PNG)

![locust](evidence/evidence-screenshot-showing-locust-test.PNG)

## Extra-Screenshots

You can see screenshot of a successful GitHub build test run, at github actions:
![webapp-logs](evidence/evidence-screenshot-showing-passing-github-actions.PNG)

## Enhancements

In the future, the project can be configured to work with gitflow, so if you commit to a particular branch, the code can continue to be deployed in the corresponding environment (Development, QA, Staging or production).

## Demo 

This is the [youtube](https://youtu.be/xQezqOopooQ) link to see a demo

