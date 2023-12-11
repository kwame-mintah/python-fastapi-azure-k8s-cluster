# Python FastAPI Azure K8S Cluster

![fastapi-0.103.2-informational](https://img.shields.io/badge/fastapi-0.103.2-informational)
<a href="https://github.com/new?template_name=python-fastapi-bigger-applications-template&template_owner=kwame-mintah">
<img src="https://img.shields.io/badge/use%20this-template-blue?logo=github">
</a>
[![Build Status](https://dev.azure.com/k-space/k/_apis/build/status%2Fdocker-k8s-cluster-deploy?branchName=main)](https://dev.azure.com/k-space/k/_build/latest?definitionId=10&branchName=main)

This project demonstrates deploying a FastAPI application onto an Azure Kubernetes Cluster. Azure Pipelines
have been created to build and push the service docker image to an Azure Container Registry. And also deploy the service
to a Kubernetes cluster. Azure resources created have been written in Terraform can be found in Azure DevOps repository
[here](https://dev.azure.com/k-space/k/_git/k-infrastructure-terraform).

> [!NOTE]
>
> This repository was original created within Azure DevOps and is now being mirrored to this GitHub [repository](https://github.com/kwame-mintah/python-fastapi-azure-k8s-cluster).
> Source of truth will always be the Azure DevOps [repository](https://dev.azure.com/k-space/k/_git/python-fastapi-azure-k8s-cluster)[^1].

## Usage

1. Install python packages used for the service

   ```console
   pip install - requirements.txt
   ```

2. Run the FastAPI server, which will run on port 8000

   ```console
   python app/main.py
   ```

   Endpoint documentation are available on http://127.0.0.1:8000/docs

## Docker

Running the `docker-compose.yml`, will build a new image python-fastapi-bigger-applications-template-fastapi:latest
which will be used for the `fastapi` service within the container.

```commandline
docker-compose up -d
```

## Tests

Unit tests are located in `/tests` directory.

```console
pytest tests/
```

## Azure Pipelines (CI/CD)

This project has two pipelines see files:
- `/azure-pipelines-docker-k8s-deploy.yml`
- `/azure-pipelines-run-unit-tests.yml`

The tables below detail pipeline variables required, most of the values required for deploying FastAPI to Azure Kubernetes cluster, can be found with
the terraform repository [here](https://dev.azure.com/k-space/k/_git/k-infrastructure-terraform). Additionally, as the orginasation / projected created,
within Azure DevOps is private, these pipelines have been written to run on a [self-host build agent](https://github.com/kwame-mintah/azuredevops-selfhosted-agents-docker-compose) so YMMV.

### Pipeline variables (docker-k8s-deploy)

| Variable                               | Description                                                                   | Default value | Required? |
|----------------------------------------|-------------------------------------------------------------------------------|---------------|-----------|
| projectAzureSubscriptionConnection     | The Azure Resource Manager service connection ID                              | N/A           | Yes       |
| projectAzureResourceGroup              | The Azure resource group were the cluster exists in                           | N/A           | Yes       |
| projectKubernetesCluster               | The Azure kubernetes cluster name                                             | N/A           | Yes       |
| projectImagePullSecret                 | The Kubernetes secret name to be generated / used for pulling images from ACR | N/A           | Yes       |
| k8sNamespace                           | The Kubernetes name space to deploy the service                               | default       | No        |
| projectPoolName                        | The Azure agent pool that the job will run on                                 | N/A           | Yes       |
| projectContainerRegistry               | The Azure container registry login server                                     | N/A           | Yes       |
| projectDockerRegistryServiceConnection | The service connection with Docker Registry (using basic authentication)      | N/A           | Yes       |
| projectImageRepository                 | The docker image name to push to registry                                     | N/A           | Yes       |

### Pipeline variables (run-unit-tests)

| Variable        | Description                                   | Default value | Required? |
|-----------------|-----------------------------------------------|---------------|-----------|
| projectPoolName | The Azure agent pool that the job will run on | N/A           | Yes       |

^1: My Azure DevOps organisation / project is private.
