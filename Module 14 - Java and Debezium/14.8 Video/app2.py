import mysql.connector
from mysql.connector import Error
import time
from datetime import datetime

MYSQL_SETTINGS = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "Egyptiancobra27!",
    "database": "education"
}

def setup_test_table(connection):
    try:
        cursor = connection.cursor()
        
        # Drop the table if it exists to ensure clean test
        cursor.execute("DROP TABLE IF EXISTS test_binlog")
        
        # Create a test table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_binlog (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Insert test records
        cursor.execute("INSERT INTO test_binlog (message) VALUES ('Test message 1')")
        cursor.execute("INSERT INTO test_binlog (message) VALUES ('Test message 2')")
        
        # Update a record
        cursor.execute("UPDATE test_binlog SET message = 'Updated message' WHERE id = 1")
        
        # Delete a record
        cursor.execute("DELETE FROM test_binlog WHERE id = 2")
        
        connection.commit()
        cursor.close()
        print(f"Test operations completed at {datetime.now()}")
        
    except Error as e:
        print(f"Error in test setup: {e}")

def get_binlog_events(cursor):
    # Get current binary log coordinates
    cursor.execute("SHOW MASTER STATUS")
    current_log = cursor.fetchone()
    
    if current_log:
        log_file = current_log['File']
        log_pos = current_log['Position']
        print(f"Current log file: {log_file}, position: {log_pos}")
        
        # Get detailed event information
        cursor.execute(f"""
            SELECT 
                CONVERT_TZ(FROM_UNIXTIME(timestamp), @@session.time_zone, '+00:00') as timestamp,
                event_type,
                server_id,
                info
            FROM mysql.slow_log
            WHERE start_time >= NOW() - INTERVAL 1 MINUTE
            ORDER BY start_time DESC
        """)
        
        return cursor.fetchall()
    return []

def capture_changes():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**MYSQL_SETTINGS)
        cursor = connection.cursor(dictionary=True)
        
        print(f"Connected to MySQL database at {datetime.now()}")
        
        # Enable necessary logging
        cursor.execute("SET GLOBAL log_output = 'TABLE'")
        cursor.execute("SET GLOBAL slow_query_log = 1")
        cursor.execute("SET SESSION binlog_format = 'ROW'")
        cursor.execute("SET GLOBAL general_log = 1")
        
        # Perform test operations
        print("Performing test operations...")
        setup_test_table(connection)
        
        # Wait a moment for logs to be written
        time.sleep(1)
        
        # Get and process events
        events = get_binlog_events(cursor)
        for event in events:
            print("\nEvent Details:")
            print(f"Timestamp: {event['timestamp']}")
            print(f"Type: {event['event_type']}")
            print(f"Server ID: {event['server_id']}")
            print(f"Info: {event['info']}")
            
        # Also check general log for additional details
        cursor.execute("""
            SELECT * FROM mysql.general_log 
            WHERE event_time >= NOW() - INTERVAL 1 MINUTE
            ORDER BY event_time DESC
        """)
        general_logs = cursor.fetchall()
        
        if general_logs:
            print("\nGeneral Log Entries:")
            for log in general_logs:
                print(f"Time: {log['event_time']}")
                print(f"Command: {log['command_type']}")
                print(f"SQL: {log['argument']}")
                print("---")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("\nConnection closed.")

def main():
    try:
        print("Starting enhanced binlog monitoring...")
        capture_changes()
        print("Monitoring complete!")
    except KeyboardInterrupt:
        print("\nStopping monitoring...")

if __name__ == "__main__":
    main()