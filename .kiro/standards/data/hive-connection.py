# BDP Hive Connection
# Demonstrates approved pattern for Hive connectivity via JDBC

import jaydebeapi
import getpass
from pandas import DataFrame


# --- Authentication ---
# Credentials via interactive prompt (never hardcode)

password = getpass.getpass(prompt='password')
fnumber = "f5331315"


# --- JDBC Configuration ---

driver = 'com.cloudera.hive.jdbc.HS2Driver'

url = (
    "jdbc:hive2://bdpi.gslb.fnb.co.za:443/default;"
    "ssl=1;"
    "AllowSelfSignedCerts=1;"
    "transportMode=http;"
    "httpPath=gateway/cdp-proxy-api/hive?tez.queue.name=default"
)

hivejar = "/etc/jar/HiveJDBC42.jar"


# --- Connection ---

conn = jaydebeapi.connect(driver, url, [fnumber, password], hivejar)
cursor = conn.cursor()

# Execute queries using cursor
# cursor.execute("SELECT * FROM database.table LIMIT 10")
# results = cursor.fetchall()

# Always close connections
# cursor.close()
# conn.close()
