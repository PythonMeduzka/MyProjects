def letter_big(x):
    words = x.lower().split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def check(text, actions, books):
    while True:
        function = input(text)
        if function in actions:
            return actions[function](books)
        else:
            print("Виберіть допустимий варіант.")


def file_writing_all(blokName, x):
    with open(blokName, "w", encoding="utf-8") as file:
        file.truncate()
        file.write('')
        for z in x:
            file.write(f"ID:  {z[0]}\n")
            file.write(f"Назва книги: {z[1]}\n")
            file.write(f"Автор: {z[2]}\n")
            file.write(f"Жанр: {z[3]}\n")
            file.write(f"Рік видання: {z[4]}\n")
            file.write(f"ISBN: {z[5]}\n")
            file.write("-------------------------------\n")
