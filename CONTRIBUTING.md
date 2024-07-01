## Contribution guidelines  


- First pull the repository. `git clone https://github.com/asifrahaman13/superquery.git`

- Go to the root directory. `cd superquery`

- create a virtual environment. `virtualenv .venv`. You need to actiavate the virtual environment too. `source .venv/bin/activate`

- Now install the dependencies. `pip install -r requirements.txt`

- Now rename the .env.example. `mv .env.example .env`.  Give the proper configuration by giving the API keys. For example set the open ai key, deepgram api key etc. Also set the configuration data in the config.yaml file. If you are using redis server instead of local redis environment please change the redis.conf file.

- Next you need to run the application using the following script: `uvicorn src.main:app --reload`

## Install precommit hooks.

 `pre-commit install`

## Frontend
Next go to the front end folder 

`cd frontend/`

Now install the dependencies.

`bun install`

Next you can run the code.

`bun run dev`

## Run with docker

Best way of utilizing the docker is through the docker compose file.

`docker compose up -d`

In case you face any issue with the installtion and set up, you can run using docker.

`docker build -t superquery:lastest .`

Next you can run the application:

`docker run -p 8000:8000 superquery:latest`

## PORT

- Backend: 8000
- Frontend: 3000
