from app import User, Post, db, app
from app import create_sample_data

with app.app_context():
    create_sample_data()
    users = User.query.all()
    print(users)
    print("Database tables created successfully.")
