MITRE ATT&CK Navigator
---

Spin up a local instance of the MITRE ATT&CK Navigator!

## Usage

The following scripts can be used to create and manage a development instance of the MITRE ATT&CK Navigator that runs within Docker.

### Requirements

- Docker
- Docker Compose

### Required ports

| Protocol | Protocol | Description    |
|----------|----------|----------------|
| TCP      | 4200     | Web UI (HTTP)  |

### Docker Compose

You can interact with containers using the provided `Makefile` or directly using `docker-compose`.

#### Starting containers

To start all containers:

```shell
$ make up
````

#### Stopping containers

To stop all containers:

```shell
$ make down
````

#### Updating containers

To stop, update, and restart all containers:

```shell
$ make update-and-restart
```

#### Removing containers

To remove all containers:

```shell
$ make clean
````
