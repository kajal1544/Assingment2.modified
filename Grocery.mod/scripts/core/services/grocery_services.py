from fastapi import APIRouter
from scripts.core.handlers.grocery_handler import Grocery_handler
from scripts.core.handlers.email_handler import Email
from schemas.model import Grocery
from scripts.core.handlers.email_handler import Email_handler
from scripts.constants.app_constants import EndPoints

item_router = APIRouter()

grocery_handler = Grocery_handler()


@item_router.post(EndPoints.adding_item)
def adding_items(collection: Grocery):
    try:
        return grocery_handler.add_item(item_id=collection.item_id, item=collection.dict())
    except Exception as e:
        print("error in add_items", str(e))


@item_router.delete(EndPoints.deleting_item)
def deleting_item(item_id: int):
    try:
        return grocery_handler.delete_item(item_id=item_id)

    except Exception as e:
        return {"Error": str(e)}


@item_router.put(EndPoints.updating_item)
def updating_item(collection: Grocery):
    try:
        return grocery_handler.update_item(item_id=collection.item_id, updated_item=collection.dict())
    except:
        return {"Error"}


@item_router.get(EndPoints.getting_items)
def fetch():
    try:
        print("Welcome to grocery")
        return grocery_handler.get_item()
    except Exception as e:
        return {"Error": str(e)}


@item_router.get(EndPoints.total_amount)
def total_price():
    try:
        item_handler = Grocery_handler()
        result = item_handler.find_total()
        return result
    except Exception as e:
        return {"Error": str(e)}


@item_router.post(EndPoints.sending_email)
def sending_item(email: Email):
    try:
        item_object = Email_handler()
        send_items = item_object.send_email(email)
        return "Email sent successfully"
    except Exception as e:
        return ({"Error": str(e)})


@item_router.get(EndPoints.fetching_total)
def find_total():
    try:
        return grocery_handler.find_total()
    except Exception as e:
        return ({"Error": str(e)})
