import os
import subprocess
import atexit
import signal

from django.conf import settings
from django.contrib.staticfiles.management.commands.runserver import Command\
    as StaticfilesRunserverCommand


class Command(StaticfilesRunserverCommand):

    def inner_run(self, *args, **options):
        self.start_watch()
        return super(Command, self).inner_run(*args, **options)

    def start_watch(self):
        self.stdout.write('>>> Starting gulp')
        self.watch_process = subprocess.Popen(
            ['gulp watch'],
            shell=True,
            stdin=subprocess.PIPE,
            stdout=self.stdout,
            stderr=self.stderr,
        )

        self.stdout.write('>>> gulp process on pid {0}'.format(self.watch_process.pid))

        def kill_watch_process(pid):
            self.stdout.write('>>> Closing gulp process')
            os.kill(pid, signal.SIGTERM)

        atexit.register(kill_watch_process, self.watch_process.pid)
