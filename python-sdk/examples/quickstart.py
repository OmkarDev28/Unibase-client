from unibase import Unibase

def main():
    db = Unibase("http://localhost:5000", "ub_live_example_key")

    print("--- Unibase Quickstart ---")
    
    # 1. Auth
    print("\n1. Creating a User...")
    res = db.auth.create_user("Bharat", "password123", "bharat@example.com")
    print(res)

    # 2. Query
    print("\n2. Querying SQL...")
    res = db.query.select("users", ["id", "username"])
    print(res)

    # 3. Collection
    print("\n3. Adding to Collection...")
    res = db.collection("logs").add({"event": "login", "user": "Bharat"})
    print(res)

    # 4. Graph
    print("\n4. Creating Graph Node...")
    res = db.graph.create_node("Bharat", {"status": "active", "country": "India", "city": "Mumbai"})
    print(res)

if __name__ == "__main__":
    main()
