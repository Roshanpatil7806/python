import json

# ==========================================
# 1. Create JSON data
# ==========================================

policy = {
    "policy_id": "POL1001",
    "customer_name": "Rahul",
    "age": 30,
    "policy_type": "Health Insurance",
    "premium": 15000,
    "active": True
}


# ==========================================
# 2. Write JSON data to file
# ==========================================

with open("policy.json", "w") as file:
    json.dump(policy, file, indent=4)

print("Policy data written successfully!")


# ==========================================
# 3. Read JSON file
# ==========================================

with open("policy.json", "r") as file:
    data = json.load(file)

print("\nPolicy Details:")
print("Policy ID:", data["policy_id"])
print("Customer:", data["customer_name"])
print("Age:", data["age"])
print("Policy Type:", data["policy_type"])
print("Premium:", data["premium"])
print("Active:", data["active"])