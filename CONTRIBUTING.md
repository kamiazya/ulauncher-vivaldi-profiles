# Contributing

## Overview

1. Fork it!
1. Create your feature branch:
    ```bash
    git checkout -b feature/my-feature
    ```

1. Commit your changes:
    ```bash
    git commit -am 'Add some feature'
    ```
1. Push to the branch:
    ```bash
    git push origin my-new-feature
    ```
1. Submit a pull request

## Development

### First time only

1. As a prerequisite, this extension must be installed in a legitimate way.
1. Set the environment variables used during development and describe them in the `.env` file.
    ```bash
    # modify it to suit your environment
    PYTHONPATH=/usr/lib/python3/dist-packages
    PYTHON3=/usr/bin/python3
    ```

### Always

1. Launch Ulauncher for development.
    ```
    make start
    ```
1. Run main.py in this repository with environment variables.
  Environment variables depend on the environment, so modify them accordingly.
    ```bash
    make dev
    ```

### Finished

The Ulauncher service has been stopped, so restart it.

```bash
make restart-service
```
