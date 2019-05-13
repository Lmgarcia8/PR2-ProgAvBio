class Store():
    """
    Class representing a store
    """

    def remove_products(self, product_name: str, amount: int = 20):
        pass

    def there_are_enough_products(self, product_name: str, amount: int) -> bool:
        pass


store = Store()
store.remove_products("cocacola", 125)
store.remove_products("leche")
store.remove_products(amount=15, product_name="cafe")
