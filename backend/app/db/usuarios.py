from app.db.main import Connection

class UsuarioDB:
    def __init__(self):
        pass
    def getAllUsuarios(self):
        try:
            conn = Connection()
            results = conn.executeSelect("usuario")
            return results
        except Exception as error:
            print(error)

    def getUsuario(self, where):
        try:
            conn = Connection()
            conn.executeSelect("usuario", where)
            return True
        except Exception as error:
            print(error)
            return False
