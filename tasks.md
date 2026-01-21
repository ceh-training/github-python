# Tasks

## Create your own pet project on [GitHub](https://github.com)

```shell
mkdir -p my-pet-project
cd my-pet-project
git init
git remote add origin git@github.com:<your-gh-account>/my-pet-project.git
echo "# My pet project" > readme.md
git status
git add readme.md
git status
git commit --message "init"
git log --all --graph --oneline --decorate
git push --set-upstream origin main
git log --all --graph --oneline --decorate
```

## Calculator

Create a calculator python application that reads 2 numbers from the standard input, and writes those sum to the standard output.

1. Write the development environment creation in [`readme.md`](/readme.md#development-environment)
2. Write some examples how to start/use the application (ie [Usage](/readme.md#usage))
3. Add [`.gitignore`](/.gitignore) to avoid accidentally add some files to your repository

### Umbrella

1. Create a GH project ie [CÉH GitHub Python - Calculator](https://github.com/users/schjan79/projects/1/settings)
2. Assign your repository as default to the
3. Create a [milestone](https://github.com/schjan79/ceh-github-python/milestone/1)


## Issues

Create an [new issue](/../../issues/new?title=formatting) for formatting expectation.

Organize the issues under both milestones and projects

Create [issue template](/.github/ISSUE_TEMPLATE.md)

Update the [`readme.md`](/readme.md#working-flow) with working flows.

## Pull request

Create a branch to implement the issue and create a pull-request.

Create a [github workflow](/.github/workflows/build.yaml) that validates the code formatting automatically at every push or PRs.

## Fix the formatting issue

```shell
python -m pip install black
black --check .
black .\calculator.py
git checkout -b fix_formatting
git add --patch
git commit --message "refromat code"
git push --set-upstream origin fix_formatting
```

Create a new pull request and merge.

## Write tests

Update [development environment](/readme.md#development-environment) to install `black` and `pytest` locally.

Implement [calculator test](./test_calculator.py)

Add test execution to the [CI](./.github/workflows/build.yaml#L20-L43)

Add [`launch.json`](/.vscode/launch.json) and [`settings.json`](/.vscode/settings.json) to SCM. Since the `.vscode` folder is in [`.gitignore`](/.gitignore#L2), the addition has to be forced, ie:

```shell
git add --force .vscode/settings.json
```

## Release

Create a release.
