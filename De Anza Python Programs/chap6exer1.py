# Laxya Kumar
# Friend List Management

# Define friend lists for 2017 and 2018
friends_2017 = ["Joe", "Lily"]
friends_2018 = ["Bob", "Tom"]

all_friends = friends_2017 + friends_2018

print("All Friends:", all_friends)

friend_name = input("Enter a friend's name: ")

if friend_name in friends_2017:
    print(f"{friend_name} was found in 2017.")
elif friend_name in friends_2018:
    print(f"{friend_name} was found in 2018.")
else:
    print(f"You don't have a friend named {friend_name} in your lists.")

new_friend_name = input("Enter a new friend's name: ")
year = int(input("Enter the year (2017 or 2018): "))

if year == 2017:
    friends_2017.append(new_friend_name)
elif year == 2018:
    friends_2018.append(new_friend_name)

print("2017 Friends:", friends_2017)
print("2018 Friends:", friends_2018)


'''
Result 1:
All Friends: ['Joe', 'Lily', 'Bob', 'Tom']
Enter a friend's name: Lily
Lily was found in 2017.
Enter a new friend's name: Emma
Enter the year (2017 or 2018): 2017
2017 Friends: ['Joe', 'Lily', 'Emma']
2018 Friends: ['Bob', 'Tom']



Result 2:
All Friends: ['Joe', 'Lily', 'Bob', 'Tom']
Enter a friend's name: Bob
Bob was found in 2018.
Enter a new friend's name: Mike
Enter the year (2017 or 2018): 2018
2017 Friends: ['Joe', 'Lily']
2018 Friends: ['Bob', 'Tom', 'Mike']


'''