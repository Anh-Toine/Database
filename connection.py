import mysql.connector

config_file = "my.conf"

dbconn = mysql.connector.connect(option_files = config_file)

# Create cursor
dbcrs = dbconn.cursor()

#Create query
selectall = ("SELECT * FROM channel")

selectlike = ("SELECT channel_id,channel_name,creation_date,verified,genre_name FROM channel c \
            LEFT JOIN genre g \
            ON g.genre_id = c.genre_id \
            WHERE channel_name LIKE %s")

dbcrs.execute(selectlike,('A%',))
#dbcrs.execute(selectall)
dbrset = dbcrs.fetchall()

for row in dbrset:
    print(row)

dbcrs.close()
dbconn.close()