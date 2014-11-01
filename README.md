boundary-python-plugin-framework
================================


Setup 
------
```bash
$ source env.sh # Adds scripts to PATH environment variable
 ```
### Export Metrics
```bash
$ metric-export -h
usage: metric-export [-h] [-d] [-e EMAIL] [-p pattern] [-t APIKEY] [-v]

Export metric definitions

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enables debugging
  -e EMAIL, --email EMAIL
                        e-mail uses to create the account
  -p pattern, --pattern pattern
                        text pattern to use search the name of the metric
  -t APIKEY, --api-key APIKEY
  -v                    verbose mode
```

### Import Metrics
```bath
$ metric-import -h
usage: metric-import [-h] [-d] [-e EMAIL] -f PATH [-t APIKEY] [-v]

Import metric definitions

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enables debugging
  -e EMAIL, --email EMAIL
                        e-mail used to create the account
  -f PATH, --file PATH  Path to JSON file
  -t APIKEY, --api-key APIKEY
                        Boundary API Key
  -v                    verbose mode
```

