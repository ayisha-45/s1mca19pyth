input_string=input("enter a string: ")
if input_string.endswith('ing'):
    modified_string=input_string+'ly'
else:
    modified_string=input_string+'ing'
print("modified string: ",modified_string)

