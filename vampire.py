# This program evaluates the identity of a person.

print('Who are you?')   # ask for their name
name = input()
print('How old are you?')   # ask for their age
age = int(input())
if name == 'Alice':
    print('Hi Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, inmortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('Get the hell out of here impostor')
