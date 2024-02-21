#!/usr/bin/env python3

from app import app
from models import db, Raccoon
from faker import Faker
from random import randint

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        print("Clearing old raccoons!")

        Raccoon.query.delete()

        print("Making raccoons!")

        raccoons = []

        for _ in range(10):
            r = Raccoon(name=faker.name(), location=faker.country())
            raccoons.append(r)

        db.session.add_all( raccoons )
        db.session.commit()

        print("Seeding complete!")