import pymongo
import pprint
import json, sys
import pandas as pd
from pymongo import MongoClient


###### PG



import psycopg2 as psycopg2

import pandas as pd

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE

from psycopg2 import sql



###Check connection

def create_connection():

    conn = psycopg2.connect(dbname='test',

                           user='postgres',

                           host='localhost',

                           port= '5432',

                           password='secret')

    print(conn)
    return conn



def create_tables():

    try:
        conn = create_connection();
        cur = conn.cursor()
        query = 'CREATE TABLE profiles (public text, completion_percentage text, gender text, AGE INTEGER, eye_color text, hair_color text, hair_type text, sign_in_zodiac text, region text, last_login text, registration text, body text, I_am_working_in_field text, I_most_enjoy_good_food text, hobbies text, spoken_languages text, pets text, body_type text, my_eyesight text, completed_level_of_education text, favourite_color text, relation_to_smoking text, relation_to_alcohol text, on_pokec_i_am_looking_for text, love_is_for_me text, relation_to_casual_sex text, my_partner_should_be text, marital_status text, children text, relation_to_children text, I_like_movies text, I_like_watching_movie text, I_like_music text, I_mostly_like_listening_to_music text, the_idea_of_good_evening text, I_like_specialties_from_kitchen text, fun text, I_am_going_to_concerts text, my_active_sports text, my_passive_sports text, profession text, I_like_books text, life_style text, music text, cars text, politics text, relationships text, art_culture text, hobbies_interests text, science_technologies text, computers_internet text, education text, sport text, movies text, travelling text, health text, companies_brands text, more text ); CREATE TABLE relations (_from text, _to text);'

        cur.execute(query)

        # close communication with the PostgreSQL database server

        cur.close()

        # commit the changes

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:

            conn.close()



def drop_tables(table_name):

    try:
        conn = create_connection();
        cur = conn.cursor()
        query = "DROP TABLE " + table_name + ';'
        cur.execute(query)

        # close communication with the PostgreSQL database server

        cur.close()

        # commit the changes

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:

        print(error)

    finally:

        if conn is not None:

            conn.close()


def Insert_INTO_profiles_table():

    # use Python's open() function to load the JSON data
    with open('../data/bodies100000.json',errors='ignore') as json_data:
        data = json.load(json_data)
        query_sql = """ insert into profiles
                select * from json_populate_recordset(NULL::profiles, %s) """
        conn = create_connection();
        cur = conn.cursor()

        cur.execute(query_sql, (json.dumps(data),))

        conn.commit()

        print ('\nfinished INSERT INTO execution')
        cur.close()
        conn.close()



def Read_profiles_table():

    select_profiles_query = "SELECT * FROM profiles"
    conn = create_connection();
    cur = conn.cursor()
    cur.execute(select_profiles_query)

    profiles = cur.fetchall()

    print("Table contents after insertion ::")


    print(profiles[99999])

    cur.close()
    conn.close()


if __name__ == "__main__":

    create_tables()

    #drop_tables('profiles')

    #drop_tables('relations')

    #Insert_INTO_profiles_table()

    #Read_profiles_table()