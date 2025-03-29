## 🎉 Contribution guidelines  👨🏻‍🚀

👈🏻 Thanks for visiting this page and your interest in contributing to this repository.

- First, fork the repository. 

- Next, pull the forked repository. `git clone https://github.com/<your_username>/superquery.git`
  
- Upstream with the original repo `git remote add upstream https://github.com/asifrahaman13/superquery.git`


## Backend

Go to the root directory. `cd superquery`

Enable virtual environment for the poetry. `uv venv`

Now activate virtual environment `source .venv/bin/activate`

Now install the dependencies. `uv sync`

Now rename the .env.example. `mv .env.example .env`.  Give the proper configuration by giving the API keys. For example set the open ai key etc. Also set the configuration data in the config.yaml file.

# Run the server 🚀
You need to run the application using the following script: `poetry run uvicorn src.main:app --reload`

## Frontend

Next, go to the front-end folder 

`cd web/`

Now, install the dependencies.

`bun install`

Now rename .env.example to .env file.

`mv .env.example .env`

Next, you can run the front-end application.

`bun run dev`


## Run with docker

The best way to utilize the docker is through the docker compose file.

`docker compose up`


## Formatting

For backend:

For linting run the following:

```bash
ruff check --fix
```

For formatting run the following script:

```bash
ruff format
```

For linting run the following:

```bash
bun run lint
```

For the format run the following:

```bash
bun run format
```

## PORT 👨🏻‍🚀

- Backend: `8000`
- Frontend: `3000`
