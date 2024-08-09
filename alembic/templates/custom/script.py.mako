<%
import os
import time

def generate_numeric_revision():
    timestamp = int(time.time())
    return str(timestamp)

up_revision = generate_numeric_revision()
%>

revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}
