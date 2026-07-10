Title: Virtualenv env vars
Date: 2022-07-08
Modified: 2022-07-08
Tags: python, virtualenv
Summary: Auto-load a project's .env file when activating a virtualenv, with a postactivate script and a grep trick for switching environments by commenting lines.

Setup `postactivate` script on a new virtualenv

### `~/.virtualenvs/project/bin/postactivate`

```sh
#!/usr/local/Cellar/bash/5.0.18/bin/bash
PROJECT_PATH=~/some/project/path/

export $(grep -v '^#' $PROJECT_PATH/.env | eval echo $(eval xargs))
```

### `~/some/project/path/.env`

```sh
# DEV ENV
# DATABASE_URL=<some_dev_env_db_url>

# LOCAL ENV
DATABASE_URL=postgresql://<local_db_url>
```

`grep` of all not commented lines allows for an easy env vars switch.

With `virtualenvwrapper`, just the `.env` file and rerun the `workon project` cmd.
