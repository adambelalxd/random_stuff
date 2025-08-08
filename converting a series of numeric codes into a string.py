codes = []
finished_string = ""

while True:
    user_code = int(input("Enter a numeric code: "))
    codes.append(user_code)
    finished = str(input("Finished? (Y/N): "))
    if finished == "Y" or finished == "y":
        break
    else:
        ""

"104 101 108 108 111 = hello"
    
print(f"Codes = {codes}")

for code in codes:
    print(f"{code} = {chr(code)}")
    finished_string += chr(code)

print(finished_string)
