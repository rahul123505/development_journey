text="ahdjjdutersasbasvnvanaliiioAEIOU"

vowels = "aeiou"

v_count = 0

for ch in text:
    
    if ch in vowels:
        v_count+= 1
print(v_count)