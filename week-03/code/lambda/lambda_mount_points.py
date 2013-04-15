#! /usr/bin/env python
#
# Demonstration of using lambda functions for common UNIX system
# administration tasks
import subprocess

lines = subprocess.check_output(['mount', '-v'])
lines = lines.splitlines()
mount_points = map(lambda line: line.split()[2], lines)
print  mount_points
