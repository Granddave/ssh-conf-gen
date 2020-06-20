from .. import ssh_generator


def parse(hosts_file):
    """Parses a hosts file to create a list of ssh hosts.

       Expects a CSV format like: `host, hostname, ssh_port, user`"""

    ssh_hosts = []
    with open(hosts_file) as f:
        for line in f:
            splitted_line = [x.strip() for x in line.split(',')]
            host = ssh_generator.SshHost(splitted_line[0], splitted_line[1])
            if (len(splitted_line) >= 2 and splitted_line[2] != ""):
                host.ssh_port = splitted_line[2]
            if (len(splitted_line) >= 3 and splitted_line[3] != ""):
                host.user = splitted_line[3]
            ssh_hosts.append(host)
    return ssh_hosts
