# JSON

> JSON is the lingua franca of web services.

You can use the scripts in this folder to:
- Pretty-print JSON documents (i.e. to make them easier to read)
- List the keys in a JSON document (i.e. to let you know what data is in a JSON document)
- Select fields in a JSON document by name (i.e. to allow for the filtering of JSON documents by key)
- Translate JSON documents into XLSX documents using [`pandas`](https://pandas.pydata.org/) (i.e. to let you work with JSON data within Microsoft Excel)

## Examples

### Pretty-printing JSON documents

Pretty-printing is a technique for rendering the content of a document or data structure on the command line.

You can pretty-print a JSON document like this:

```shell
$ ./tools/json/pretty-print-json.sh resources/example-data/json/list-of-maps.json
[
  {
    "name": "Meowsy",
    "species": "cat",
    "foods": {
      "likes": [
        "tuna",
        "catnip"
      ],
      "dislikes": [
        "ham",
        "zucchini"
      ]
    }
  },
  {
    "name": "Barky",
    "species": "dog",
    "foods": {
      "likes": [
        "bones",
        "carrots"
      ],
      "dislikes": [
        "tuna"
      ]
    }
  },
  {
    "name": "Purrpaws",
    "species": "cat",
    "foods": {
      "likes": [
        "mice"
      ],
      "dislikes": [
        "cookies"
      ]
    }
  }
]
```

### Listing keys in a JSON file

You can list:
- The top-level keys in a JSON document containing a map; or
- The keys associated with a list of JSON documents (e.g. a list of users)

Like this:

```shell
$ python3 tools/json/get-json-keys.py -i resources/example-data/json/map.json
["foods", "name", "species"]

$ python3 tools/json/get-json-keys.py -i resources/example-data/json/list-of-maps.json
["foods", "name", "species"]
```

### Selecting fields in JSON file

You can select a subset of the fields in a JSON document like this:

```shell
$ cat resources/example-data/json/map.json | jq
{
  "name": "Barky",
  "species": "dog",
  "foods": {
    "likes": [
      "bones",
      "carrots"
    ],
    "dislikes": [
      "tuna"
    ]
  }
}

$ python3 tools/json/select-json-keys.py -i resources/example-data/json/map.json -k name,species
{
    "name": "Barky",
    "species": "dog"
}
```

By default, the output will be written to stdout - you can write to a file using the `--output-file` argument.

```shell
$ python3 tools/json/select-json-keys.py -i resources/example-data/json/map.json -k name,species -o example.json && jq < example.json
```

Or, using shell redirection:

```shell
$ python3 tools/json/select-json-keys.py -i resources/example-data/json/map.json -k name,species > example.json && jq < example.json
```

### Translating JSON files into XLSX files

The following file formats are supported when translating JSON files into XLSX files:
- JSON files containing key/value pairs (e.g. `{"hostname": "example.com, "ip_address": "10.13.35.18"}`)
- JSON files containing lists of maps (e.g. `[{"hostname": "example.com, "ip_address": "10.13.35.18"}]`)
- JSON files containing maps of maps (e.g. `{"locator": {"hostname": 4, "fqdn": 0, "ip_address: 36}}`)

For example:

```shell
$ python3 tools/json/json-to-excel.py -i resources/example-data/json/maps.json -o resources/example-data/json/map.xlsx
$ python3 tools/json/json-to-excel.py -i resources/example-data/json/list-of-maps.json -o resources/example-data/json/list-of-maps.xlsx
$ python3 tools/json/json-to-excel.py -i resources/example-data/json/map-of-maps.json -o resources/example-data/json/map-of-maps.xlsx
```
