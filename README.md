# SQLAlchemy Recap

## Learning Goals

- Initializing a database

- Creating models

- Migrating a database

- CRUD using SQLAlchemy methods

```python
Raccoon.query.all()
Raccoon.query.where(Raccoon.id == 1).first()

r3.location = "Paris"
db.session.commit()

first_raccoon = Raccoon.query.where(Raccoon.id == 1).first()
db.session.delete(first_raccoon)
db.session.commit()
```