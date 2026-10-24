from unibase import Unibase

def main():
    db = Unibase("http://localhost:5000", "ub_live_example_key")

    print("--- Unibase Todo App ---")
    
    # Add a todo
    print("Adding a todo...")
    db.collection("todos").add({"title": "Buy milk", "completed": False})

    # Get all todos
    print("Fetching todos...")
    todos = db.collection("todos").get_all()
    print(todos)

    # Complete a todo
    print("Completing todo...")
    db.collection("todos").where("title", "==", "Buy milk").update({"completed": True})

if __name__ == "__main__":
    main()
