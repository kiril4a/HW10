import pymongo
from pymongo.errors import ConnectionFailure, OperationFailure

def list_databases_and_collections():
    try:
        # Підключення до MongoDB за допомогою pymongo
        client = pymongo.MongoClient(
            "mongodb+srv://kiril4a:matador1983@cluster0.t1m9ifp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        )

        # Перевірка підключення
        print(client.admin.command('ping'))
        
        # Отримання всіх баз даних
        databases = client.list_database_names()

        if databases:
            print("Databases in the cluster:")
            for db_name in databases:
                print(f"\nDatabase: {db_name}")
                db = client[db_name]
                collections = db.list_collection_names()
                if collections:
                    print("Collections:")
                    for collection in collections:
                        print(f" - {collection}")
                else:
                    print("No collections found in this database.")
        else:
            print("No databases found in the cluster.")
    
    except ConnectionFailure as e:
        print(f"Connection Error: {e}")
    except OperationFailure as e:
        print(f"Operation Failure: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Виклик функції для виводу баз даних та колекцій
if __name__ == "__main__":
    list_databases_and_collections()
