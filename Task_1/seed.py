import psycopg2
from faker import Faker

conn = psycopg2.connect(
    dbname="postgres",  
    user="postgres",      
    password="",  # Пароль не був використаний
    host="localhost"
)
cursor = conn.cursor()

fake = Faker()

for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cursor.execute("INSERT INTO status (name) VALUES (%s)", (status,))

# Заповнення таблиці tasks
for _ in range(20):
    title = fake.sentence(nb_words=6)
    description = fake.paragraph(nb_sentences=3)
    status_id = fake.random_int(min=1, max=3)
    user_id = fake.random_int(min=1, max=10)
    cursor.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                   (title, description, status_id, user_id))

conn.commit()
cursor.close()
conn.close()