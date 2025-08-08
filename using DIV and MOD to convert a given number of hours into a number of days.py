days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours = int(input("Enter how many hours you want: "))
num_days = hours // 24
num_days = num_days % 7
print(days[num_days])