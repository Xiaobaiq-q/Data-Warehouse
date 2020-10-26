import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplay_table"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events (
    event_id 
""")

staging_songs_table_create = ("""
""")

songplay_table_create = ("""
CREATE TABLE songplay (
    songplay_id INT IDENTITY(0,1),
    start_time  TIMESTAMP NOT NULL, 
    user_id int, 
    level varchar(10), 
    song_id varchar(25),
    artist_id varchar(25),
    session_id int, 
    location varchar(25), 
    user_agent  text,
    primary key(songplay_id)
    );
""")

user_table_create = ("""
CREATE TABLE users(
    user_id int,
    first_name varchar(25),
    last_name varchar(25), 
    gender varchar(10),
    level varchar(10),
    primary key(user_id));
""")

song_table_create = ("""
    CREATE TABLE songs(
        song_id varchar(25) not null, 
        title varchar(50) not null,
        artist_id varchar(25) not null, 
        year int, 
        duration float,
        primary key(song_id)
        );
""")

artist_table_create = ("""
    CREATE TABLE artists(
        artist_id varchar(25) not null, 
        name varchar(25) not null, 
        location(25) varchar,
        latitude float, 
        longitude float,
        primary key(artists_id)
        );
""")

time_table_create = ("""
    CREATE TABLE times(
        start_time BIGINT,  
        hour int, 
        day int, 
        week int, 
        month int, 
        year int, 
        weekday int,
        primary key(start_time)
        );
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
    INSERT INTO songplays( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level)
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
""")

time_table_insert = ("""
    INSERT INTO times(start_time, hour, day, week, month, year, weekday)
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
