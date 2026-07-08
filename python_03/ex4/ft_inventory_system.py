import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        else:
            item_name = parts[0]
            if item_name in inventory:
                print(f"Redundant parts '{item_name}' - discarding")
                continue
            try:
                item_quantity = int(parts[1])
            except ValueError as error:
                print(f"Quantity error for '{item_name}': {error}")
                continue
        inventory.update({item_name: item_quantity})
    print(f"Got inventory: {inventory}")
    if not inventory:
        return
    item_lst = list(inventory.keys())
    item_quan_lst = list(inventory.values())
    print(f"Item list: {item_lst}")
    total_quantity = sum(item_quan_lst)
    print(f"Total quantity of the {len(item_lst)} items: {total_quantity}")
    most_item = ""
    most_quantity = 0
    least_item = ""
    least_quantity = 0
    first = True
    for item in inventory:
        percentage = round(inventory[item] / total_quantity * 100, 1)
        print(f"Item {item} represents {percentage}%")
        if inventory[item] > most_quantity:
            most_item = item
            most_quantity = inventory[item]
        if first:
            least_item = item
            least_quantity = inventory[item]
            first = False
        elif inventory[item] < least_quantity:
            least_item = item
            least_quantity = inventory[item]
    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
