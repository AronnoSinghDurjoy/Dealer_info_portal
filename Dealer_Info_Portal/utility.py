import oracledb

def fetch_dealer_info(short_code, hierarchy_level, start_date, end_date):
    try:
        user =
        password =
        dsn =

        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        cursor = connection.cursor()

        def return_strings_as_bytes(cursor, metadata):
            if metadata.type_code is oracledb.DB_TYPE_VARCHAR:
                return cursor.var(str, arraysize=cursor.arraysize, bypass_decode=True)
        cursor.outputtypehandler = return_strings_as_bytes

        # Query: filter by date only (ignoring time) on LOAD_DATA_TS
        query = f'''
        
        '''

        cursor.execute(query)
        column_names = [col[0] for col in cursor.description]
        results = [
            [r.decode('latin-1') if isinstance(r, bytes) else r for r in row]
            for row in cursor.fetchall()
        ]

        cursor.close()
        connection.close()

        return column_names, results

    except oracledb.DatabaseError as e:
        return str(e), []