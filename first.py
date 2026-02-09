memory = {}

while True:
    cmd = input("Ты: ")

    if cmd.startswith("распбот запомни"):
        fact = cmd.replace("распбот запомни", "").strip()
        memory["fact"] = fact
        print("Raspbot: я запомнил и заменил старое")

    if cmd == "распбот что ты помнишь":
        if "fact" in memory:
            print("Raspbot помнит:", memory["fact"])
        else:
            print("Raspbot: я пока ничего не помню")