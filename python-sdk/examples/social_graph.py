from unibase import Unibase

def main():
    db = Unibase("http://localhost:5000", "ub_live_example_key")

    print("--- Unibase Social Graph ---")
    
    # Create users
    print("Creating users...")
    db.graph.create_node("Bharat", {"age": 28, "city": "Mumbai", "country": "India"})
    db.graph.create_node("Aarav", {"age": 32, "city": "Delhi", "country": "India"})
    db.graph.create_node("Vihaan", {"age": 25, "city": "Bengaluru", "country": "India"})

    # Create relationships
    print("Creating relationships...")
    db.graph.create_relationship("Bharat", "Aarav", "FRIENDS_WITH", {"since": "2023"})
    db.graph.create_relationship("Bharat", "Vihaan", "FOLLOWS")

    # Get friends
    print("Getting friends of Bharat...")
    friends = db.graph.get_neighbors("Bharat", "FRIENDS_WITH")
    print(friends)

if __name__ == "__main__":
    main()
