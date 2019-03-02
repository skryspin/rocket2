"""Command parsing for project events"""
import argparse
import logging
import shlex


class ProjectCommand:
    """Represent Project Command Parser."""

    command_name = "project"
    desc = "for dealing with " + command_name + "s"

    def __init__(self, sc):
        """Initialize project command parser with given Slack Client Interface"""
        logging.info("Initializing ProjectCommand instance")
        self.sc = sc
        self.desc = ""
        self.parser = argparse.ArgumentParser(prog="/rocket")
        self.parser.add_argument("project")
        self.subparser = self.init_subparsers()
        self.help = self.get_help()


    def init_subparsers(self):
        """Initialize subparsers for project commands"""
        subparsers = self.parser.add_subparsers(dest="which")

        """Parser for list command."""
        parser_list = subparsers.add_parser("list")
        parser_list.set_defaults(which="list",
                                 help="Outputs the project names.")

        """Parser for view command."""
        parser_view = subparsers.add_parser("view")
        parser_view.set_defaults(which="view",
                                 help="View information about a project.")
        parser_view.add_argument("project_name", type=str, action='store')

        """Parser for delete command."""
        parser_delete = subparsers.add_parser("delete")
        parser_delete.set_defaults(which="delete",
                                   help="(Admin only) Permanently delete "
                                        "specified project.")
        parser_delete.add_argument("project_name", type=str, action='store')


