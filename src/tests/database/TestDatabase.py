from src.database.DbDao import DbDao
from src.database.database import Database
from src.database.database_initializator import intitialize_database

import unittest


class TestDatabase(unittest.TestCase):

    dbDao = DbDao()

    def setUp(self):
        self.numberOfRow = self.dbDao.getNomberOfRow()

    def test_add(self):

        numberOfRowBeforeAdding = self.dbDao.getNomberOfRow()
        self.dbDao.addCalcul("8 + 8", "16")
        numberOfRowAfterAdding = self.dbDao.getNomberOfRow()
        self.assertTrue(numberOfRowAfterAdding > numberOfRowBeforeAdding)

    def test_delete(self):

        self.dbDao.deleteCalcul(self.numberOfRow)
        numberOfRowAfterDeleting = self.dbDao.getNomberOfRow()
        print(numberOfRowAfterDeleting)

        self.assertNotEqual(self.numberOfRow, numberOfRowAfterDeleting)
        self.assertEqual(self.numberOfRow-1, numberOfRowAfterDeleting)

    def test_result_in_databse(self):
        rowid = self.dbDao.addCalcul("9 + 9", "16")
        result = self.dbDao.getResultById(rowid)
        self.assertEqual(16, result)

    def test_input_in_databse(self):
        rowid = self.dbDao.addCalcul("9 + 9", "16")
        input = self.dbDao.getInputById(rowid)
        self.assertEqual("9 + 9", input)

    @classmethod
    def setUpClass(cls):
        intitialize_database()

    @classmethod
    def tearDownClass(cls):
        cls.dbDao.deleteAllCalcul()


if __name__ == '__main__':
    unittest.main()
