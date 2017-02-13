#!/usr/bin/env python
import ast
import unittest

from mock import patch

import dcos_valkiria.valkiria


@patch('dcos_valkiria.valkiria.parse_args')
@patch('dcos_valkiria.valkiria.call_valkiria_module')
class TestValkiria(unittest.TestCase):
    def test_main_install(self, mock_call, mock_parse):
        mock_call.return_value = True
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                   '--help': False,
                   '--ips': None,
                   '--option': None,
                   '--pem': None,
                   '--user': 'root',
                   '<args>': ['--agents'],
                   '<command>': 'install'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_install', ['install', '--agents'])

        mock_call.reset_mock()
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                           '--help': False,
                           '--ips': None,
                           '--option': None,
                           '--pem': None,
                           '--user': 'root',
                           '<args>': ['--masters'],
                           '<command>': 'install'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_install', ['install', '--masters'])

        mock_call.reset_mock()
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                                   '--help': False,
                                   '--ips': None,
                                   '--option': None,
                                   '--pem': None,
                                   '--user': 'root',
                                   '<args>': ['--masters','--pem=/path/to/pem'],
                                   '<command>': 'install'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_install', ['install', '--masters', '--pem=/path/to/pem'])

        mock_call.reset_mock()
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                                          '--help': False,
                                          '--ips': None,
                                          '--option': None,
                                          '--pem': None,
                                          '--user': 'root',
                                          '<args>': ['--masters','--ips=1.1.1.1,2.2.2.2'],
                                          '<command>': 'install'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_install', ['install', '--masters', '--ips=1.1.1.1,2.2.2.2'])

    def test_main_uninstall(self, mock_call, mock_parse):
        mock_call.reset_mock()
        mock_call.return_value = True
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                '--help': False,
                '--ips': None,
                '--option': None,
                '--pem': None,
                '--user': 'root',
                '<args>': ['--agents'],
                '<command>': 'uninstall'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_uninstall', ['uninstall', '--agents'])

    def test_main_start(self, mock_call, mock_parse):
        mock_call.reset_mock()
        mock_call.return_value = True
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                '--help': False,
                '--ips': None,
                '--option': None,
                '--pem': None,
                '--user': 'root',
                '<args>': ['--agents'],
                '<command>': 'start'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_start', ['start', '--agents'])

    def test_main_stop(self, mock_call, mock_parse):
            mock_call.reset_mock()
            mock_call.return_value = True
            mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                       '--help': False,
                       '--ips': None,
                       '--option': None,
                       '--pem': None,
                       '--user': 'root',
                       '<args>': ['--agents'],
                       '<command>': 'stop'}""")
            dcos_valkiria.valkiria.main()
            mock_call.assert_called_once_with('valkiria_stop', ['stop', '--agents'])

    def test_main_status(self, mock_call, mock_parse):
        mock_call.reset_mock()
        mock_call.return_value = True
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                '--help': False,
                '--ips': None,
                '--option': None,
                '--pem': None,
                '--user': 'root',
                '<args>': ['--agents'],
                '<command>': 'status'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_status', ['status', '--agents'])

    def test_main_kill(self, mock_call, mock_parse):
        mock_call.reset_mock()
        mock_call.return_value = True
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                '--help': False,
                '--ips': None,
                '--option': None,
                '--pem': None,
                '--user': 'root',
                '<args>': ['--agents'],
                '<command>': 'kill'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_kill', ['kill', '--agents'])

    def test_main_tasks(self, mock_call, mock_parse):
        mock_call.reset_mock()
        mock_call.return_value = True
        mock_parse.return_value = ast.literal_eval("""{'--config-file': None,
                '--help': False,
                '--ips': None,
                '--option': None,
                '--pem': None,
                '--user': 'root',
                '<args>': ['--agents'],
                '<command>': 'tasks'}""")
        dcos_valkiria.valkiria.main()
        mock_call.assert_called_once_with('valkiria_tasks', ['tasks', '--agents'])


if __name__ == "__main__":
    unittest.main()
