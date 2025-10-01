def char_frequency(text):
    freq = {}
    seen = set()  
    for char in text:
        if char != " " and char != ",":
          
            if char.lower() not in seen:
                total = text.lower().count(char.lower())
                freq[char] = total 
                seen.add(char.lower())
    return freq

user_input = input("Enter string: ")

parts = [part.strip() for part in user_input.split(",")]

for part in parts:
    result = char_frequency(part)
    output = ", ".join([f"{k}={v}" for k, v in result.items()])
    print(output)




