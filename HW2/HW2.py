def char_frequency(text):
    freq = {}
    seen = set()
    for char in text:
        if char != " " and char != ",":  
            if char.lower() not in seen:  
                total = text.lower().count(char.lower())

                if char.upper() in text:
                    freq[char.upper()] = total
                else:
                    freq[char] = total
                seen.add(char.lower())
    return freq

user_input = input("Enter string: ")


parts = [part.strip() for part in user_input.split(",")]

for part in parts:
    result = char_frequency(part)

    output_list = []
    for item in result.items():
        key = item[0]    
        value = item[1]    
        output_list.append(f"{key}={value}")

    output = ", ".join(output_list)
    print(output)
