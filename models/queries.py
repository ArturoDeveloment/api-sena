from conexion import Conexion

class RequestDataBase:
    conexion = Conexion()

    def query_insert(self, table: str, columns_titles: list, columns_values: list):
        columns_into = ",".join([i for i in columns_titles])
        empty_spaces = ",".join(['?' for i in range(len(columns_titles))])
        values = tuple([str(i) for i in columns_values])
        query_execute = f"INSERT INTO {table} ({columns_into}) VALUES ({empty_spaces})", values
        self.conexion.execute_commit(query_execute)

    def query_update(self, table: str, columns_of_where: dict, columns_titles: list, columns_values: list):
        columns_into = ",".join([f'{i}'+'=?' for i in columns_titles])
        where_column = "".join(list(columns_of_where.keys()))
        columns_values.append(list(columns_of_where.values())[0])
        query_execute = f"UPDATE {table} SET {columns_into} WHERE {where_column}=?", tuple(columns_values)
        self.conexion.execute_commit(query_execute)

    def show_registers(self, table: str = None, query: list = None, columns_of_where: dict = {'id': None}):
        query = ",".join([i for i in query])
        # varibales for where 
        column_where_title = list(columns_of_where.copy().keys())[0]
        column_where_value = columns_of_where.copy().get(column_where_title)
        query_execute = f"SELECT {query} FROM {table} WHERE {column_where_title}=?", tuple([column_where_value])
        query = self.conexion.execute_commit(query_execute)
        data = [i for i in query]
        return data


rq = RequestDataBase()
execute = rq.query_insert('prueba', ['name', 'description'], ['carlos', 'prueba2'])
print(execute)
execute = rq.query_update('prueba', {'id': 2}, ['name'], ['ortiz'])
print(execute)
execute = rq.show_registers('prueba', ['name'], {'name': 'carlos'})
print(execute)