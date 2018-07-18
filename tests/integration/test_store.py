from models.item import ItemModel
from models.store import StoreModel
from app import app
from tests.integration.integration_base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')

        self.assertListEqual(store.items.all(), [], 'The length of list was not 0')

    def test_create_items(self):
        with app.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'), f'Found a store with name {store.name},'
                                                               f' even it was not saved in the database')

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'), f'the store with name {store.name} was not found')

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'), f'Found a store with name {store.name},'
                                                               f' even it was deleted from the database')

    def test_store_relationship(self):
        with app.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self):
        store = StoreModel('test')
        expected = {
            'name': 'test',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with app.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'test',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected)
