#! /usr/bin/env python
"""
Establish an SSH connection to the master or agent nodes and start the Valkiria agent process on them.

usage:
    dcos-valkiria start [options] [-a|--agents] [-m|--masters] [--all]

Generic options:
    --pem=<path>
        The PEM path to connect to node(s).
    --user=<user>
        The SSH user, where the default user [default: root].
    --option <ssh-opt=value>
        The SSH options. For information, enter `man ssh_config` in your terminal.
    --help, -h
        Show command help.
    --config-file=<path>
        Path to config file for ssh connection.
    --ips=<ip-iplist>
        List of IP addresses to connect

Specific start actions:
    -a, --agents    start Valkiria agent in all agent nodes.
    -m, --masters   start Valkiria agent in all master nodes.
    --all           start Valkiria agent in all nodes.

See 'valkiria start --help' for more information.

"""

import subprocess

from dcos import util
from docopt import docopt

from dcos_valkiria import constants
from dcos_valkiria.utils import set_default_timeout, get_pem_path, get_ips_list, get_ips


def _start(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to start valkiria agent
    """
    option = set_default_timeout(option)
    pem_path = get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    for ip in get_ips_list(ips):
        cmd = '''ssh {6}{2}{0}@{1} 'if [ -f ./{4} ]; then
            echo Valkiria is currently running in {1}
            elif [ ! -f {3} ]; then
                echo Valkiria is currently not installed in {1}
            else
                nohup {3}/valkiria a 2> {5} > /dev/null 2>&1
                echo $! > {4}
            fi' '''.format(
            user,
            ip,
            ssh_options,
            constants.end_path,
            constants.pid,
            constants.log,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _start_agents(user, option, pem, config_file):
    agents = get_ips('agent')
    _start(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _start_masters(user, option, pem, config_file):
    masters = get_ips('master')
    _start(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _start_all_nodes(user, option, pem, config_file):
    nodes = get_ips(None)
    _start(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def main():
    args = docopt(
        __doc__,
        version='valkiria start')

    nodes = args['--ips']
    user = args['--user']
    option = args['--option']
    pem = args['--pem']
    config_file = args['--config-file']

    if nodes:
        return _start(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)
    elif args['--agents']:
        return _start_agents(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--masters']:
        return _start_masters(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--all']:
        return _start_all_nodes(user=user, option=option, pem=pem, config_file=config_file)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
