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



## Deploy the app to an Azure App Service
Now is time to deploy the app to an azure app service...

Create an App Service in Azure. In this example the App Service is called jose-flaskpipelines and the resource group is called jose-udacity-project. In the first Cloud Console run the follow command, the result take a few minutes:

```
az webapp up -n jose-flaskpipelines -g jose-udacity-project
```
![create-webapp](evidence/screenshot-create-webapp.PNG)

This is the webapp on the azure portal:
![webapp](evidence/screenshot-webapp.PNG)

Next, create and configure the pipeline in Azure DevOps. More information on this process can be found [here](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops&WT.mc_id=udacity_learn-wwl). The basic steps to set up the pipeline are:

- Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
- Create a new private project.
- Under Project Settings create a new service connection to Azure Resource Manager, scoped to your subscription and resource group.
- Create a new pipeline (python to linux web app on azure)linked to your GitHub repo.


![azure-pipeline](evidence/screenshot-azure-pipeline.PNG)


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

