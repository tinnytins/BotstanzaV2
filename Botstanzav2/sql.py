import sqlite3 as sql
import jsonpickle   

#init tables
try:
    con = None
    con = sql.connect("./data/botstanza.db")
    cur = con.cursor()
    con.execute("drop table ufo")
    cur.execute("create table ufo(sightingID int,summary text,city text,state text,date_time datetime,shape text,duration text,stats text,report_link text,[text] text, posted datetime,city_latitude text, sity_longitude text)")
    sightings = jsonpickle.decode(open('./data/nuforc_reports.json').read())
    count = 1
    sightings.pop(0)
    for sighting in sightings:

        if sighting.date_time == '':
            date = 'NULL'
        else:
            date = sighting.date_time
        if sighting.posted == '':
            pdate = 'NULL'
        else:
            pdate = sighting.date_time
        if count % 1000 == 0:
            print(count)
        cur.execute("insert into ufo values ({12},'{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')".format(
            sighting.summary.replace("'","''"),sighting.city.replace("'","''"),sighting.state.replace("'","''"),date,sighting.shape.replace("'","''"),sighting.duration.replace("'","''"),sighting.stats.replace("'","''"),sighting.report_link,sighting.text.replace("'","''"),pdate,sighting.city_longitude,sighting.city_latitude,count))
        count += 1
    con.commit()
    cur.close()

except sql.Error as e:
    print("Error {}".format(e.args[0]))
    sys.exit(1)
finally:
    if con:
        con.close()