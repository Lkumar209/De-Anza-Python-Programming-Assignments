# Laxya Kumar

# Description: This code creates a table for figure skating medal counts using lists and dictionaries,
# prints the table, calculates the total number of medals and gold/silver/bronze medals,
# removes countries without a gold medal from the table,
# prints the updated table, and saves the data using dictionaries.

medal_table = [
    ["Country", "Gold", "Silver", "Bronze"],
    ["Canada", 0, 3, 0],
    ["Italy", 0, 0, 1],
    ["Germany", 0, 0, 1],
    ["Japan", 1, 0, 0],
    ["Russia", 3, 1, 1],
    ["South Korea", 0, 1, 0],
    ["United States", 1, 0, 1]
]

for row in medal_table:
    print("{:<15} {:<8} {:<8} {:<8}".format(*row))

total_medals = sum(sum(row[1:]) for row in medal_table[1:])
print("\nTotal Medals:", total_medals)

gold_medals = sum(row[1] for row in medal_table[1:])
silver_medals = sum(row[2] for row in medal_table[1:])
bronze_medals = sum(row[3] for row in medal_table[1:])
print("Gold Medals:", gold_medals)
print("Silver Medals:", silver_medals)
print("Bronze Medals:", bronze_medals)

medal_table = [row for row in medal_table[1:] if row[1] > 0]

print("\nUpdated Table:")
print("{:<15} {:<8} {:<8} {:<8}".format(*medal_table[0]))  
for row in medal_table[1:]:
    print("{:<15} {:<8} {:<8} {:<8}".format(*row))

medal_data = {
    "Canada": {"Gold": 0, "Silver": 3, "Bronze": 0},
    "Italy": {"Gold": 0, "Silver": 0, "Bronze": 1},
    "Germany": {"Gold": 0, "Silver": 0, "Bronze": 1},
    "Japan": {"Gold": 1, "Silver": 0, "Bronze": 0},
    "Russia": {"Gold": 3, "Silver": 1, "Bronze": 1},
    "South Korea": {"Gold": 0, "Silver": 1, "Bronze": 0},
    "United States": {"Gold": 1, "Silver": 0, "Bronze": 1}
}

print("\nMedal Data:")
for country, medals in medal_data.items():
    print(country + ":")
    for medal, count in medals.items():
        print("{:<8}: {}".format(medal, count))
    print()


'''
Country         Gold     Silver   Bronze  
Canada          0        3        0       
Italy           0        0        1       
Germany         0        0        1       
Japan           1        0       0       
Russia          3        1        1       
South Korea     0        1        0       
United States   1        0        1       

Total Medals: 14
Gold Medals: 5
Silver Medals: 5
Bronze Medals: 4

Updated Table:
Country         Gold     Silver   Bronze  
Japan           1        0        0       
Russia          3        1        1       
United States   1        0        1       

Medal Data:
Canada:
Gold    : 0
Silver  : 3
Bronze  : 0

Italy:
Gold    : 0
Silver  : 0
Bronze  : 1

Germany:
Gold    : 0
Silver  : 0
Bronze  : 1

Japan:
Gold    : 1
Silver  : 0
Bronze  : 0

Russia:
Gold    : 3
Silver  : 1
Bronze  : 1

South Korea:
Gold    : 0
Silver  : 1
Bronze  : 0

United States:
Gold    : 1
Silver  : 0
Bronze  : 1



'''