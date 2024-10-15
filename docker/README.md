# Docker

This directory contains all necessary files and configurations to manage the projects `Docker` environments.
It uses `Docker`, `Docker Compose` and is managed by the provided `Makefile`.

## Prerequisites

Before using this setup, make sure you have the following installed:

* [Docker]()
* [Docker Compose]()
* [Make]()

### Configuration

To create, run and manage the Docker environment, it is necessary to provide some basic configuration via `.env` files in:

* [.env](.env) in `/docker`

    ```dotenv
    NETWORK_NAME=astrolens_docker_network
    POSTGRES_DIR=postgresql
    GRAFANA_DIR=grafana
    ```

* [.env](grafana/.env) in `/grafana`

    ```dotenv
    # Grafana Security
    GF_SECURITY_ADMIN_USER=...
    GF_SECURITY_ADMIN_PASSWORD=...
    # Grafana Database Connection (PostgreSQL)
    GF_DATABASE_TYPE=...
    GF_DATABASE_HOST=...
    GF_DATABASE_NAME=...
    GF_DATABASE_USER=...
    GF_DATABASE_PASSWORD=...
    ```

* [.env](postgresql/.env) in `/postgresql`

    ```dotenv
    # PostgreSQL Security
    POSTGRES_USER: ...
    POSTGRES_PASSWORD: ...
    POSTGRES_DB: ...
    ```

### [Makefile](Makefile) Usage

The provided `Makefile` automates the following operations:

| Command       | Description                                            |
|---------------|--------------------------------------------------------|
| `make start`  | Start network and services                             |
| `make stop`   | Stop services                                          |
| `make status` | Check services status                                  |
| `make logs`   | Show logs for both PostgreSQL and Grafana services     |
| `make clean`  | Clean all resources: containers, networks, and volumes |
