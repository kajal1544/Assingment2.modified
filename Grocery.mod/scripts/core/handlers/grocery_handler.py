from scripts.constants.aggregation import DatabaseConstants
from scripts.utility.mongo_utility import Mongoserver


class Grocery_handler:

    def __init__(self):
        self.mongo_server_obj = Mongoserver()

    def add_item(self, item_id: int, item: dict):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            return {"message": "This item already exists in the grocery collection."}
        else:
            self.mongo_server_obj.write_items(item)
            return {"message": "Item added successfully"}

    def get_item(self):
        data = list(self.mongo_server_obj.read_items())
        for items in data:
            del items['_id']
        return data

    def update_item(self, item_id: int, updated_item: dict):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            result = self.mongo_server_obj.update_details(item_id, updated_item)
            if result.modified_count == 1:
                return {"message": "Grocery is updated successfully"}
            else:
                return {"message": "Item not found"}
        return {"message": "item not found"}

    def delete_item(self, item_id: int):
        existing_item = self.mongo_server_obj.check_item(item_id)
        if existing_item:
            result = self.mongo_server_obj.delete_items(item_id)
            if result.deleted_count == 1:
                return {"message": "Item deleted successfully from the grocery collection"}
            else:
                return {"message": "Item not found"}
        return {"message": "item not found"}

    def find_total(self):
        try:
            db_constant_object = DatabaseConstants()
            total = self.mongo_server_obj.find_total(db_constant_object.aggregate)
            return total
        except Exception as e:
            return {"status": "failed", "error": str(e.args)}
