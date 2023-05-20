from pymongo import MongoClient


class Mongoserver:

    def __init__(self):
        try:
            self.client_uri = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
            self.db = "interns_b2_23"
            self.collection = "grocery"
        except Exception as e:
            raise Exception(str(e))

    def check_item(self, item_id):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.find_one({"id": item_id})
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def write_items(self, item):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.insert_one(item)
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def read_items(self):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.find()
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def update_details(self, item_id, updated_item):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.update_one({"id": item_id}, {"$set": updated_item})
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def delete_items(self, item_id):
        try:
            mongo_collect = self.client_uri[self.db][self.collection]
            mongo_result = mongo_collect.delete_one({"id": item_id})
            return mongo_result
        except Exception as e:
            raise Exception(str(e))

    def find_total(self, agg):
        try:
            total = [self.collection].aggregate(agg)
            if total == 0:
                return total
            else:
                return (list(total))[0]['total']
        except Exception as e:
            return {"error": str(e)}
