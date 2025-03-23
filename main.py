
from product_manager import ProductManager
from product import Product


def main():
    manager = ProductManager()

    manager.add_product(Product("Laptop", 1200.99, 9))
    manager.add_product(Product("Mouse", 25.50, 21))
    manager.add_product(Product("Keyboard", 45.00, 11))
    manager.add_product(Product("Monitor", 250.75, 12))

    #print("Available Products:")
    #manager.display_all_products()

    #total_value = manager.total_inventory_value()
    #print(f"\nTotal Inventory Value: ${total_value:.2f}")
    

if __name__ == "__main__":
    main()
    