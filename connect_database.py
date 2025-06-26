import mysql.connector

class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._user = 3306
        self._password = "root"
        self._database = "db_students"
        self.con = None
        self.cursor = None

    def connect_db(self):

        self.con= mysql.connector.connect(
            host=self._host,
            port = self._port,
            user=self._user,
            password=self._password,
            database=self._database
            )
        self.cursor = self.con.cursor(dictionary=True)

    def add_info(self,studentId,first_name,last_name,state,city,email_address):
        self.connect_db()
        sql = f"""
        INSERT INTO students_info (studentId, firstName, lastName, state, city, emailAddress) VALUES ({student_id},'{first_name}', '{last_name}', '{state}', '{city}', '{email_address}');
        """
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            raise E
        finally:
            self.con.close()

    def update_info(self,studentId,first_name,last_name,state,city,email_address):
        self.connect_db()
        sql = f"""
        UPDATE students_info SET firstName='{first_name}', lastName='{last_name}', state='{state}', city='{city}', emailAddress='{email_address}' WHERE studentId={studentId};
        """
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            raise E
        finally:
            self.con.close()
            
    def delete_info(self,studentId):
        self.connect_db()
        sql = f"""
        DELETE FROM students_info WHERE studentId={studentId};
        """
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            raise E
        finally:
            self.con.close()

    def search_info(self,student_id=None, first_name=None, last_name=None,state=None,city=None,email_address=None):
        self.connect_db()
        condition = ""
        if student_id:
            condition += f"studentId LIKE '%{student_id}%'" 
        else:
            if first_name:
                if condition:
                    condition += f" AND firstName LIKE '%{first_name}%'"
                else:
                    condition += f"firstName LIKE '%{first_name}%'"
            if last_name:
                if condition:
                    condition += f" AND lastName LIKE '%{last_name}%'"
                else:
                    condition += f"lastName LIKE '%{last_name}%'"
            if state:
                if condition:
                    condition += f" AND state LIKE '%{state}%'"
                else:
                    condition += f"state LIKE '%{state}%'"
            if city:
                if condition:
                    condition += f" AND city LIKE '%{city}%'"
                else:
                    condition += f"city LIKE '%{city}%'"
            if email_address:
                if condition:
                    condition += f" AND emailAddress LIKE '%{email_address}%'"
                else:
                    condition += f"emailAddress LIKE '%{email_address}%'"
        if condition:
            sql = f"""
            SELECT * FROM students_info WHERE {condition};
            """
        else:
            sql = f"""
            SELECT * FROM students_info;
            """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as E:
            return E
        finally:
            self.con.close()
    def get_all_states(self):
        self.connect_db()
        sql = f"""
        SELECT state FROM students_info GROUP BY state;
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
            
    def get_all_cities(self):
        self.connect_db()
        sql = f"""
        SELECT city FROM students_info GROUP BY city;
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
            
        
   