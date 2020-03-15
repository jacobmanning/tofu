#!/usr/bin/env python3

"""
Tofu
"""

import logging
import os
import pathlib
import subprocess
import sys

CONFIG = {
  "logging_format_string": "[%(levelname)s] %(message)s",
  "logging_name": "tofu",
  "logging_level": logging.INFO,
  "root_dir": pathlib.Path.home() / pathlib.Path("tofu"),
  "scripts_dir": pathlib.Path("scripts"),
}

def get_scripts_dir():
  """Get the directory where scripts are found."""
  return CONFIG["root_dir"] / CONFIG["scripts_dir"]

def get_full_command(cmd):
  """Get the full path to the command in the scripts dir."""
  return get_scripts_dir() / pathlib.Path(cmd)

def get_valid_commands():
  """Get a list of the valid commands."""
  return [f.name for f in get_scripts_dir().glob('*') if f.is_file()]

def is_valid_command(cmd):
  """Check if a command is valid"""
  return cmd in get_valid_commands()

def main():
  """Run tofu"""
  # Parse command line arguments
  _, command, *arguments = sys.argv

  # Check if passed command is valid
  # A command is valid if it has a script to execute under the scripts directory
  if not is_valid_command(command):
    log.warning(f"Command = {command} is not valid")
    log.warning(f"Valid commands are {get_valid_commands()}")
    sys.exit(1)

  # Run the desired command by forwarding the arguments
  return subprocess.run([get_full_command(command), *arguments])

if __name__ == "__main__":
  # Configure logger
  logging.basicConfig(format=CONFIG["logging_format_string"])
  log = logging.getLogger(CONFIG["logging_name"])
  log.setLevel(CONFIG["logging_level"])
  main()
