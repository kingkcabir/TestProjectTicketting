text = input("input your words")
for ch in text:
    if ch in 'AaEeIiOoUu':
        print("vowel_count:", ch, end=" ,")
