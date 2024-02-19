slowa_kluczowe = ['for', 'print', 'break', 'done', 'bad']

for slowo in slowa_kluczowe:
    print(f"{slowo} to słowo kluczowe: {slowo in dir(__builtins__)}")