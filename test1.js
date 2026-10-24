import { Unibase } from "./unibase.js"; 

// CONFIGURATION
const API_URL = "http://localhost:5000"; 
const API_KEY = "YOUR_API_KEY_HERE"; // Replace with your actual key

// Initialize SDK
const db = new Unibase(API_URL, API_KEY);

// Sign Up
const newUser = await db.auth.signUp({ 
    username: 'werrrrr', 
    password: 'secure123', 
    
}).run();

console.log(newUser);


// Sign In
const session = await db.auth.signIn({ 
    username: 'werrr', 
    password: 'secure123' 
}).run();

console.log(session);