from pymongo import MongoClient

# Підключення до локальної бази даних MongoDB
client = MongoClient('localhost', 27017)

# Створення або підключення до бази даних 'cats_db'
db = client['cats_db']

# Створення або підключення до колекції 'cats'
collection = db['cats']

def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat)
    print(f"Inserted cat with id: {result.inserted_id}")

def read_all_cats():
    cats = collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    cat = collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Cat not found")

def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print(f"Updated {result.modified_count} cat(s)")

def add_feature_to_cat(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    print(f"Updated {result.modified_count} cat(s)")

def delete_cat_by_name(name):
    result = collection.delete_one({"name": name})
    print(f"Deleted {result.deleted_count} cat(s)")

def delete_all_cats():
    result = collection.delete_many({})
    print(f"Deleted {result.deleted_count} cat(s)")

# Приклад використання:
create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
create_cat("Tom", 4, ["все життя намагаєтся спіймати одне мишеня", "постійно щось ламає", "синій"])
read_all_cats()

read_cat_by_name("Barsik")
read_cat_by_name("Tom")

update_cat_age("Barsik", 4)
update_cat_age("Tom", 5)

add_feature_to_cat("Barsik", "любить гратися з м'ячиком")
add_feature_to_cat("Tom", "полюьляє полювання, але погано на ньому розуміється")

delete_cat_by_name("Barsik") # Видалимо тільки Барсіка
#delete_all_cats() # Видалення всіх записів, якщо потрібно (Не видаляйте Тома!)