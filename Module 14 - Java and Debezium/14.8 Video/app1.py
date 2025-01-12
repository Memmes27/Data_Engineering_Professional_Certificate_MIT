import mysql.connector
from mysql.connector import Error
import time

MYSQL_SETTINGS = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "Egyptiancobra27!",
    "database": "education"
}

def capture_changes():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**MYSQL_SETTINGS)
        cursor = connection.cursor(dictionary=True)
        
        print("Successfully connected to MySQL database")
        
        # Enable binary logging
        cursor.execute("SET SESSION binlog_format = 'ROW';")
        cursor.fetchall()
        
        cursor.execute("FLUSH LOGS;")
        cursor.fetchall()

        # Get the current binary log file and position
        cursor.execute("SHOW BINARY LOGS;")
        log_info = cursor.fetchall()[-1]
        
        if log_info:
            log_file = log_info["Log_name"]
            print(f"Monitoring binary log file: {log_file}")
            
            # Get the current position
            cursor.execute("SHOW BINLOG EVENTS IN %s;", (log_file,))
            events = cursor.fetchall()
            
            if events:
                log_pos = events[-1]["Pos"]
                print(f"Starting position: {log_pos}")
                print("Waiting for database changes... (Press Ctrl+C to exit)")

                # Start listening for changes
                while True:
                    cursor.execute(f"SHOW BINLOG EVENTS IN '{log_file}' FROM {log_pos};")
                    
                    while True:
                        row = cursor.fetchone()
                        if row is None:
                            break
                            
                        event_type = row.get("Event_type")
                        if event_type in ["WRITE_ROWS_EVENT", "UPDATE_ROWS_EVENT", "DELETE_ROWS_EVENT"]:
                            yield {
                                "type": event_type,
                                "data": row,
                            }
                    
                    # Wait a bit before checking again
                    time.sleep(1)

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("\nConnection closed.")

def main():
    try:
        for event in capture_changes():
            print(event)
    except KeyboardInterrupt:
        print("\nStopping binlog monitoring...")

if __name__ == "__main__":
    main()