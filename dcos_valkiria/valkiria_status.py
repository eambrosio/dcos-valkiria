#! /usr/bin/env python
"""
Establish an SSH connection to the master or agent nodes to check valkiria agent status.

usage:
    dcos-valkiria status [options] [-a|--agents] [-m|--masters] [--all]

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

Specific uninstall actions:
    -a, --agents    check Valkiria agent status in all agent nodes.
    -m, --masters   check Valkiria agent status in all master nodes.
    --all           check Valkiria agent status in all nodes.

See 'valkiria status --help' for more information.

"""

import subprocess

from dcos import util
from docopt import docopt

from dcos_valkiria import constants
from dcos_valkiria.utils import set_default_timeout, get_pem_path, get_ips_list, get_ips


def _status(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to check valkiria agent status
    """
    option = set_default_timeout(option)
    pem_path = get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    for ip in get_ips_list(ips):
        cmd = '''ssh {5}{2}{0}@{1} 'if [ ! -f ./{4} ]; then
            echo Valkiria is currently stopped in {1}
            else
            echo Valkiria is currently running in {1}
            fi' '''.format(
            user,
            ip,
            ssh_options,
            constants.end_path,
            constants.pid,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _status_agents(user, option, pem, config_file):
    agents = get_ips('agent')
    _status(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _status_masters(user, option, pem, config_file):
    masters = get_ips('master')
    _status(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _status_all_nodes(user, option, pem, config_file):
    nodes = get_ips(None)
    _status(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def main():
    args = docopt(
        __doc__,
        version='valkiria status')

    nodes = args['--ips']
    user = args['--user']
    option = args['--option']
    pem = args['--pem']
    config_file = args['--config-file']

    if nodes:
        return _status(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)
    elif args['--agents']:
        return _status_agents(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--masters']:
        return _status_masters(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--all']:
        return _status_all_nodes(user=user, option=option, pem=pem, config_file=config_file)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
