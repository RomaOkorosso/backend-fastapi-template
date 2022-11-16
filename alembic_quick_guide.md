## Alembic Quick Guide

### Here will be a quick guide with must common commands to using Alembic.

1. To initialize a new project, run `alembic init`.
2. Fix the `alembic.ini` file depend on `https://alembic.sqlalchemy.org/en/latest/tutorial.html`
3. `alembic upgrade head` to upgrade to the latest version.
4. To run all migrations:
    1. drop database;
    2. `$ alembic upgrade head`
5. To run specific migration:
   `$ alembic upgrade <migration_name>`
6. To revert specific migration:
   `$ alembic downgrade <migration_name>`
7. To revert all migrations:
   `$ alembic downgrade base`
8. To revert one migration:
   `$ alembic downgrade -1`
9. To see all migrations:
   `$ alembic history`
10. To see current migration:
    `$ alembic current`
11. To create new migration with autogenerate:
    `$ alembic revision --autogenerate -m "message"`
12. To create new migration without autogenerate:
    `$ alembic revision -m "message"`

<!-- TODO 
Write with real examples and screenshots
-->