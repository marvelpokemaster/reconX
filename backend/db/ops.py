import psycopg2

def create_investigation(target):
    if not target:
        return {"error":"target is required"}, 404 #doesnt exist not bad
    conn = psycopg2.connect(
        database="reconx",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO investigations (target, status)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (target, "pending")
    )
    investigation_id=cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return{'id':investigation_id,
    'target': target,
    'status':"pending"    },201 #created success

def get_investigation(id):
    conn = psycopg2.connect(
        database="reconx",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id,target,status FROM investigations WHERE ID = %s
        """,
        (id,)
    )
    row=cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return {"error":"investigation not found"}, 400
    investigation_id,target,status=row
    
    return {
        "id": investigation_id,
        "target": target,
        'status':status
    }
