def say_hello():
    print("Hello from my_module!")


print('Outside the function')
x = 15


if __name__ == "__main__":
    print("This code is executed when running my_module.py directly.")
    print(x)
    say_hello()
