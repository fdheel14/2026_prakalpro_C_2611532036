nim = input().split()
submitted = input().split()

set_submitted = set(submitted)

not_submitted = set(nim) - set_submitted

print(f"Submitted: {len(set_submitted)} students")
print(f"Not submitted: {len(not_submitted)} students")

for num in nim:
    if num in not_submitted:
        print(num)
