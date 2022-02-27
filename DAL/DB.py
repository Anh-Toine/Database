import mysql.connector
from mysql.connector import optionfiles

class DB(object):

    def __init__(self):
        try:
            self.config_file = "my.conf"
            self.connections = mysql.connector.connect(option_files = self.config_file)
        except mysql.connector.Error as mse:
            print(mse)
            self.close()

    def execute_select(self, table_one:str, table_two:str,shared_val:str, params=None):
        result_set = []
        query = "SELECT channel_id,channel_name,creation_date,verified,genre_name FROM {0} \
                    LEFT JOIN {1} \
                    ON {0}.{2} = {1}.{2}".format(table_one,table_two,shared_val)
        cursor = self.connections.cursor(dictionary=True)
        if params is None:
            cursor.execute(query)
        else:
            print(query)
            
            where_clause = " WHERE " + " AND ".join(['`' + k + '` = %s' for k in params.keys()])
            print(where_clause)
            
            values = list(params.values())
            print(values)
            
            cursor.execute(query + where_clause, values)
        for x in cursor:
            result_set.append(x)
        
        cursor.close()
        return result_set

    