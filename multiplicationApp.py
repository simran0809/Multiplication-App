try:
    a = int(input("Enter the number: "))
    print(f"Multiplication table of {a} is:")

    for i in range(1, 101):
        print(f"{int(a)} X {i} = {int(a) * i}")

# except ValueError:
#     print("Please enter a valid integer.")

except Exception as e:
    print(e)

#finally:
    print("Some important lines")
    print("End of program")
