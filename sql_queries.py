import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events (
    event_id INT IDENTITY(0,1),
    artist_name varchar(255),
    auth varchar(50),
    user_fisrt_name varchar(255),
    user_gender varchar(1),
    item_in_session int,
    user_last_name varchar(255),
    length DOUBLE PRECISION,
    user_level varchar(50),
    user_location varchar(255),
    method varchar(25),
    page varchar(50),
    registration varchar(50),
    session_id BIGINT,
    song varchar(255),
    status int,
    ts BIGINT,
    user_agent text,
    user_id varchar(100),
    primary key(event_id))  
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs(
    song_id  varchar(100),
    num_songs int,
    artist_id varchar(100),
    artist_latitude DOUBLE PRECISION,
    artist_longitude DOUBLE PRECISION,
    artist_loaction varchar(255),
    artist_name varchar(255),
    title  varchar(255),
    duration DOUBLE PRECISION,
    year int,
    primary key (song_id)
);
""")

songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id INT IDENTITY(0,1),
    start_time  TIMESTAMP not null, 
    user_id varchar(100) not null, 
    level varchar(50), 
    song_id varchar(100) not null,
    artist_id varchar(100) not null,
    session_id BIGINT, 
    location varchar(255), 
    user_agent  text,
    primary key(songplay_id)
    );
""")

user_table_create = ("""
CREATE TABLE users(
    user_id varchar(100),
    first_name varchar(255),
    last_name varchar(255), 
    gender varchar(1),
    level varchar(50),
    primary key(user_id));
""")

song_table_create = ("""
    CREATE TABLE songs(
        song_id varchar(100), 
        title varchar(255),
        artist_id varchar(100) not null, 
        year int, 
        duration DOUBLE PRECISION,
        primary key(song_id)
        );
""")

artist_table_create = ("""
    CREATE TABLE artists(
        artist_id varchar(100), 
        name varchar(255), 
        location varchar(255),
        latitude DOUBLE PRECISION, 
        longitude DOUBLE PRECISION,
        primary key(artist_id)
        );
""")

time_table_create = ("""
    CREATE TABLE times(
        start_time TIMESTAMP,  
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
    copy staging_events 
    from {}
    iam_role {}
    json {};
""").format(config.get('S3','LOG_DATA'),config.get('IAM_ROLE','ARN'),config.get('S3','LOG_JSONPATH'))

staging_songs_copy = ("""
    copy staging_songs 
    from {}
    iam_role {}
    json 'auto';
""").format(config.get('S3','SONG_DATA'),config.get('IAM_ROLE','ARN'))

# FINAL TABLES

songplay_table_insert = ("""
    INSERT INTO songplays( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    SELECT 
    TIMESTAMP 'epoch' + e.ts/1000 * interval '1 second' as start_time,
    e.user_id, 
    e.user_level, 
    s.song_id,
    s.artist_id,
    e.session_id,
    e.user_location, 
    e.user_agent
    FROM staging_events e
    JOIN  staging_songs s
    ON e.song=s.title
    AND e.artist_name=s.artist_name 
    AND e.length=s.duration; 

""")

user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level) 
    SELECT DISTINCT
    user_id, 
    user_fisrt_name,
    user_last_name,
    user_gender,
    user_level
    FROM staging_events 
    WHERE user_id IS NOT NULL

""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
    SELECT DISTINCT
    song_id,
    title,
    artist_id,
    year,
    duration 
    FROM staging_songs
    WHERE song_id IS NOT NULL
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    SELECT DISTINCT
    artist_id,
    artist_name,
    artist_loaction,
    artist_latitude,
    artist_longitude
    FROM staging_songs
    WHERE artist_id IS NOT NULL
""")

time_table_insert = ("""
    INSERT INTO times(start_time, hour, day, week, month, year, weekday)
    SELECT start_time,
    extract (hour from start_time),
    extract (day from start_time),
    extract (week from start_time),
    extract (month from start_time),
    extract (year from start_time),
    extract (dayofweek from start_time)
    FROM songplays

""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]

