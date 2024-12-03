from Logic.validate import validate_LL

#runs the program using if __name__ == '__main__': main()
if __name__ == "__main__":
    test = validate_LL()
    test2 = validate_LL()
    if test.validate_email("John@gmail.com"):
        print("Email is valid")
    else:
        print("Email is not valid")
