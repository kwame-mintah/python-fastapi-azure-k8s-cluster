# Python FastAPI Bigger Applications Template

![fastapi-0.103.2-informational](https://img.shields.io/badge/fastapi-0.103.2-informational)
<a href="https://github.com/new?template_name=python-fastapi-bigger-applications-template&template_owner=kwame-mintah">
<img src="https://img.shields.io/badge/use%20this-template-blue?logo=github">
</a>

This a template project, to demonstrate using FastAPI in a bigger application. The same file structure
has been followed as per FastAPI [docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/).

This repository is intended as a quick-start and includes the following:

- A `Dockerfile` to build the FastAPI application following [guidelines](https://docs.docker.com/develop/develop-images/guidelines/)
- `docker-compose.yml` file to build and start the application
- GitHub Action workflow to run linting and unit tests
- Pre-commit hooks to run on each commit
- Pydantic models as response models for endpoints
- Unit and feature tests for endpoints

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

## Deploy on Azure Web App

This project has been configured to automatically run and deploy changes made to the `main` branch to an environment variable,
see `/azure-pipelines-docker-k8s-deploy.yml` and `/azure-pipelines-run-unit-tests.yml` the following variables are required to be set for pipelines.

### Pipeline variables (docker-k8s-deploy)

| Variable                               | Description                                                              | Default value | Required? |
| -------------------------------------- | ------------------------------------------------------------------------ | ------------- | --------- |
| projectPoolName                        | The Azure agent pool that the job will run on                            | N/A           | Yes       |
| projectContainerRegistry               | The Azure Container Registry login server                                | N/A           | Yes       |
| projectDockerRegistryServiceConnection | The service connection with Docker Registry (using basic authentication) | N/A           | Yes       |
| projectImageRepository                 | The docker image name to push to registry                                | N/A           | Yes       |

### Pipeline variables (run-unit-tests)

| Variable                               | Description                                                              | Default value | Required? |
| -------------------------------------- | ------------------------------------------------------------------------ | ------------- | --------- |
| projectPoolName                        | The Azure agent pool that the job will run on                            | N/A           | Yes       |
