# Laxya Kumar
# Description: This code creates a dictionary of friends found in 2017 and 2018,
# allows the user to search for a friend's name, and gives the option to add a new friend to the respective year's list.

def main():
    
    friend_dict = {
        2017: ["Joe", "Lily"],
        2018: ["Bob", "Tom"]
    }

    
    print("Friend's names:")
    for year in friend_dict:
        print(f"Year {year}: {', '.join(friend_dict[year])}")

    
    name = input("Enter a name of a friend: ")

    
    found = False
    for year in friend_dict:
        if name in friend_dict[year]:
            print(f"{name} was found in {year}.")
            found = True
            break

    
    if not found:
        print(f"{name} was not found.")

    
    new_friend = input("Enter a new friend's name: ")
    new_year = int(input("Enter the year (2017 or 2018): "))

    
    if new_year in friend_dict:
        friend_dict[new_year].append(new_friend)
    else:
        friend_dict[new_year] = [new_friend]

    
    print("Updated friend's dictionary:")
    for year in friend_dict:
        print(f"Year {year}: {', '.join(friend_dict[year])}")



if __name__ == '__main__':
    main()


'''
Result 1:

Friend's names:
Year 2017: Joe, Lily
Year 2018: Bob, Tom
Enter a name of a friend: Bob
Bob was found in 2018.
Enter a new friend's name: Alice
Enter the year (2017 or 2018): 2018
Updated friend's dictionary:
Year 2017: Joe, Lily
Year 2018: Bob, Tom, Alice


Result 2:

Friend's names:
Year 2017: Joe, Lily
Year 2018: Bob, Tom
Enter a name of a friend: Lily
Lily was found in 2017.
Enter a new friend's name: Kate
Enter the year (2017 or 2018): 2019
Updated friend's dictionary:
Year 2017: Joe, Lily, Kate
Year 2018: Bob, Tom
Year 2019: Kate



'''
