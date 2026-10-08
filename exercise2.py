# Student Parameters
LAST_NAME = "Santos"
STUDENT_ID = "TUPM-26-1866"
SEED_NUM = int(STUDENT_ID[-1])  # 6
FAVORITE_ARTIST = "TWICE"

# 1. Generate Student Names
student_names = [f"Student_{LAST_NAME}_{i}" for i in range(1, 6)]

# 2. Derive Base Marks from FAVORITE_ARTIST ASCII values
base_marks = [ord(char) % 50 + 50 for char in FAVORITE_ARTIST[:5]]

# 3. Construct Student Performance Dictionary
students_data = {}
subjects = ["Math", "Physics", "Programming"]

for i, name in enumerate(student_names):
    mark = base_marks[i]
    students_data[name] = {
        "Math": min(100, mark + SEED_NUM),
        "Physics": max(50, mark - SEED_NUM),
        "Programming": min(100, mark + (SEED_NUM * 2))
    }

# 4. Add Incomplete Student Record
students_data[f"Student_{LAST_NAME}_Inc"] = {"Math": 85}

# 5. Process Performance Summaries with Default Values (Fault-Tolerant)
from collections import defaultdict

subject_totals = defaultdict(list)
student_averages = {}

for st_id, marks in students_data.items():
    default_val = 60 + SEED_NUM
    m_score = marks.get("Math", default_val)
    p_score = marks.get("Physics", default_val)
    pr_score = marks.get("Programming", default_val)
    
    subject_totals["Math"].append(m_score)
    subject_totals["Physics"].append(p_score)
    subject_totals["Programming"].append(pr_score)
    
    avg = (m_score + p_score + pr_score) / 3
    student_averages[st_id] = avg

print("=== ASSESSMENT DATA: EXERCISE 2 ===")
print("1. STUDENT MARKS DATABASE:")
for st, m in students_data.items():
    print(f"{st}: {m}")

print("\n2. STUDENT AVERAGES:")
for st, avg in student_averages.items():
    print(f"{st}: {avg:.2f}")

print("\n3. SUBJECT CLASS AVERAGES:")
for subj, scores in subject_totals.items():
    print(f"{subj} Class Avg: {sum(scores)/len(scores):.2f}")