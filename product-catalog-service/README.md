# Product Catalog Service

RESTful product catalogue backend (Flask, SQLAlchemy, factory_boy) built with TDD,
with BDD scenarios (Behave and Selenium) for the admin UI.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
The default database is PostgreSQL (`postgresql://postgres:postgres@localhost:5432/postgres`).
To use another database set `DATABASE_URI`, for example `sqlite:///dev.db`.

## Run the unit tests (TDD)
```bash
pytest
```

## Run the service
```bash
honcho start            # serves on http://localhost:8080
```

## Run the BDD tests (needs Chrome and chromedriver)
With the service running in another terminal:
```bash
behave
```

## REST API
| Method | URL | Description |
|---|---|---|
| POST | /products | Create a product |
| GET | /products/{id} | Read a product |
| PUT | /products/{id} | Update a product |
| DELETE | /products/{id} | Delete a product |
| GET | /products | List all |
| GET | /products?name=Hat | List by name |
| GET | /products?category=FOOD | List by category |
| GET | /products?available=true | List by availability |

Example: `curl -i "http://localhost:8080/products?category=FOOD"`
