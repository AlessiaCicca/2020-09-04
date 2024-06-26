from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.movie import Movie


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getNodi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
from movies m 
where m.`rank` is not null"""

        cursor.execute(query)

        for row in cursor:
            result.append(Movie(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod

    def getConnessioni(rank):
            conn = DBConnect.get_connection()

            result = []

            cursor = conn.cursor(dictionary=True)
            query = """select distinct f1 as v1,f2 as v2, count(distinct a1) as peso
    from (select distinct m.id as f1,r.actor_id as a1
    from movies m , roles r 
    where m.`rank` >=%s and m.id =r.movie_id) as t1,
    (select distinct m.id as f2,r.actor_id as a2
    from movies m , roles r 
    where m.`rank` >=%s and m.id =r.movie_id) as t2
    where t1.f1!=t2.f2 and  t1.a1=t2.a2 
    group by f1,f2
    """

            cursor.execute(query, (rank, rank,))

            for row in cursor:
                result.append(Connessione(**row))

            cursor.close()
            conn.close()
            return result
