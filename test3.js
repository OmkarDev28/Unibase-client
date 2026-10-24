import { Unibase } from "./unibase.js";

const API_URL = "http://localhost:5000"; 
const API_KEY = "YOUR_API_KEY_HERE"; 

const db = new Unibase(API_URL, API_KEY);
async function runTestPipeline() {
    try {
        console.log("🚀 Starting Unibase Integration Test...\n");

        // 1. TEST INSERT
        console.log("Step 1: Inserting new patient...");
        const newPatient = await db.table('test_patients')
            .insert({ name: "Bob Ross", age: 52, status: "happy" })
            .returning('*')
            .execute();
        console.log("✅ Inserted:", newPatient[0].name);

        // 2. TEST SELECT (Filtering)
        console.log("\nStep 2: Selecting stable patients over 20...");
        const patients = await db.table('test_patients')
            .select('name, status')
            .where('age', '>', 20)
            .where('status', '=', 'stable')
            .execute();
        console.log("✅ Found:", patients.length, "patients");
        console.table(patients);

        // 3. TEST UPDATE
        console.log("\nStep 3: Updating Bob's status...");
        const updated = await db.table('test_patients')
            .update({ status: 'painting' })
            .where('name', '=', 'Bob Ross')
            .execute();
        console.log("✅ Updated Status:", updated[0].status);

        // 4. TEST DELETE
        console.log("\nStep 4: Deleting test record...");
        const deleted = await db.table('test_patients')
            .delete()
            .where('name', '=', 'Bob Ross')
            .execute();
        console.log("✅ Deleted Record Count:", deleted.length);

        console.log("\n✨ All tests passed successfully!");

        const newPatient1 = await db.table('test_patients')
            .insert({ name: "Pokemon", age: 52, status: "happy" })
            .returning('*')
            .execute();
        console.log("✅ Inserted:", newPatient[0].name);

    } catch (err) {
        console.error("\n❌ TEST FAILED:");
        console.error("Message:", err.message);
        // This helps you see if the error is from your builder or the DB
        if (err.stack) console.error("Stack:", err.stack);
    }
}

runTestPipeline();
