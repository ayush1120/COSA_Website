# Django Project


##### Install Anacoda
  - Install Anaconda (Make sure 'add path to environment/system variables' is checked)


##### Add environment
#
#
Use the Terminal or an Anaconda Prompt for the following steps.
1. Go to directory of CoSA_Website Folder.

2. Create the environment from the djangoEnv.yml file:
        
        conda env create -f djangoEnv.yml

3. Activate the new environment:
    - Windows :  ``` activate djangoEnv```
    - macOS and Linux: ```source activate djangoEnv```
    

#
#
#### Run Django Project

After activating the environment run the following command -

    python manage.py runserver
    
Open    ```localhost:8000```     in the Browser. 

In first_app Folder : 
- Webpage Directories:
    ```templates/first_app/page_name/```
    
- Resources Directories:
    ```static/first_app/page_name/```