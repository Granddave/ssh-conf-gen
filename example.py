#!/usr/bin/env python3

import argparse

from ssh_conf_gen.ssh_generator import write_ssh_config_file
from ssh_conf_gen.sources import csv, sqlite


def _get_args():
    parser = argparse.ArgumentParser(description="ssh_conf_gen example")

    parser.add_argument("-i",
                        "--input",
                        required=True,
                        help="input file containing host information")

    parser.add_argument("-o",
                        "--output",
                        default="example-config",
                        help="output filepath for ssh config")

    parser.add_argument("-n",
                        "--no-confirm",
                        action="store_true",
                        help="Do not ask for permission if a file already exists at the output path")

    return parser.parse_args()


if __name__ == "__main__":
    args = _get_args()

    if ".sqlite" in args.input:
        hosts = sqlite.get_hosts(args.input)
    else:
        hosts = csv.get_hosts(args.input)

    write_ssh_config_file(hosts, args.output, args.no_confirm)
