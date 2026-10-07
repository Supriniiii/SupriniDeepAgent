# Sampling Data from Teradata
# Demonstrates approved pattern for Teradata database access

import sqlalchemy
import getpass
import pandas as pd
import plotly.express as px


# --- Authentication ---
# Credentials via interactive prompt (never hardcode)

password = getpass.getpass(prompt='password')
fnumber = "F1111111"


# --- Query ---

sql = """
    SELECT *
    FROM dev_ext_bdp_monitoring.load_reporting_hive_query
    ORDER BY date_time DESC
    SAMPLE 100;
"""


# --- Connection ---
# Using SQLAlchemy with teradatasql driver and LDAP authentication

eng = sqlalchemy.create_engine(
    f'teradatasql://edw.gslb.fnb.co.za/?user={fnumber}&password={password}&logmech=LDAP&tmode=TERA'
)

results = pd.read_sql_query(sql, eng)
results.head()


# --- Visualization ---

fig = px.line(
    results,
    x=results["date_time_formated"],
    y=results["response_time"]
)
fig.show()
