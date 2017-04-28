get_ipython().magic(u'matplotlib inline')

import psycopg2
import pprint
import pandas as pd
import pandas.io.sql as psql
import matplotlib
import matplotlib.pyplot as plt
import pickle

configuration = { 'dbname': 'bbnews', 
                  'user':'sae_bbnews',
                  'pwd':'saeBBNew5',
                  'host':'bbnews-qt-redshift.ciyg0rvtqu5l.us-west-2.redshift.amazonaws.com',
                  'port':'8194'
                }
def create_conn(*args,**kwargs):

    config = kwargs['config']
    try:
        conn=psycopg2.connect(dbname=config['dbname'], host=config['host'], port=config['port'], user=config['user'], password=config['pwd'])
    except Exception as err:
        print err.code, err
    return conn

conn = create_conn(config=configuration)
cursor = conn.cursor()

query = """SELECT t1.storyidentifier,t1.tickers,t1.storytime as ,t1.storyheadline,t2.bodytext FROM t_bb_news_story_analytics_v2 t1 
INNER JOIN t_bb_story_text_indexed t2 ON t2.storyidentifier = t1.storyidentifier LIMIT 10000000"""

#database_list = ['bb_news_taxonomy_new_companies','bb_news_taxonomy_securities','t_bb_barra_v_exchange_listing','t_inv_univ_constituent_hist',
#                 't_bb_news_story_analytics','t_bb_company_meta_pre2008_dump','t_bb_topic_meta_pre2008_dump','t_bb_news_story_pre2008_dump',
#                 't_bb_story_text_pre2008_dump','t_bb_news_story_analytics_v2','t_bb_news_company_meta','t_bb_news_company_analytics_indexed',
#                 't_bb_news_company_analytics','t_bb_news_safahus_esg_controversies','bb_news_taxonomy_topics','t_bb_news_topic_meta',
#                 't_bb_news_company_meta_storyid_indexed','t_bb_news_story_analytics_indexed'',kv_test','t_bb_story_text_indexed',
#                 't_map_newstkr_barrid','test_table','t_bb_news_story_company_count','sae_temp_japan_stories_lemmon']
#atabase_list = ['t_bb_news_story_analytics_v2']

#query = """SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"""
#query = """SELECT count(*) AS exact_count FROM t_bb_story_text_indexed"""
#df_raw_copper = psql.read_sql(query, conn)
#query = """SELECT t1.storyidentifier,t1.tickers,t1.storytime,t1.storyheadline,t2.bodytext FROM t_bb_news_story_analytics_v2 t1 
#INNER JOIN t_bb_story_text_indexed t2 ON t2.storyidentifier = t1.storyidentifier LIMIT 10000000"""
#df_raw_copper.to_csv("database_joined.csv", sep='|', encoding='utf-8')
#for i in range(167):
    #query="""SELECT storyidentifier,bodytext FROM t_bb_story_text_indexed LIMIT 1000000 OFFSET """+str(1000000*i)
    #df_raw_copper = psql.read_sql(query, conn)
    #df_raw_copper.to_csv("database_"+str(i)+".csv", sep='|', encoding='utf-8')
    #df_raw_copper.to_csv("database_"+str(i)+".csv", sep='|', encoding='utf-8')
    #del df_raw_copper
#print df_raw_copper
