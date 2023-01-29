from sqlite3 import Error
from src.database.database import Database
from src.database.database_initializator import intitialize_database


class DbDao:

    def __init__(self):
        self.db_connexion = Database().create_connection()

    def addCalcul(self, body, result):
        """
        Delete a calcul 
        :param conn:  Connection to the SQLite database
        :param body: body of the calcul
        :param result: result of the calcul
        :return:
        """
        try:
            sql = ''' INSERT INTO HISTORIQUE(INPUT,RESULT) values (?,?) '''
            cur = self.db_connexion.cursor()
            cur.execute(sql, (body, result))
            self.db_connexion.commit()
            return (cur.lastrowid)
        except Error as e:
            print(e)

    def getAllCalculs(self):
        """
        Get All calcul
        :param conn:  Connection to the SQLite database
        :return: list
        """
        try:
            sql = ''' SELECT  rowid,INPUT,RESULT FROM HISTORIQUE ORDER BY rowid DESC'''
            cur = self.db_connexion.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(e)

    def deleteCalcul(self, rowid):
        """
        Delete a calcul by calcul id
        :param conn:  Connection to the SQLite database
        :param rowid: id of the calcul
        :return:
        """
        try:
            sql = ''' DELETE FROM HISTORIQUE WHERE rowid = ?'''
            cur = self.db_connexion.cursor()
            cur.execute(sql, (rowid,))
            self.db_connexion.commit()
        except Error as e:
            print(e)

    def deleteAllCalcul(self):
        """
        Delete a calcul by calcul id
        :param conn:  Connection to the SQLite database
        :param rowid: id of the calcul
        :return:
        """
        try:
            sql = ''' DELETE FROM HISTORIQUE '''
            cur = self.db_connexion.cursor()
            cur.execute(sql,)
            self.db_connexion.commit()
        except Error as e:
            print(e)

    def getResultById(self, rowid):
        """
        Get calcul by a given id
        :param conn:  Connection to the SQLite database
        :param rowid: id of the calcul
        :return: list
        """
        try:
            sql = ''' SELECT RESULT FROM HISTORIQUE WHERE rowid = ?'''
            cur = self.db_connexion.cursor()
            cur.execute(sql, (rowid,))
            rows = cur.fetchall()
            return rows[0][0]
        except Error as e:
            print(e)

    def getInputById(self, rowid):
        """
        Get calcul by a given id
        :param conn:  Connection to the SQLite database
        :param rowid: id of the calcul
        :return: list
        """
        try:
            sql = ''' SELECT INPUT FROM HISTORIQUE WHERE rowid = ?'''
            cur = self.db_connexion.cursor()
            cur.execute(sql, (rowid,))
            rows = cur.fetchall()
            return rows[0][0]
        except Error as e:
            print(e)

    def getCalculById(self, rowid):
        """
        Get calcul by a given id
        :param conn:  Connection to the SQLite database
        :param rowid: id of the calcul
        :return: list
        """
        try:
            sql = ''' SELECT  rowid,INPUT,RESULT FROM HISTORIQUE WHERE rowid = ?'''
            cur = self.db_connexion.cursor()
            cur.execute(sql, (rowid,))
            rows = cur.fetchall()
            return rows
        except Error as e:
            print(e)

    def getNomberOfRow(self):
        """
        Get the number of row
        :return: str
        """
        try:
            sql = ''' SELECT COUNT(rowid) FROM HISTORIQUE'''
            cur = self.db_connexion.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            return rows[0][0]
        except Error as e:
            print(e)

    def __del__(self):
        self.db_connexion.close()

# if __name__ == '__main__':
#    db = DbDao()
#    db.deleteAllCalcul()
#    print(db.getNomberOfRow())
