text = "the quick brown fox jumps over the lazy dog"

alphabets=abcdefghijklmnopqrstuvwxyz:

is_pangram=True

for ch in alphabets:

    if ch not in text:

    is_pangram=false
    break
print(is_pangram)
