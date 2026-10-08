# Student Parameters
LAST_NAME = "Santos"
STUDENT_ID = "TUPM-26-1866"
SEED_NUM = int(STUDENT_ID[-1])  # 6
FAVORITE_ARTIST = "TWICE"

# 1. Generate Test Sources (T1 to T5)
test_sources = [f"{LAST_NAME}_T{i}" for i in range(1, 6)]

# 2. Categories
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

# 3. Derive Values from FAVORITE_ARTIST ASCII + SEED_NUM
artist_values = [ord(char) + SEED_NUM for char in FAVORITE_ARTIST]

# 4. Generate Records
generated_records = [
    {"source": test_sources[0], "category": categories[0], "value": artist_values[0]}, # T1, TEMP, 90
    {"source": test_sources[1], "category": categories[1], "value": artist_values[1]}, # T2, VOLT, 93
    {"source": test_sources[2], "category": categories[2], "value": artist_values[2]}, # T3, CURR, 79
    {"source": test_sources[3], "category": categories[3], "value": artist_values[3]}, # T4, PRES, 73
    {"source": test_sources[4], "category": categories[4], "value": artist_values[4]}, # T5, SPEED, 75
    # Additional measurements under multiple categories
    {"source": test_sources[0], "category": categories[0], "value": artist_values[1]}, # T1, TEMP, 93
    {"source": test_sources[1], "category": categories[1], "value": artist_values[2]}, # T2, VOLT, 79
    # Repeated record (Duplicate of Record 1)
    {"source": test_sources[0], "category": categories[0], "value": artist_values[0]}  # T1, TEMP, 90
]

# 5. Identify Repeated and Distinct Data
seen = set()
repeated = []
distinct = []

for rec in generated_records:
    rec_tuple = (rec["source"], rec["category"], rec["value"])
    if rec_tuple in seen:
        repeated.append(rec)
    else:
        seen.add(rec_tuple)
        distinct.append(rec)

# 6. Categorical & Numerical Summaries
from collections import defaultdict
cat_summary = defaultdict(list)
for rec in distinct:
    cat_summary[rec["category"]].append(rec["value"])

print("=== ASSESSMENT DATA: EXERCISE 1 ===")
print("1. GENERATED TEST DATA:")
for r in generated_records:
    print(r)

print("\n2. REPEATED RECORDS:")
for r in repeated:
    print(r)

print("\n3. DISTINCT RECORDS:")
for r in distinct:
    print(r)

print("\n4. CATEGORICAL SUMMARIES:")
for cat, vals in cat_summary.items():
    avg_v = sum(vals) / len(vals)
    print(f"[{cat}] Count: {len(vals)} | Min: {min(vals)} | Max: {max(vals)} | Avg: {avg_v:.2f}")