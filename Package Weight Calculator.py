from time import sleep

print("##### PACKAGE WEIGHT CALCULATOR V2 #####\n")

global limit

def main():
    def packer(list_of_weights):

        package = []
        overflow_list = []

        for i in sorted(list_of_weights, reverse = True):
            if sum(package) +i <= limit:
                package.append(i)
            else:
                overflow_list.append(i)

        print(f"Package: {package} Total Weight: {(sum(package))}")

        list_of_weights=overflow_list
        package = []
        overflow_list=[]
        if len(list_of_weights) > 0:
            packer(list_of_weights)

    while True:
        try:
            limit = int(input("Set Target Value:\n"))
            break
        except ValueError:
            print("Please enter a number\n")
        
    print(f"\nInput the list of weights separated by spaces, followed by ENTER.")

    while True:
        try:
            list_of_weights = [int(x) for x in input().split()]
            if (all(x<=limit for x in list_of_weights)):
                break
            else:
                print(f"One of your values is over {limit}. Please try again")
        
        except ValueError:
            print("Please Enter Only Numbers and Spaces")

    print("\n")

    packer(list_of_weights)

    again= input("\nStart Over? Y/N>")
    if "y".lower() in again.lower():
        print("\n")
        main()
    else:
        print("Goodbye...")
        sleep(1)
        quit()

main()
