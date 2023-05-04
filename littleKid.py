# This program evaluates the identity of a person.

print('Who are you?')   # ask for their name
name = input()
print('How old are you?')   # ask for their age
age = int(input())
if name == 'Alice':
    print('Hi Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
