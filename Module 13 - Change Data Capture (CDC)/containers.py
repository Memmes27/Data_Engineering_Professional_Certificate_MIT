# docker run --name final_assignment -e MYSQL_ROOT_PASSWORD=Egyptiancobra27! -p 3300:3306 -d mysql
# docker run -p 3300:3306 --name my_sql -e MYSQL_ROOT_PASSWORD=Egyptiancobra27! -d mysql

import os
import sys

def run_mysql_container():
    cmd = "docker run -p 3300:3306 --name my_sql -e MYSQL_ROOT_PASSWORD=Egyptiancobra27! -d mysql"
    result = os.system(cmd)
    
    if result == 0:
        print("MySQL container started successfully")
    else:
        print("Error starting MySQL container")

run_mysql_container()