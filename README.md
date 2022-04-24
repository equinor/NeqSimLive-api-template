# NeqSimLive api template
This is a template for creating a NeqSimLive API using the [NeqSim](https://pypi.org/project/neqsim/) python package. The API endpoints are created using [fastapi](https://pypi.org/project/fastapi/) and it is all packed in a docker container.


## Getting started
Click "Use this template" to generate a repository for your API.  
See demoAPI/src for a sample application and demoAPI/example for a jupyter notebook testing the API. All user development is done using python. See the [NeqSimPython project](https://github.com/equinor/neqsimpython) for documentation of how to use NeqSim in Python. 


## Develop using Codespaces
Click the "<> Code" button and select "codespaces" if you want to use a github-hosted cloud environment instead of running locally. For more info see [codespaces](https://github.com/features/codespaces).


## Getting ready for deployment
Document your API in demoAPI/README.md.  
Rename the demoAPI folder to a suitable short name for your application you are making.

## Pull the code into NeqSimLive repo 
Open NeqSimLive [NeqSimLive repo](https://github.com/equinor/NeqSimLive) local or using CodeSpaces. Make a new branch in NeqSimLive. Run command git submodule add "git path to you new API". Your API will then be reviwed by NeqSimLive administrators and merged into NeqSimLive main branch and available via Raddix to be used via tools such as Sigma for online monitoring.

## Go live using Sigma
Establish Sigma server, config page and start live process calculation and monitoring.
Contact NeqSimLive administrators.


