# Django FMG project template

This Django starter pack template inspired by [Cookiecutter Django-Vue](https://github.com/vchaptsev/cookiecutter-django-vue) which powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter). It is for jumpstarting production-ready Django projects quickly.

## Features

- [ ] TODO: describe all futures (12 app, poetry, poe, graphql).

## Step by step to use

- Clone repository `git clone https://github.com/FreeMindsGroup/dj-backend.git`.
- Install dependencies and create a virtual environment by `poetry install` from **pyptoject.toml**.
- Fill **.env** variables by creating a file in the Django root directory.

## Commands

- [ ] TODO: describe all [poetry](https://python-poetry.org/) and [poe](https://github.com/nat-n/poethepoet) commands.

# Environment variables example

All variables should be stored in this format: `KEY="value"`.

These variables are used by [Django configurations](https://django-configurations.readthedocs.io/en/stable/) to separate
environment settings into development, quality assurance and production:

- `DJANGO_SETTINGS_MODULE="config.settings"`. The variable stores the path to the `settings.py` file.
- `DJANGO_CONFIGURATION="Dev"`. The variable stores the environment selection (Dev,QA, Prod classes).

Standard Django settings:

- `DJANGO_SECRET_KEY="bbyby"`. The variable stores a
  unique [secret key](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY), which can be
  generated using the `poetry run poe secret` command. More info in `pyproject.toml` at a chapter`[tool.poe.tasks]`.

# Deployment

- [ ] TODO: deploy to Heroku.

# LICENSE

MIT License

Copyright (c) 2021 Ilya Filimonov

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
