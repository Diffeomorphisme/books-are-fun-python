# books-are-fun-python
Why not in Python as well?

The project is divided into two parts:
- a backend (organised in a folder by feature way, so the structure is not as exactly the same as in the books-are-fun project), which consists of:
  - the API (consumed by the frontend)
  - the database, with its schema and repositories (used by certain calls to the API)
- a frontend, which interacts with the API to display a list of books


## Running the project

### Docker
From the root of the project, run:
```bash
docker compose up -d
```
The frontend is reachable [here](http://127.0.0.1:1234)


## To dos

- For frontend/backend specific todo, refer to their respective READMEs.
- Docker compose: introduce environment variables at this stage
- Separate requirements for front-end and back-end to avoid useless installs
- set up linter and formatter
