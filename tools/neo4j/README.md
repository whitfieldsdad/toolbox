Neo4j
---

![Neo4j](images/neo4j.png)

Neo4j is a graph database.

# Containers

## Start

To start Neo4j:

```shell
$ ./start-neo4j.sh
```

## Stop

To stop Neo4j:

```shell
$ ./stop-neo4j.sh
```

### Required ports

| Service      | Source port | Target port |
|--------------|-------------|-------------|
| neo4j        | 7687        | 7687        |
| neo4j        | 7473        | 7473        |
| neo4j        | 7474        | 7474        |

### Volumes

| Service      | Local volume | Remote path |
|--------------|--------------|-------------|
| neo4j        | neo4j        | /bitnami    |
