# directus-requests

[![Release](https://img.shields.io/github/v/release/edouardbruelhart/directus-requests)](https://img.shields.io/github/v/release/edouardbruelhart/directus-requests)
[![Build status](https://img.shields.io/github/actions/workflow/status/edouardbruelhart/directus-requests/main.yml?branch=main)](https://github.com/edouardbruelhart/directus-requests/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/edouardbruelhart/directus-requests/branch/main/graph/badge.svg)](https://codecov.io/gh/edouardbruelhart/directus-requests)
[![Commit activity](https://img.shields.io/github/commit-activity/m/edouardbruelhart/directus-requests)](https://img.shields.io/github/commit-activity/m/edouardbruelhart/directus-requests)
[![License](https://img.shields.io/github/license/edouardbruelhart/directus-requests)](https://img.shields.io/github/license/edouardbruelhart/directus-requests)

A repository to group all little scripts that are not made to be automated afterwards. For example, scripts to update only one time data in directus, but not scripts that will automate a process.

- **Github repository**: <https://github.com/edouardbruelhart/directus-requests/>
- **Documentation** <https://edouardbruelhart.github.io/directus-requests/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:edouardbruelhart/directus-requests.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
