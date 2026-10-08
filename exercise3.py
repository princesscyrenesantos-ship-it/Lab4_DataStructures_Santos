from collections import deque

# Student Parameters
LAST_NAME = "Santos"
STUDENT_ID = "TUPM-26-1866"
SEED_NUM = int(STUDENT_ID[-1])  # 6
FAVORITE_ARTIST = "TWICE"

# 1. Base Transactions Queue using Deque
tx_queue = deque()

# 2. Derive Transaction Amounts using ASCII values of FAVORITE_ARTIST
tx_amounts = [(ord(char) * SEED_NUM) for char in FAVORITE_ARTIST]

# 3. Populate Queue with Transactions
for i, amt in enumerate(tx_amounts, 1):
    tx_queue.append({
        "tx_id": f"TX_{LAST_NAME}_{i:03d}",
        "amount": amt,
        "type": "CREDIT" if i % 2 != 0 else "DEBIT"
    })

print("=== ASSESSMENT DATA: EXERCISE 3 ===")
print("1. INITIAL TRANSACTION QUEUE:")
for tx in tx_queue:
    print(tx)

# 4. Process Transactions (FIFO via popleft)
processed_tx = []
total_balance = 0

while tx_queue:
    current_tx = tx_queue.popleft()
    if current_tx["type"] == "CREDIT":
        total_balance += current_tx["amount"]
    else:
        total_balance -= current_tx["amount"]
    
    current_tx["running_balance"] = total_balance
    processed_tx.append(current_tx)

print("\n2. PROCESSED TRANSACTIONS (FIFO Order):")
for tx in processed_tx:
    print(tx)

print(f"\n3. FINAL ACCOUNT BALANCE: Php {total_balance:.2f}")