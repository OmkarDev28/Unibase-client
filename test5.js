import { Unibase } from "./unibase.js"; 

const ub = new Unibase(
    "http://localhost:5000", 
    "YOUR_API_KEY_HERE"
);

async function seedSocialGraph() {
    try {
        console.log("--- Seeding Social Graph ---");

        // 1. Create User Nodes
        // We use the 'nodeName' (which goes into the 'type' column) as the Username
        const users = ["alice_dev", "bob_coder", "charlie_pro", "dana_hr"];

        for (const username of users) {
            await ub.graph.createNode(username, { 
                bio: `Hello, I am ${username}`,
                joined_at: new Date().toISOString()
            });
            console.log(`User created: ${username}`);
        }

        // 2. Create Follower Relationships
        console.log("\nEstablishing Follows...");

        // Alice follows everyone
        await ub.graph.connect("alice_dev", "bob_coder", "FOLLOWS");
        await ub.graph.connect("alice_dev", "charlie_pro", "FOLLOWS");
        await ub.graph.connect("alice_dev", "dana_hr", "FOLLOWS");

        // Bob and Charlie follow each other (Mutuals)
        await ub.graph.connect("bob_coder", "charlie_pro", "FOLLOWS");
        await ub.graph.connect("charlie_pro", "bob_coder", "FOLLOWS");

        // Dana only follows Alice
        await ub.graph.connect("dana_hr", "alice_dev", "FOLLOWS");

        console.log("--- Social Graph Seeded Successfully ---");
    } catch (error) {
        console.error("Seeding failed:", error.message);
    }
}

seedSocialGraph();