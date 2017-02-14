#! /usr/bin/env python
"""
Establish an SSH connection to the master or agent nodes and install Valkiria on them.

usage: valkiria install [options] [-a|--agents] [-m|--masters] [--all] [--ips=<ip-or-list>]

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

Specific install actions:
    -a, --agents    install Valkiria agent in all agent nodes.
    -m, --masters   install Valkiria agent in all master nodes.
    --all           install Valkiria agent in all nodes.

See 'valkiria install --help' for more information.

"""

import subprocess

from dcos import util
from docopt import docopt

from dcos_valkiria import constants
from dcos_valkiria.utils import set_default_timeout, get_pem_path, get_ips_list, get_ips


def _install(ips, user, option, pem, config_file):
    option = set_default_timeout(option)
    pem_path = get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    for ip in get_ips_list(ips):
        cmd = '''ssh {10}{2}{0}@{1} ' if [ ! -d {6} ]; then
                curl -O {3}; tar -xvf {4};
                mkdir -p {6}; cp {5} {6}; rm -rf {7}; rm {4};
                nohup {6}/valkiria a 2> {9} > /dev/null 2>&1 &
                echo $! > {8}
                echo Valkiria was installed successfully
                else
                echo Valkiria is already installed in {1}
                fi ' '''.format(
            user,
            ip,
            ssh_options,
            constants.url_install,
            constants.name,
            constants.previous_path,
            constants.end_path,
            constants.previous_path.split('/')[0],
            constants.pid,
            constants.log,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _install_agents(user, option, pem, config_file):
    agents = get_ips('agent')
    _install(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _install_masters(user, option, pem, config_file):
    masters = get_ips('master')
    _install(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _install_all_nodes(user, option, pem, config_file):
    nodes = get_ips(None)
    _install(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def main():
    args = docopt(
        __doc__,
        version='valkiria install')

    nodes = args['--ips']
    user = args['--user']
    option = args['--option']
    pem = args['--pem']
    config_file = args['--config-file']

    if nodes:
        return _install(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)
    elif args['--agents']:
        return _install_agents(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--masters']:
        return _install_masters(user=user, option=option, pem=pem, config_file=config_file)
    elif args['--all']:
        return _install_all_nodes(user=user, option=option, pem=pem, config_file=config_file)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
