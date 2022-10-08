Redis
---

![Redis](images/redis.png)

Redis is an in-memory data structure store that is widely regarded as being "glue for microservices".

# Containers

[Redis](https://redis.io/) is provided via the following containers:
- [redislabs/redismod](https://hub.docker.com/r/redislabs/redismod)
  - Includes Redis;
  - Includes a command line interface for working with Redis (`redis-cli`);
  - Includes select Redis modules from [Redis Labs](https://redislabs.com/)
    + [RediSearch](https://oss.redislabs.com/redisearch/): a full-featured search engine
    + [RedisGraph](https://oss.redislabs.com/redisgraph/): a graph database
    + [RedisTimeSeries](https://oss.redislabs.com/redistimeseries/): a timeseries database
    + [RedisJSON](https://oss.redislabs.com/redisjson/): a native JSON data type
    + [RedisBloom](https://oss.redislabs.com/redisbloom/): native Bloom and Cuckoo Filter data types
    + [RedisGears](https://oss.redislabs.com/redisgears/): a dynamic execution framework
- [redislabs/redisinsight](https://hub.docker.com/r/redislabs/redisinsight)
  - Provides a web interface for Redis

## Start

To start Redis:

```shell
$ ./start-redis.sh
```

## Stop

To stop Redis:

```shell
$ ./stop-redis.sh
```

## `redis-cli`

You can access `redis-cli` by attaching to a running instance of a `redis` container as follows:

```shell
$ ./connect-to-redis.sh 
Attaching to 'redis' container...
127.0.0.1:6379> 
```

### Required ports

| Service      | Source port | Target port |
|--------------|-------------|-------------|
| redis        | 6379        | 6379        |
| redisinsight | 8001        | 8001        |

### Volumes

| Service      | Local volume | Remote path |
|--------------|--------------|-------------|
| redis        | redis        | /data       |
| redisinsight | redisinsight | /db         |
