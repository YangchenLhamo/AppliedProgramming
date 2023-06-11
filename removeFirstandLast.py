def remove_firstchar(char):
    String=char[1:]
    return String

def remove_lastchar(char):
    String=char[:-1]
    return String

character=input("Enter a character: ")
print(remove_firstchar(character))
print(remove_lastchar(character))