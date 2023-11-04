text="Hello World!"
newVariable= text.split() #It gives a list ["Hello", "World"]
print(text.upper()) # It makes upper case
print(text.replace("H","W")) 
print(newVariable)
print(type(newVariable)) # It gives variable type
print(text[1]) #gives index 1

#text[first:last:step]
print(text[0:10:2]) 
print(text[3:])
print(text[:4])
print(text[::2])

#last

print(text[-2])

print(len(text)) # Degiskenin veya listenin uzunlugunu verir

print(text[::-1])
