#!/usr/bin/env python3

from ssh_conf_gen.ssh_generator import write_ssh_config_file
from ssh_conf_gen.sources import csv, sqlite

if __name__ == "__main__":
    output_file = "example-config"

    #hosts = csv.parse("hosts.txt")
    hosts = sqlite.get_hosts("hosts.sqlite")

    write_ssh_config_file(hosts, output_file)
