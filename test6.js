import { Unibase } from "./unibase.js"; 

//const ub = new Unibase("http://localhost:5000", "YOUR_API_KEY_HERE");

const following = await ub.graph.getConnections("alice_dev", "FOLLOWS");

await ub.graph.connect("Omkar", "user-01", "TEACHES");

const ub = new Unibase(
    "http://localhost:5000", 
    "ub_live_01cf910d6f0b3ebe3454a30497e93e39359e4708"
);

await ub.query(...);

const newUser = await db.auth.signUp({ 
    username: 'werrrrr', 
    password: 'secure123', 
}).run();

const newPatient = await db.table('test_patients')
            .insert({ name: "Bob Ross", age: 52, status: "happy" })
            .returning('*')
            .execute();

await ub.graph.connect("Merchant_A", "Rider_77", "ASSIGNED_TO",
                        { order_id: "ORD-101" }
                    );
