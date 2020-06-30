import sqlite3

from .. import ssh_generator


def _select_hosts(conn):
    """Select hosts with supplied database connection"""
    cur = conn.cursor()
    cur.execute("SELECT host, hostname, port, user FROM hosts")

    rows = cur.fetchall()
    return rows


def get_hosts(database_path):
    """Get a list with ssh hosts from sqlite3 database with `database_path`"""
    ssh_hosts = []
    with sqlite3.connect(database_path) as conn:
        for row in _select_hosts(conn):
            host = ssh_generator.SshHost(row[0], row[1], row[2], row[3])
            ssh_hosts.append(host)
    return ssh_hosts

