import psycopg

# Connect to an existing database
with psycopg.connect("dbname=postgres user=postgres host=localhost password=wedics404 port=5432") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.
        sql = "CREATE DATABASE my_db"

        cur.execute(sql)
        print('Database has been created successfully')

        # Make the changes to the database persistent
        conn.commit()