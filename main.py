def nerdify(text):
    # Mapping character changes 
    replacements = {
        'a': '4',
        'A': '4',
        'e': '3',
        'E': '3',
        'l': '1',
        'L': '1',
        'i': '1',
        'I': '1'
    }

    result = ''
    for char in text:
        # Determine replacement or use original character
        replacement = replacements.get(char, char)
        print(f"Processing character: {char}, Replacement: {replacement}")
        result += replacement
    

    print(f"Final result: {result}")

    return result

print(nerdify("Fundamentals"))  # "Fund4m3nt41s"
print(nerdify("Jonathan"))      # "Jon4th4n"
print(nerdify("Alexander"))     # "413x4nd3r"
print(nerdify("Carolina Code School")) # "C4ro11n4 Cod3 Schoo1"
print(nerdify("Develop Carolina"));# "D3v31op C4ro11n4"