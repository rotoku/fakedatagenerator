def snake_to_camel(snake_word):
    # Split the word by underscore and capitalize the first letter of each part
    camel_word = ''.join(word.capitalize() for word in snake_word.split('_'))
    
    return camel_word

if __name__ == "__main__":
    snake_word = input("Faça sua pergunta: ")
    print(f"Original Snake Case: {snake_word}")
    print(f"Camel Case: {snake_to_camel(snake_word)}")
    print()