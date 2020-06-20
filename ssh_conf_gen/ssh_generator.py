from datetime import datetime
import os


class SshHost:
    def __init__(self, host, hostname, ssh_port=None, user=None):
        self.host = host
        self.hostname = hostname
        self.ssh_port = ssh_port
        self.user = user
        # description?
        # identityfile?
        # tunneling?

    def get_config_str(self):
        """Returns the host block for the ssh config"""
        rows = []
        rows.append(f"Host {self.host}")
        rows.append(f"    HostName {self.hostname}")
        if self.ssh_port is not None:
            rows.append(f"    Port {self.ssh_port}")
        if self.user is not None:
            rows.append(f"    User {self.user}")

        return "\n".join(rows) + "\n"


def _get_file_header():
    """Returns a file header string containing cration date"""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    return f"""# This file was auto generated by ssh_conf_gen
# Creation date: {timestamp}\n"""


def write_ssh_config_file(ssh_hosts, dest_file, confirm=True):
    """Writes ssh hosts to supplied file

    Set `confirm=False` to overwrite any already existing file"""

    if confirm == False and os.path.exists(dest_file):
        answer = input("Overwrite existing file? [y/N] ")
        if not "y" in answer.strip().lower():
            return

    with open(dest_file, "w+") as f:
        file_content = []
        file_content.append(_get_file_header())
        for host in ssh_hosts:
            file_content.append(host.get_config_str())
        file_content.append("# vi:syntax=sshconfig")

        f.write("\n".join(file_content) + "\n")

