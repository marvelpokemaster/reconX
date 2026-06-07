import psycopg2

def init_db():
    conn = psycopg2.connect(
        database="reconx",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS investigations (
            id SERIAL PRIMARY KEY,
            target VARCHAR(255) NOT NULL,
            status VARCHAR(20) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS dns_records (
            id SERIAL PRIMARY KEY,
            investigation_id INT NOT NULL,
            record_type VARCHAR(20) NOT NULL,
            value TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (investigation_id) REFERENCES investigations(id) ON DELETE CASCADE
        );
        CREATE TABLE IF NOT EXISTS certificates (
            id SERIAL PRIMARY KEY,
            investigation_id INT NOT NULL,
            issuer VARCHAR(255) NOT NULL,
            valid_from TIMESTAMP,
            valid_to TIMESTAMP,
            FOREIGN KEY (investigation_id) REFERENCES investigations(id) ON DELETE CASCADE
        );
        
    """)

    conn.commit()
    cur.close()
    conn.close()

