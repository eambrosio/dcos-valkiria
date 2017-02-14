#! /usr/bin/env python
"""
Establish an SSH connection to the master or agent nodes and uninstall Valkiria on them.

usage: valkiria uninstall [options] [-a|--agents] [-m|--masters] [--all] [--ips=<ip-or-list>]

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
    -a, --agents    uninstall Valkiria agent in all agent nodes.
    -m, --masters   uninstall Valkiria agent in all master nodes.
    --all           uninstall Valkiria agent in all nodes.

See 'valkiria uninstall --help' for more information.

"""

import subprocess

from dcos import util
from docopt import docopt

from dcos_valkiria import constants
from dcos_valkiria.utils import set_default_timeout, get_pem_path, get_ips_list, get_ips


def _uninstall(ips, user, option, pem, config_file):
    for ip in get_ips_list(ips):
        option = set_default_timeout(option)
        pem_path = get_pem_path(pem)
        ssh_options = util.get_ssh_options(config_file, option)
        cmd = '''ssh {9}{2}{0}@{1} ' if [ -d {6} ]; then
                if [ -f ./{7} ]; then pkill -F {7}; rm -rf {7};
                fi
                rm -rf {6}; rm ./{8};
                fi
                echo Valkiria was uninstalled successfully ' '''.format(
            user,
            ip,
            ssh_options,
            constants.url_install,
            constants.name,
            constants.previous_path,
            constants.end_path,
            constants.pid,
            constants.log,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _uninstall_agents(user, option, pem, config_file):
    agents = get_ips('agent')
    _uninstall(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _uninstall_masters(user, option, pem, config_file):
    masters = get_ips('master')
    _uninstall(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _uninstall_all_nodes(user, option, pem, config_file):
    nodes = get_ips(None)
    _uninstall(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def main():
    args = docopt(
        __doc__,
        version='valkiria uninstall')

    nodes = args['--ips']
    user = args['--user']
    option = args['--option']
    pem = args['--pem']
    config_file = args['--config-file']

    if nodes:
        return _uninstall(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)
    elif args['--agents']:
        return _uninstall_agents(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--masters']:
        return _uninstall_masters(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--all']:
        return _uninstall_all_nodes(user=user, option=option, pem=pem, config_file=config_file)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
