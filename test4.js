import { Unibase } from "./unibase.js";

const API_URL = "http://localhost:5000"; 
const API_KEY = "YOUR_API_KEY_HERE"; 

const ub = new Unibase(API_URL, API_KEY);

// await ub.graph.createNode("Merchant_A", { location: "Mumbai" });
// await ub.graph.createNode("Rider_77", { vehicle: "Electric Scooter" });

await ub.graph.connect("Merchant_A", "Rider_77", "ASSIGNED_TO", { order_id: "ORD-101" });

// await ub.graph.disconnect("Merchant_A", "Rider_77", "ASSIGNED_TO");

