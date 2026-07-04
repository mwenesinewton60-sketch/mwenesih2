import random
import string

def gen_pass(length=10):
    characters = string.ascii_letters + string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password

if __name__=="__main__":
    length= int(input("Enter what u wanna be the length of the password:"))
    password= gen_pass(length)
    print("Your generated password is:",password)
