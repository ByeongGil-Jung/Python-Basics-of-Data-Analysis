import cx_Oracle
import Data as d
from exercise_1 import DtoPC as dp

"""
 Created by IntelliJ IDEA.
 Project: source
 ===========================================
 User: ByeongGil Jung
 Date: 2018-07-08
 Time: 오전 1:49
"""


# Connecting DB using Singleton
class Dao(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Dao, cls).__new__(cls, *args, **kwargs)  # 왜 super 이지 ??
        return cls._instance

    def _get_conn(self):
        try:
            conn = cx_Oracle.connect(d.Data.id.value, d.Data.pw.value, d.Data.url.value)
            print("[INFO] Connecting DB succeeded")
            return conn
        except Exception as e:
            print("[ERROR] Connecting DB failed")
            print(e)

    def pc_list(self):
        conn = None
        cur = None
        dtos = list()

        try:
            conn = self._get_conn()
            cur = conn.cursor()

            sql = """SELECT * FROM pc"""

            for row in cur.execute(sql):
                dto = dp.DtoPC(row[0], row[1], row[2], row[3], row[4].rstrip(), row[5])
                dtos.append(dto)

            return dtos
        except Exception as e:
            print("[ERROR] occurring SQL Error in pc")
            print(e)
        finally:
            try:
                if not cur:
                    cur.close()
                if not conn:
                    conn.close()
            except Exception as e:
                print(e)

    def pc_insert(self, model, speed, ram, hd, cd, price):
        conn = None
        cur = None

        try:
            conn = self._get_conn()
            cur = conn.cursor()

            sql = """INSERT INTO pc (model, speed, ram, hd, cd, price) VALUES (:1, :2, :3, :4, :5, :6)"""

            cur.execute(sql, (model, speed, ram, hd, cd, price))
            conn.commit()
        except Exception as e:
            print("[ERROR] occurring SQL Error in pc_insert")
            print(e)
        finally:
            try:
                if not cur:
                    cur.close()
                if not conn:
                    conn.close()
            except Exception as e:
                print(e)

    def pc_delete(self, model):
        conn = None
        cur = None

        try:
            conn = self._get_conn()
            cur = conn.cursor()

            sql = """DELETE FROM pc WHERE model = :1"""

            cur.execute(sql, (model,))
            conn.commit()
        except Exception as e:
            print("[ERROR] occurring SQL Error in pc_delete")
            print(e)
        finally:
            try:
                if not cur:
                    cur.close()
                if not conn:
                    conn.close()
            except Exception as e:
                print(e)
