import os
import subprocess
import atexit
import signal

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command\
    as StaticfilesRunserverCommand


RUNSERVER_EXTRA_COMMANDS = [
    'gulp watch',
]


class Command(StaticfilesRunserverCommand):

    def inner_run(self, *args, **options):
        self.commands = []
        self.start_commands()
        return super(Command, self).inner_run(*args, **options)

    def start_commands(self):
        for command in RUNSERVER_EXTRA_COMMANDS:
            self.start_command(command)

    def start_command(self, command):
        self.stdout.write('>>> Starting {}'.format(command))
        process = subprocess.Popen(
            [command],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write('>>> {command} gulp process on pid {pid}'.format(command=command, pid=process.pid))

        def kill_process(pid):
            self.stdout.write('>>> Stopping {}'.format(command))
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_process, process.pid)
