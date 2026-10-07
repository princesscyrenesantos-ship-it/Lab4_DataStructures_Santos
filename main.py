from collections import defaultdict

# Student Identity
LAST_NAME = "Santos"
STUDENT_ID = "TUPM-26-1866"

sys_config = {
    "operator": LAST_NAME,
    "auth_id": STUDENT_ID,
    "base_seed": int(STUDENT_ID[-1]),
    "vector_dim": len(LAST_NAME)
}

# Task 14: Fault-Tolerant Key Mappings (Defaultdict)
# Initialize with a default integer factory (creates a 0 for missing keys)
default_data = defaultdict(int)

# Assign a known key
default_data['active_key'] = sys_config["vector_dim"]
print(f"Existing Key Value: {default_data['active_key']}")

# Accessing an uninitialized key will not throw a KeyError
print(f"Missing Key Value (Auto-generated): {default_data['unknown_key']}")