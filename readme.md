# GitHub training with python

This is an example project how to use [GitHub](https://github.com) with Python project.

Prerequisites:
* [ ] Python 3.10+ and venv are installed on your computer
* [ ] Git is installed on your computer
* [ ] You have a GitHub account

For practicing follow the [task descriptions](./tasks.md) and executes them in a separated branch.

## Development environment

1. Create a virtual environment
```shell
python -m pip install --upgrade pip
python -m venv .venv
pip install -r requirements.txt
```

2. Activate the created virtual environment
```shell
.\.venv\Scripts\Activate.ps1
```

3. Formatting the code
```shell
black .
```

4. running test
```shell
pytest . -v
```

### IDE

If you are using Visual Studio Code, then the project specific [settings](/.vscode/settings.json) and [launch configurations](/.vscode/launch.json) are in `.vscode` folder.


## Working flow

1. In case of new feature requirements or bug fixes create [new issues](/../../issues/new)
2. Fork the project under your github account
3. Create a new branch for the issue to implement
4. Create a pull-request to the upstream project


## Release

Create a tag on the commit you want to release. The tag naming convenvtion must fit to `<major>.<minor>.<patch>` format where both `major`, `minor` and `patch` are numbers, ie: `0.2.1`.

## Usage

```shell
python calculator.py
1
2

3
```
