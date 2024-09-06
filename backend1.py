import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            database="CovidDB",
            user="postgres",
            host="localhost",
            password="Achu@2003",
            port=5432
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Connection failed: {e}")
        return None

def insertPerson(name, gender, dob, contactno, pincode, email, area, city, state):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                f"""
                INSERT INTO Location (pincode, area, city, state) VALUES ({pincode}, '{area}', '{city}', '{state}')
                ON CONFLICT (pincode) DO NOTHING;
                
                INSERT INTO Person (P_name, P_Gender, P_DOB, P_contactno, P_address, P_email) 
                VALUES ('{name}', '{gender}', '{dob}', {contactno}, {pincode}, '{email}');
                """
            )
            conn.commit()
            cur.close()
            print("Record inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting record: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")

def insertHospital(name, pwd, contactno, htype, pincode, area, city, state, email, vac, quant_rem):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                f"""
                INSERT INTO Location (pincode, area, city, state) VALUES ({pincode}, '{area}', '{city}', '{state}')
                ON CONFLICT (pincode) DO NOTHING;
                
                INSERT INTO Hospital (H_name, H_pwd, H_contactno, H_type, H_address, H_email, H_vac, quant_rem) 
                VALUES ('{name}', '{pwd}', {contactno}, '{htype}', {pincode}, '{email}', '{vac}', {quant_rem});
                """
            )
            conn.commit()
            cur.close()
            print("Hospital record inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting hospital record: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")

def insertInventory(name, contactno, pincode, area, city, state):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                f"""
                INSERT INTO Location (pincode, area, city, state) VALUES ({pincode}, '{area}', '{city}', '{state}')
                ON CONFLICT (pincode) DO NOTHING;

                INSERT INTO Inventory (I_name, I_contactno, I_address) 
                VALUES ('{name}', {contactno}, {pincode});
                """
            )
            conn.commit()
            cur.close()
            print("Inventory record inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting inventory record: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")

def addSupplies(hospital_id, inventory_id, quantity, timestamp):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                f"""
                INSERT INTO Supplies (S_hospital, S_inventory, S_quantity, S_time) 
                VALUES ({hospital_id}, {inventory_id}, {quantity}, '{timestamp}');
                """
            )
            conn.commit()
            cur.close()
            print("Supplies record inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting supplies record: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")

def newVaccination(person_id, hospital_id, date_first, date_second):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                f"""
                INSERT INTO Vaccinates (P, Hosp, Date_first, Date_second) 
                VALUES ({person_id}, {hospital_id}, '{date_first}', '{date_second}');
                """
            )
            conn.commit()
            cur.close()
            print("Vaccination record inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting vaccination record: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")

def insertVaccine(name, company, cost):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                f"""
                INSERT INTO Vaccine (V_name, V_company, V_cost) 
                VALUES ('{name}', '{company}', {cost});
                """
            )
            conn.commit()
            cur.close()
            print("Vaccine record inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting vaccine record: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")

def insert_doctors(d_id,d_dept):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(
                f"""
                INSERT INTO Doctor (D_id, D_dept) 
                VALUES ({d_id}, '{d_dept}');
                """
            )
            conn.commit()
            cur.close()
            print("Doctor record inserted successfully")
        except psycopg2.Error as e:
            print(f"Error inserting doctor record: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")

def update_function(table, attribute_name, new_value, condition):
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(f"UPDATE {table} SET {attribute_name} = '{new_value}' WHERE {condition};")
            conn.commit()
            print(f"{table} updated successfully!")
        except psycopg2.Error as e:
            conn.rollback()
            print("Error updating hospital:", e)
        finally:
            cur.close()
            conn.close()

def delete_function(table, condition):
    conn = connect()
    cur = conn.cursor()
    try:
        # Constructing the DELETE query
        query = f"DELETE FROM {table} WHERE {condition};"
        
        # Executing the query
        cur.execute(query)
        conn.commit()
        print("deleted successfully!")
    
    except psycopg2.Error as e:
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

def select_function(table, columns, condition=None, order_by=None, ascending=True, group_by=None):
    a = []
    conn = connect() 
    cur = conn.cursor()
    try:
        # Constructing the SELECT query
        query = f"SELECT {', '.join(columns)} FROM {table}"
        
        if condition:
            query += f" WHERE {condition}"
        
        if group_by:
            query += f" GROUP BY {group_by}"
        
        if order_by:
            query += f" ORDER BY {order_by}"
            if not ascending:
                query += " DESC"
        
        query += ";"
        
        # Executing the query
        cur.execute(query)
        rows = cur.fetchall()
        
        # Printing the results
        if rows:
            print("Results:")
            for row in rows:
                print(row)
                a.append(row)
        else:
            print("No results found.")
        
    except psycopg2.Error as e:
        print("Error selecting data:", e)
    finally:
        cur.close()
        conn.close()
    return a
        

def getPatients():
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Person;")
            patients = cur.fetchall()
            cur.close()
            return patients
        except psycopg2.Error as e:
            print(f"Error fetching patients: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")
    return []

def getHospitals():
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Hospital;")
            hospitals = cur.fetchall()
            cur.close()
            return hospitals
        except psycopg2.Error as e:
            print(f"Error fetching hospitals: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")
    return []

def getInventory():
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Inventory;")
            inventory = cur.fetchall()
            cur.close()
            return inventory
        except psycopg2.Error as e:
            print(f"Error fetching inventory: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")
    return []

def getSupplies():
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Supplies;")
            supplies = cur.fetchall()
            cur.close()
            return supplies
        except psycopg2.Error as e:
            print(f"Error fetching supplies: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")
    return []

def getVaccination():
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Vaccinates;")
            vaccination = cur.fetchall()
            cur.close()
            return vaccination
        except psycopg2.Error as e:
            print(f"Error fetching vaccination: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")
    return []

def getDoctors():
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Doctor;")
            vaccination = cur.fetchall()
            cur.close()
            return vaccination
        except psycopg2.Error as e:
            print(f"Error fetching vaccination: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database")
    return []


def fetch_person_ids():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT P_id FROM Person")
    person_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return person_ids

def fetch_hospital_ids():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT H_id FROM Hospital")
    hospital_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return hospital_ids

def fetch_inventory_ids():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT I_id FROM Inventory")
    inventory_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return inventory_ids