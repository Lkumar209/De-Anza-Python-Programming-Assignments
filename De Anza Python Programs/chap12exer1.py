import csv

def read_order(filename):
    order_dict = {}
    total_order_dict = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter='\t')

        for row in reader:
            burger_num = row[0]
            quantities = list(map(int, row[1:]))

            order_dict[burger_num] = quantities
            total_order_dict[burger_num] = sum(quantities)

    return total_order_dict

def write_order_csv(order_dict, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        for burger_num, quantities in order_dict.items():
            writer.writerow([burger_num, sum(quantities)])

if __name__ == "__main__":
    actual_result_total_order_dict = read_order("order.csv")
    expected_result_total_order_dict = {'1': 91, '2': 100, '3': 32, '4': 62, '5': 64}

    for burger_num, expected_total in expected_result_total_order_dict.items():
        assert actual_result_total_order_dict[burger_num] == expected_total, f"The actual result is not the same as the expected result for the order number {burger_num}!"

    print("Everything passed")
    write_order_csv(actual_result_total_order_dict, "outputfile.csv")
