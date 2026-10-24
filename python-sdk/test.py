from unibase import Unibase

def main():
    api_key = "ub_live_your_api_key_here"
    db = Unibase("http://localhost:5000", api_key)
    
    print("Testing Auth Service...")
    # Using a fresh username so it doesn't collide with "Bharat"
    res = db.auth.create_user(username="PythonTester", email="test@example.com", password="password123")
    print(f"Auth Response: {res.success} - {res.message}")

    print("\nPreparing SQL Database...")
    # 1. Automatically create the users table using raw SQL
    db.query.raw("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, role text);")
    # 2. Insert a row so the select query has something to find
    db.query.insert("users", {"role": "admin"})

    print("Testing SQL Service (Select)...")
    sql_res = db.query.select(table="users", columns=["*"], where={"role": "admin"})
    print(f"SQL Response: {sql_res.success} - {sql_res.message}")

    print("\nPreparing Collections...")
    # 1. Automatically register the 'items' collection in the system table
    db.query.raw("INSERT INTO _ub_collections (name) VALUES ('items') ON CONFLICT DO NOTHING;")

    print("Testing Collections (Add)...")
    coll_res = db.collection("items").add({"name": "Laptop", "price": 999})
    print(f"Collection Response: {coll_res.success} - {coll_res.message}")

    print("\nTesting Graph...")
    graph_res = db.graph.create_node("PythonNode", {"environment": "SDK Test"})
    graph_res = db.graph.create_node("ReactNode", {"environment": "SDK Test"})
    print(f"Graph Response: {graph_res.success} - {graph_res.message}")

if __name__ == "__main__":
    main()
