## Contribution guidelines  👨🏻‍🚀

- First, pull the repository. `git clone https://github.com/asifrahaman13/superquery.git`

- Go to the root directory. `cd superquery`

- Enable virtual environment for the poetry. `poetry config virtualenvs.in-project true`

- Now install the dependencies. `poetry install`

- Now rename the .env.example. `mv .env.example .env`.  Give the proper configuration by giving the API keys. For example set the open ai key etc. Also set the configuration data in the config.yaml file.

## Install precommit hooks.

You need to install the pre-commit hooks to ensure that your code follows the proper guidelines and linting.

 `poetry run pre-commit install`

# Run the server 🚀
You need to run the application using the following script: `poetry run uvicorn src.main:app --reload`

## Frontend

Next go to the front end folder 

`cd frontend/`

Now, install the dependencies.

`bun install`

Next, you can run the code.

`bun run dev`

Now rename .env.example to .env file.

`mv .env.example .env`


## Run with docker

The best way of utilizing the docker is through the docker-compose file.

`docker compose up -d`


## PORT 👨🏻‍🚀

- Backend: 8000
- Frontend: 3000
