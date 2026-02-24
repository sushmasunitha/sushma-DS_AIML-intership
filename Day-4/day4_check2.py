
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)
is_ID05_present = "ID05" in unique_users

original_count = len(raw_logs)
unique_count = len(unique_users)

print("=== Unique User IDs ===")
print(unique_users)

print("\n=== Membership Test ===")
print("Is ID05 in unique users?", is_ID05_present)

print("\n=== Count Comparison ===")
print("Original log count:", original_count)
print("Unique user count:", unique_count)