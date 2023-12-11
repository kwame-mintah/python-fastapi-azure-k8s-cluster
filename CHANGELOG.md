## v0.1.1 (2023-12-11)

### Refactor

- **summary**: update endpoint summary to include full stop

## v0.1.0 (2023-12-10)

### Feat

- **k8s**: initial deployment k8s
- **routers**: rename `/demo` endpoint to `/v1/hello`
- **endpoints**: add response models to endpoints
- **pydantic**: introduce pydantic models application
- **docker-compose**: initial docker-compose for fastapi bigger applications
- **app**: initial project structure
- **init**: initial project set up for `pre-commit` and project linting

### Refactor

- **versions**: include `v1` as a prefix to endpoints
- **demo**: include service version in hello world message
- change port to 8080
- **k8s**: change ports used in k8s deployment
- **main**: change root message
- **demo**: change prefix from dashboard to demo
- **main**: remove auto reload of fastapi
