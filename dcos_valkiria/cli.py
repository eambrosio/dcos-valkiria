#! /usr/bin/env python
"""
Administer and manage tasks in DCOS cluster nodes.
usage: valkiria [--pem=<path>] [--user=<user>]
                [--option <ssh-opt>=<value>] [--help|-h]
                [--config-file=<path>] [--ips=<ip-or-list>]
                <command> [<args>...]

options:
    --pem=<path>
        The PEM path to connect to node(s).
    --user=<user>
        The SSH user, where the default user [default: root].
    --option <ssh-opt=value>
        The SSH options. For information, enter `man ssh_config` in your terminal.
    --help, -h
        Show command help
    --config-file=<path>
        Path to config file for ssh connection.
    --ips=<ip-iplist>
        List of IP addresses to connect

The most commonly used git commands are:
    info        show valkiria info
    status      show valkiria agent status
    install     install Valkiria agent in agents, masters or any
    uninstall   uninstall Valkiria agent in agents, masters or any
    start       install Valkiria agent in agents, masters or any
    stop        stop Valkiria agent in agents, masters or any
    tasks       list the killable tasks in agents, masters or any
    kill        kill the task with a specific taskId

See 'valkiria <command> help' for more information on a specific command.
"""

from subprocess import call

from docopt import docopt


def main():
    args = parse_args()

    argv = [args['<command>']] + args['<args>']

    if args['<command>'] == 'info':
        print('Administer and manage commands in DCOS cluster nodes.')
    elif args['<command>'] == 'install':
        call_valkiria_module('valkiria_install', argv)
    elif args['<command>'] == 'status':
        call_valkiria_module('valkiria_status', argv)
    elif args['<command>'] == 'uninstall':
        call_valkiria_module('valkiria_uninstall', argv)
    elif args['<command>'] == 'start':
        call_valkiria_module('valkiria_start', argv)
    elif args['<command>'] == 'stop':
        call_valkiria_module('valkiria_stop', argv)
    elif args['<command>'] == 'tasks':
        call_valkiria_module('valkiria_tasks', argv)
    elif args['<command>'] == 'kill':
        call_valkiria_module('valkiria_kill', argv)
    elif args['<command>'] in ['help', None]:
        print(__doc__)
    else:
        exit("%r is not a valkiria command. See 'valkiria help'." % args['<command>'])


def parse_args():
    return docopt(
        __doc__,
        version='valkiria version 1.7.4.4',
        options_first=True)


def call_valkiria_module(module, argv):
    exit(call(['python', module + '.py'] + argv))


if __name__ == '__main__':
    main()
