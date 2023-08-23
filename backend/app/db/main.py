import pymysql

class Connection:
    def __init__(self, hostname = 'mysql', port = 3306, username = 'root', password = '123456', database = 'loja') -> None:
        self.__connection = pymysql.connect(host=hostname, port=port, user=username, passwd=password, database=database)
    
    def __del__(self):
        self.__connection.close()

    def executeSelect(self, table, params = None):
        try:
            with self.__connection.cursor() as cursor:
                query = f"SELECT * from {table}"
                if params:
                    params = [f"{item[0]}='{item[1]}'" if item[2] == 'str' else f"{item[0]}={item[1]}" for item in params]
                    query += f" WHERE {' AND '.join(params)}"
                cursor.execute(query) 
                result = cursor.fetchall()
                if len(result) == 0:
                    raise Exception("Resultado vazio")
                return result
        except Exception as error:
            raise Exception(error)
        
    def executeInsert(self, table, params = None):
        try:
            with self.__connection.cursor() as cursor:
                params = [(item[0], f"'{item[1]}'") if item[2] == 'str' else (item[0], item[1]) for item in params]
                query = f"INSERT INTO {table} ({','.join(item[0] for item in params)}) VALUES ({','.join(item[1] for item in params)})"
                print(query)
                if not cursor.execute(query):
                    raise Exception("Erro ao inserir item")
                self.__connection.commit()
        except Exception as error:
            raise Exception(error)
