# Unibase Python SDK

The official Python SDK for Unibase — a powerful Backend-as-a-Service (BaaS) engine. 
This SDK provides a clean, Pythonic wrapper around the Unibase REST API, letting you handle authentication, SQL queries, NoSQL collections, graph relationships, and storage effortlessly.

## Installation

```bash
pip install unibase
```

## Quickstart

```python
from unibase import Unibase

# Initialize the client
db = Unibase("http://localhost:5000", "ub_live_your_api_key_here")

# Authenticate a user
user = db.auth.create_user(username="Bharat", password="secret", email="bharat@example.com")

# Query SQL tables
rows = db.query.select(table="users", where={"role": "admin"})

# Work with Collections (NoSQL)
db.collection("products").add({"name": "Laptop", "price": 999})
expensive = db.collection("products").where("price", ">", 500).get()

# Manage Graph Nodes
db.graph.create_node("Bharat", properties={"country": "India", "city": "Mumbai"})
```

For more examples, check the `examples/` directory.

## License & Attribution

This project is open-source under the MIT License. However, we request that you **give credit and mention Unibase Team** if you use this SDK in your projects. 

