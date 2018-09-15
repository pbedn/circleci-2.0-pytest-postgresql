## circleci-2.0-pytest-postgresql

[![CircleCI](https://circleci.com/gh/pbedn/circleci-2.0-pytest-postgresql.svg?style=shield)](https://circleci.com/gh/pbedn/circleci-2.0-pytest-postgresql)

Example configuration for python + postgresql with CircleCI

---

Current setup creates database schema running command in .circleci/config.yml

```
- run:
    name: Setup the database
    command: psql -h localhost -p 5432 -U ubuntu -d circle_test -a -f schema.sql
```

Other possibility could be to do it from python, just uncomment line *setup_database(cur)* and remove one from circleci config to prevent error.

```python
# test_database.py
@pytest.fixture(scope="module")
def db():
    con, cur = connect_to_db(DATABASE)
    # setup_database(cur)
    yield con, cur
    con.close()
```
