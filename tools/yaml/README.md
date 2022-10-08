# JSON

> YAML is a markup language that's designed to be easy for humans to read.
 
## Examples

### Translating YAML files into JSON files.

You can convert YAML files to JSON files like this:

```shell
$ python3 tools/yaml/yaml-to-json.py -i resources/example-data/yaml/atomic-red-team-tests.yaml | jq
$ python3 tools/yaml/yaml-to-json.py -i resources/example-data/yaml/atomic-red-team-tests.yaml -o resources/example-data/yaml/atomic-red-team-tests.json
```

### Translating JSON files into YAML files

You can convert JSON files into YAML files like this:

```shell
$ python3 tools/json/json-to-yaml.py -i resources/example-data/yaml/atomic-red-team-tests.json -o resources/example-data/yaml/atomic-red-team-tests.yaml
```
