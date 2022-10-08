## Container registries

You can use scripts in this repository to maintain a local Docker container registry.

### Related network ports

| Source port | Target port | Description     |
|-------------|-------------|-----------------|
| 5000        | 5000        ||

### Related volumes

| Local volume   | Remote path       |
|----------------|-------------------|
 | registry-data  | /var/lib/registry |
 | registry-certs | /certs            |
 | registry-auth  | /auth             |


### Start a local container registry

```shell
$ ./start.sh
```

Or: 

```shell
$ make up
```

### Stop a local container registry

```shell
$ ./stop.sh
```

Or:

```shell
$ make down
```