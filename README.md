# NeqSimLive api template
This is a template for creating a NeqSimLive API, typically for deployment in [Radix](https://radix.equinor.com/) , using the [NeqSim](https://pypi.org/project/neqsim/) python package. The API endpoints are created using [fastapi](https://pypi.org/project/fastapi/) and it is all packed in a docker container.


## Getting started
Click "Use this template" to generate a repository for your API. Select a relevant name for the repository and if it is public/internal/private. NB! Internal is recommended if it is to be deployed in Radix.

All user development is done in python. See demoAPI/src for a sample application and demoAPI/example for a jupyter notebook for testing the API and for connecting to plant data. See the [NeqSimPython project](https://github.com/equinor/neqsimpython) for documentation of how to use NeqSim in Python. 


## Develop using Codespaces
In your new repository, click the "<> Code" button and select "codespaces" if you want to use a github-hosted cloud environment instead of running locally. For more info see [codespaces](https://github.com/features/codespaces).


## Getting ready for deployment
Document your API in demoAPI/README.md.  
Rename the demoAPI folder to a suitable short name for your application you are making.


## Pull the code into NeqSimLive repo 
Open NeqSimLive [NeqSimLive repo](https://github.com/equinor/NeqSimLive) local or using CodeSpaces. Make a new branch in NeqSimLive and run command command 
```
git submodule add "path to you new API"
````
When a pull request is created, the NeqSimLive administrators will review and merge into NeqSimLive main branch, thus making it available via Radix to be used via tools such as Sigma for online monitoring. API updates are done in your own  of API are done on your own branch and by pulling the updates into NeqSimLive.


## Go live using Sigma
Establish Sigma server, config page and start live process calculation and monitoring.
Contact NeqSimLive administrators.


