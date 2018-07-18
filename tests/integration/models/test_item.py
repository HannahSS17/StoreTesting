from models.item import ItemModel
from models.store import StoreModel
from tests.integration.integration_base_test import BaseTest


class ItemTest(BaseTest):
    def test_create_items(self):
        with self.app_context():
            item = ItemModel('test', 19.99, 1)

            # check if the item does not exist already in the database before we save it there
            self.assertIsNone(ItemModel.find_by_name('test'))

            # save item to SQLite file database
            item.save_to_db()

            # check if the item exists
            self.assertIsNotNone(ItemModel.find_by_name('test'), f'Found an item with the name {item.name},'
                                                                 'but not expected.')

            item.delete_from_db()

            # check if item does not exist in database after deleting it
            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')




