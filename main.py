logregel = f"{datetime.now()} | {data}"
print(logregel)

with open("logs.txt", "a") as file:
    file.write(logregel + "\n")
