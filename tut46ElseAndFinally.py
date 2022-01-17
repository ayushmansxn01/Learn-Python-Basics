try:
    f=open("file11")

except Exception as e:
    print("file not found")

else:
    print("this will run if except is not run")

finally:
    print("this is important stuff that must be printed")
    try:
        f.close()
    except Exception as e:
        print("not found to close")


print("Rest of code")

# finally is done to wrap up the code or close the files you have opened
# else will get printed when except is not executed