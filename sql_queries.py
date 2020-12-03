# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
songplay_table_create = (
    """create table if not exists songplays (
    songplay_id serial PRIMARY KEY, 
    start_time timestamp not null, 
    user_id varchar not null, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location varchar, 
    user_agent varchar)"""
)

# user_id, first_name, last_name, gender,level 
user_table_create = (
    """create table if not exists users(
    user_id varchar PRIMARY KEY, 
    first_name varchar, 
    last_name varchar, 
    gender varchar, 
    level varchar)"""
)

# song_id, title, artist_id, year, duration
song_table_create = (
    """create table if not exists songs(
    song_id varchar PRIMARY KEY, 
    title varchar, 
    artist_id varchar not null, 
    year int, 
    duration numeric)"""
)

# artist_id, name, location, latitude, longitude
artist_table_create = (
    """create table if not exists artists(
    artist_id varchar PRIMARY KEY, 
    name varchar, 
    location varchar, 
    latitude numeric, 
    longitude numeric)"""
)

# start_time, hour, day, week, month, year, weekday
time_table_create = (
    """create table if not exists time(
    start_time TIMESTAMP PRIMARY KEY, 
    hour int not null, 
    day int not null, 
    week int not null, 
    month int not null, 
    year int not null, 
    weekday varchar not null)"""
)

# INSERT RECORDS

songplay_table_insert = (
    """INSERT INTO songplays (
    start_time, user_id,level,song_id, artist_id, session_id, location, user_agent) 
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (songplay_id) DO NOTHING"""
)

user_table_insert = (
    """INSERT INTO users 
    (user_id, first_name, last_name, gender, level) 
    VALUES 
    (%s, %s, %s, %s, %s) ON CONFLICT(user_id) DO UPDATE SET level = excluded.level"""
)

artist_table_insert = (
    """INSERT INTO artists 
    (artist_id, name, location, latitude, longitude) 
    VALUES 
    (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING"""
)

song_table_insert = (
    """INSERT INTO songs 
    (song_id, title, artist_id, year, duration) 
    VALUES 
    (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING"""
)

time_table_insert = (
    """INSERT INTO time (start_time, hour, day, week, month, year, weekday) 
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING"""
)

# FIND SONGS

song_select = (
    """select s.song_id, a.artist_id 
    from songs s inner join artists a on s.artist_id = a.artist_id 
    where s.title = %s and a.name = %s and s.duration = %s"""
)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

