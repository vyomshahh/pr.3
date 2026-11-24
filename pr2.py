print(" ")
print("Welcome to the Pattern Generator and Number Analyzer!")
print(" ")
while True:
    print("Select an option:")
    print(" ")
    print("1.Generte a Pattern")
    print(" ")
    print("2.Analyze a Range of Numbers")
    print(" ")
    print("3.Exit")
    print(" ")


    choice =int(input("Enter your choice:"))

    if choice<=0|choice>3:
        print("Invaild choice,Enter valid choice!")
        continue


    elif choice == 1:

        a=int(input("Enter your rows number:"))

        for i in range(0,a):
            for j in range(1,i+1):
                 print("*",end=" ")
            print()

    elif choice == 2:

        start=int(input("Enter your start number of range :"))
        end=int(input("Enter your end number of range :"))

        total_sum = 0
        for i in range(start,end+1):
            if i % 2 == 0:
                print(f"{i} is even")
            else:
                print(f"{i} is odd")
            total_sum +=i
        print(f"The sum of numbers from{start} to {end} is: {total_sum}")

    elif choice == 3:
        print(" ")
        print("Exiting the program.Goodbye!")
        break