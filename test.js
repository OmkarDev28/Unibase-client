// Adjust the import path to where your unibase.js is located
import { Unibase } from "./unibase.js"; 

// CONFIGURATION
const API_URL = "http://localhost:5000"; 
const API_KEY = "YOUR_API_KEY_HERE"; // Replace with your actual key

// Initialize SDK
const db = new Unibase(API_URL, API_KEY);

// Generate random user to avoid conflicts
const randomId = Math.floor(Math.random() * 10000);
const testUser = {
    username: `sdk_user_${randomId}`,
    email: `sdk_${randomId}@test.com`,
    password: "secure_password_123"
};

async function runTests() {
    console.log("🚀 Starting SDK Auth Tests...\n");

    try {
        // --- TEST 1: SIGN UP ---
        console.log(`1️⃣  Testing signUp()...`);
        const newUser = await db.auth.signUp({
            username: testUser.username,
            email: testUser.email,
            password: testUser.password
        });
        console.log("✅ User Created:", newUser.id);
        console.log(newUser);
        console.log("--------------------------------------------------\n");


        // --- TEST 2: SIGN IN ---
        console.log(`2️⃣  Testing signIn()...`);
        const loggedInUser = await db.auth.signIn(testUser.username, testUser.password);
        
        console.log("✅ Login Successful:", loggedInUser.username);
        console.log("--------------------------------------------------\n");


        // --- TEST 3: UPDATE USER ---
        console.log(`3️⃣  Testing updateUser()...`);
        const randomPhone = `+1-555-${Math.floor(Math.random() * 9000) + 1000}`;

        const updates = {
            phone: randomPhone, 
        };

        const updatedUser = await db.auth.updateUser(loggedInUser.id, updates);
        
        console.log("✅ Profile Updated:", updatedUser.phone);
        console.log(updatedUser);
        console.log("--------------------------------------------------\n");


        // --- TEST 4: GET USER ID ---
        console.log(`4️⃣  Testing getUserId()...`);
        const idResult = await db.auth.getUserId(testUser.username);
        
        console.log("✅ ID Fetched:", idResult.id);
        console.log("--------------------------------------------------\n");

        console.log("🎉 ALL TESTS PASSED!");

    } catch (err) {
        console.error("\n❌ TEST FAILED:");
        console.error(err.message);
        

    }
}


runTests();


