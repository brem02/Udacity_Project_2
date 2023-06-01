[![Build Status](https://dev.azure.com/odluser234748/Udacity_AzureDevops-P2/_apis/build/status%2Fbrem02.Udacity_Project_2?branchName=main)](https://dev.azure.com/odluser234748/Udacity_AzureDevops-P2/_build/latest?definitionId=1&branchName=main)

# Udacity_Project_2
Building a CI/CD Pipeline


## Overview

In this project, you will build a Github repository from scratch and create a scaffolding that will assist you in performing both, Continuous Integration and Continuous Delivery. You will use Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle. After that, you will integrate this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.
The project builds a python web application (using Flask and sklearn) and deploys it using Azure App Services. It is designed to predict housing prices in Boston. This GitHub repository will enable you to do the following:

- Deploy the app in Azure CloudShell
- Deploy the app as an Azure App Service
- Perform Load-Test against application

Commits to the GitHub repo trigger automated code testing using GitHub Actions. A pipeline has been created in Azure DevOps, and the updated code is also automatically tested in Azure DevOps and deployed to the Azure App Service.

Architecture overview:

![architectural-diagram](https://github.com/brem02/Udacity_Project_2/assets/122722304/f55f537e-b9d2-4ba0-8f18-62e2028292a7)


## Project Plan

It is important to have an effective project plan and task tracking. In this section you can find:

* Trello Board, see https://trello.com/b/m3tTf7w3/udacity-building-ci-cd-pipeline 
* Spreadsheet including original and final project plan:


## Instructions

### Deploy the app in Azure Power/Cloud Shell
&emsp;

***- Create a new repository:***

![Create_New_Repository](https://github.com/brem02/Udacity_Project_2/assets/122722304/64add23b-e27b-4435-8b49-b2736b1fb500)

&emsp;

***- Go to the azure portal (portal.azure.com) in your browser and open power or cloud shell:*** 

![Open_Cloud_Shell](https://github.com/brem02/Udacity_Project_2/assets/122722304/c5b8cdc6-8802-48e8-ae03-a8544b81494a)

&emsp;
   
***- Generate, copy and add SSH-Key in Github***

![Generate_SSH_Key](https://github.com/brem02/Udacity_Project_2/assets/122722304/21a98664-c304-4106-a02f-30b29115a14e)

![Copying_SSH_Key](https://github.com/brem02/Udacity_Project_2/assets/122722304/54f5b218-c7b5-44b8-b123-5f5ba5cf2483)

![Add_SSH_Key_in_Github](https://github.com/brem02/Udacity_Project_2/assets/122722304/7ca8ab72-e010-4c24-90f0-0dcfe1287b42)

&emsp;

***- Clone the repo with git clone https://github.com/brem02/Udacity_Project_2.git***

![Cloning_Project_into_Azure_Cloud_Shell](https://github.com/brem02/Udacity_Project_2/assets/122722304/5820860f-67ca-4a0c-b124-4866ddec5b95)

&emsp;

***- Generate necessary files in Project:***

![Generate_Files_in_Project](https://github.com/brem02/Udacity_Project_2/assets/122722304/0ac5929e-8e16-4767-9281-eaaa1b0738dd)

&emsp;

***- Define hello.py via bash editor***

![Define_Hello_py](https://github.com/brem02/Udacity_Project_2/assets/122722304/bcb86d82-3f58-461b-be88-f9ae1488a9e8)

&emsp;

***- Define test_hello.py***

![Define_test_Hello_py](https://github.com/brem02/Udacity_Project_2/assets/122722304/a3c5ada9-8088-4ec4-994b-e7efce67334d)

&emsp;

***- Define requirements.txt***

![Define_requirements_txt](https://github.com/brem02/Udacity_Project_2/assets/122722304/6fd94cb7-5d0b-4ee6-a7c7-cd5b6ef737da)

&emsp;

***- Prepare Makefile in Visual Studio***

![Prepare_Makefile_in_Visual_Studio_with_Tab](https://github.com/brem02/Udacity_Project_2/assets/122722304/063f3634-71e0-463d-b4b8-33dc1aa1c377)

&emsp;

***- Define Makefile***

![Define_Makefile](https://github.com/brem02/Udacity_Project_2/assets/122722304/355de6ba-c127-4dd5-974e-6d28ef92fdb4)

&emsp;

***- Push Files to Github:***

![Git_Push_Files](https://github.com/brem02/Udacity_Project_2/assets/122722304/175c821e-ab0f-4d58-b9c2-c216783756a8)

&emsp;

***- Result of Push:***

![Result_Git_Push_Files](https://github.com/brem02/Udacity_Project_2/assets/122722304/8dc1c48c-317a-4d08-aa46-628beb962620)


***- Create and Activate Virtual Environment***

![Creating_Virtual_Environment](https://github.com/brem02/Udacity_Project_2/assets/122722304/e919d00b-c175-414d-ab7c-4cc3ec582db5)

&emsp;

***- Install dependencies and run make all in the VM and check, if test has passed***

![Passing_Test_After_Make_All](https://github.com/brem02/Udacity_Project_2/assets/122722304/a7d8998f-9e44-4a38-92cb-89e212ec14b3)

&emsp;

***- Validate application in the VM before deploying it to Azure App Service. In a new Cloud Shell go to your repo and start locally the file make_prediction.sh***
&emsp;
```
bash ./make_prediction.sh
```
&emsp;

![Test_Application_Locally_Make_Prediction](https://github.com/brem02/Udacity_Project_2/assets/122722304/a07330f8-4e48-4877-81a6-abdd90529b51)

&emsp;

***- Get Started with Github Actions by clicking on 'Actions', then click on "set up a workflow yourself' and use the GitHub Actions yaml file .github/workflows/pythonapp.yml as a template:***

![Get_Started_With_GitHub_Actions](https://github.com/brem02/Udacity_Project_2/assets/122722304/78a882fc-0a49-411a-a363-7c91a46756d1)

![Create_Pythonapp_yml](https://github.com/brem02/Udacity_Project_2/assets/122722304/f383c9d2-88f5-4027-b79e-44ae07fd6cf7)

&emsp;

***- Once the workflow is created (detailed steps for that will be provided in the 'Deploy the app to an Azure App Service' section right underneeth) it is automatically triggered and should show a Passing GitHub Actions Build:***

![Passing_GitHub_Actions_Build](https://github.com/brem02/Udacity_Project_2/assets/122722304/4e310c63-0db0-4a6b-974b-1b41bb348c99)


&emsp;

***- Git Clone Starter Code:***

![Git_Clone_Starter_Code](https://github.com/brem02/Udacity_Project_2/assets/122722304/db6df712-173e-463e-bf1e-ebb5da327e2a)

&emsp;

### Deploy the app to an Azure App Service

***Create an App Service in Azure. In this example the App Service is called uda-azuredevops-p2 and the resource group is called Azuredevops. In the first Cloud Console run the following command, the result takes a few minutes:"***

&emsp;

```
az webapp up --name uda-azuredevops-p2 --resource-group Azuredevops --sku B1 --logs --runtime "PYTHON:3.8
```
&emsp;

![Create_Web_App](https://github.com/brem02/Udacity_Project_2/assets/122722304/db51f2d1-dfe0-4b7a-ab2f-573a6332badf)

&emsp;

***- This is the webapp on the azure portal:***

![Web_App_Details](https://github.com/brem02/Udacity_Project_2/assets/122722304/a122a245-dae2-4b60-8887-970ac7659780)

&emsp;

***- Create and configure the pipeline in Azure DevOps. More information on this process can be found [here:(https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops&WT.mc_id=udacity_learn-wwl). The basic steps to set up the pipeline are:***
&emsp;
- Go to [https://dev.azure.com](https://dev.azure.com) and sign in.
- Create a new project.
- Under Project Settings create a new service connection to Azure Resource Manager, scoped to your subscription and resource group.
- Create a new pipeline (python to linux web app on azure) linked to your GitHub repo.
&emsp;
***In the following every step is described in more detail:***

&emsp;

***- Create a new project:***

![Create_New_Project_in_Azure_DevOps](https://github.com/brem02/Udacity_Project_2/assets/122722304/25dbeddc-fe7d-4144-93a0-c97ef0307ed2)

&emsp;

***- Create a new Service Connection:***

![Service_Connection](https://github.com/brem02/Udacity_Project_2/assets/122722304/e4d91066-aecd-4e79-9fd8-d9033d4defee)

&emsp;

***- Create Pipeline:***

![Create_Azure_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/16dbc62b-6c38-4ac7-928c-6c0f268e0e4e)

&emsp;

***- Edit Pipeline:***

![Edit_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/6a43d1cc-f2dc-49a0-bb6d-e49defe74c12)

&emsp;

***-Build Pipeline:***

![Build_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/b649761e-2aa4-4e38-8fb5-0f181cb0f635)

&emsp;

***- Create Environment:***

![Create_New_Environment](https://github.com/brem02/Udacity_Project_2/assets/122722304/545d0f34-25ef-45a3-8daf-dd70b46a709b)

&emsp;

***- Create Agent Pool:***

![Create_Agent_Pool](https://github.com/brem02/Udacity_Project_2/assets/122722304/21d0f65d-e4b0-423d-9788-298bc607592e)

&emsp;

***- Create Virtual Machine:***

![Create_Virtual_Machine](https://github.com/brem02/Udacity_Project_2/assets/122722304/4fbf382d-ea2d-461a-a2e6-5531aeed2651)

&emsp;

***- Virtual Machine Details:***

![Virtual_Machine_Details](https://github.com/brem02/Udacity_Project_2/assets/122722304/990b4b31-76ea-4ffb-a7de-d2742ac7f240)

&emsp;

***- Configure Virtual Machine --> Install Docker:***

![Configure_VM_Install_Docker](https://github.com/brem02/Udacity_Project_2/assets/122722304/80cfc6b2-b40f-49ac-a3c9-384d6ab905bc)

&emsp;

***- Create new Agent:***

![Create_New_Agent](https://github.com/brem02/Udacity_Project_2/assets/122722304/70e4ca46-414a-4cf9-9ad8-2e290f89e189)

&emsp;

***- Configure Virtual Machine --> Install Agent Services:***

![Configure_VM_Install_Agent_Services](https://github.com/brem02/Udacity_Project_2/assets/122722304/9dac8139-ff3b-4119-8094-ab284f78eddd)

&emsp;

***- Check, if Agent has been registered:***

![Agent_Registered](https://github.com/brem02/Udacity_Project_2/assets/122722304/28b0046c-3680-44d3-9755-ba17071e538d)

&emsp;

***- Run Pipeline:***

![Run_Pipeline](https://github.com/brem02/Udacity_Project_2/assets/122722304/eef18c0e-4c85-4344-93aa-e604095ae745)

&emsp;

***- WebApp has been started:***

![Run_Web_App](https://github.com/brem02/Udacity_Project_2/assets/122722304/ed04a4a8-f2a7-448c-a22a-ff0c2b2eca6c)

&emsp;

***- WebApp Result:***

![Web_App_Result](https://github.com/brem02/Udacity_Project_2/assets/122722304/f2f12e75-2c81-4e60-8476-f3eee5b89f93)

&emsp;

***- WebApp Result, if you change the python file app.py:***

![Web_App_Result_Test_Change](https://github.com/brem02/Udacity_Project_2/assets/122722304/4ce4d603-daf1-4497-9258-1a2fa9093afd)

&emsp;


***-WebApp Logs:***

![Web_App_Log_1](https://github.com/brem02/Udacity_Project_2/assets/122722304/a4a6e700-c5c6-4ee4-9e11-9c7a6005435d)
![Web_App_Log_2](https://github.com/brem02/Udacity_Project_2/assets/122722304/2f2ba5de-4cac-4774-a3a3-b702ab02a77e)
![Web_App_Deploy_Log](https://github.com/brem02/Udacity_Project_2/assets/122722304/84a44970-72f2-4cc0-8daa-c2a20e6cf036)
![Application_Log](https://github.com/brem02/Udacity_Project_2/assets/122722304/bfe0201d-722b-496c-bc90-db21f66b8c78)

&emsp;

***- Test the App by editing the make_predict_azure_app.sh script with your DNS name of your app 
***- Run the following commands:

```
make setup 
```
```
make all
```
```
python app.py 
```
&emsp;

***- Running it on Cloud Shell in a separate terminal window:***

```
bash ./make_predict_azure_app.sh 
```
![Test_Application_AzureAppService_make_predict_azure_app](https://github.com/brem02/Udacity_Project_2/assets/122722304/27b8c339-3377-4856-bb92-f78e53f77c87)

&emsp;

### Load Test

***-Performance validation of the webapp can be performed via a load test using locust. 
Replace the webapp name accordingly in the provided locustfile.py and call locust:***
&emsp;

***Install Locust:***
```
pip3 install locust
```
&emsp;
***Check Installation***
```
locust -V
```
&emsp;
***Run Locust File:***
```
locust -f locustfile.py --host https://uda-azuredevops-p2.azurewebsites.net/  --headless -u 20 -r 5 -t 20s
```
&emsp;
Using these parameters above locust will use 20 users with a spawn rate of 5 users per second and run for 20 seconds.

&emsp;

***- Locust Run:***
&emsp;
![Locust_Run_01](https://github.com/brem02/Udacity_Project_2/assets/122722304/d8aeab4c-2c0b-4940-82f8-48727fe02975)
![Locust_Run_02](https://github.com/brem02/Udacity_Project_2/assets/122722304/f8fcdce2-d917-4d1c-8803-13e00ebc5bce)
![Locust_Run_03](https://github.com/brem02/Udacity_Project_2/assets/122722304/d6fd9b3b-4c11-4a30-8dda-88b0d362e1ac)
&emsp;

***Run Locust File locally and use Locust UI:***
&emsp;
- Install Python: .\python-3.11.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
- Install Locust: pip3 install locust
- Check Version: locust -V
- Run local Locust-File: 
  ```
  locust
  ```
  
***- Locust Run:***
&emsp;
![Locust_Run_UI](https://github.com/brem02/Udacity_Project_2/assets/122722304/149ed36a-5943-485a-9185-683ad80cda86)
&emsp;

- Open a browser and go to http://localhost:8089. Enter the total number of users to simulate, enter the spawn rate, set the host https://uda-azuredevops-p2.azurewebsites.net/ and click Start Swarming:

&emsp;
![Locust_UI_01](https://github.com/brem02/Udacity_Project_2/assets/122722304/13307ae9-a95a-454b-ad0d-f97725341b86)
![Locust_UI_02](https://github.com/brem02/Udacity_Project_2/assets/122722304/21f73960-61f6-40ed-9d7e-a49dfe9f5fbf)
&emsp;

## Extra-Screenshots

You can see the screenshot of a successful Azure Pipeline Run:

![image](https://github.com/brem02/Udacity_Project_2/assets/122722304/74d56f34-df06-452e-9ddd-5e96b6d620d3)

&emsp;

## Enhancements

In the future, the project can be configured to work with gitflow, so if you commit to a particular branch, the code can continue to be deployed in the corresponding environment (Development, QA, Staging or production).
&emsp;

## Annotations

- In the main branch there is a command.txt file, which includes all relevant commands to set up the environment for this project. Moreover, it contains also the steps to do the set up. 
- the command python3 -m pip install pandas in the azure-pipelines.yml is necessary, because the according entry in requirements.txt was not processed correctly under python 3.8 --> the tutor has opened up a bug
&emsp;

## Demo 

This is the [youtube](https://youtu.be/xQezqOopooQ) link to see a demo

