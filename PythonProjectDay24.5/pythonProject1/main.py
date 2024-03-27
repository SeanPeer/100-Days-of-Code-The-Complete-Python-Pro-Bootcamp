#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(f"input/Letters/starting_letter.txt", "r") as text:
    template = text.read()


with open("input/Names/invited_names.txt", "r") as names:
    list_names = names.readlines()
    print(list_names)
    for name in list_names:
        noBack = name.strip()
        with open(f"output/ReadyToSend/invited_{noBack}.txt", "w") as new_text:
            new_text.write(template.replace("[name]", f"{noBack}")) # copying the template and paste it with the new name
