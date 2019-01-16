"""Represent a data model for a team."""


class Team:
    """Represent a team with related fields and methods."""

    def __init__(self, gtid, github_team_name, display_name):
        """
        Initialize the team.

        Parameters are a valid Github team ID, team name and display name.
        """
        self.__gtid = gtid
        self.__github_team_name = github_team_name
        self.__display_name = display_name
        self.__platform = ""
        self.__members = set()

    @staticmethod
    def is_valid(team):
        """
        Return true if this team has no missing required fields.

        Required fields for database to accept:
        - ``__github_team_name``
        - ``__gtid``

        :param team: team to check
        :return: returns true if this team has no missing required fields
        """
        return len(team.get_github_team_name()) > 0 and\
            len(team.get_gtid()) > 0

    def __eq__(self, other):
        """Return true if this team has the same attributes as the other."""
        return str(self.__dict__) == str(other.__dict__)

    def __ne__(self, other):
        """Return the opposite of what is returned in self.__eq__(other)."""
        return not (self == other)

    def get_gtid(self):
        """Return this team's unique Github team ID."""
        return self.__gtid

    def set_gtid(self, gtid):
        """Set this team's unique Github team ID."""
        self.__gtid = gtid

    def get_github_team_name(self):
        """Return this team's unique Github team name."""
        return self.__github_team_name

    def set_display_name(self, display_name):
        """Set this team's display name to the given argument."""
        self.__display_name = display_name

    def get_display_name(self):
        """Return this team's display name."""
        return self.__display_name

    def set_platform(self, platform):
        """Set this team's working platform to the given argument."""
        self.__platform = platform

    def get_platform(self):
        """Return this team's working platform."""
        return self.__platform

    def add_member(self, gid):
        """Add a new member's Github ID to the team's set of members' IDs."""
        self.__members.add(gid)

    def discard_member(self, gid):
        """Discard the member of the team with Github ID in the argument."""
        self.__members.discard(gid)

    def get_members(self):
        """Return the set of all members' Github IDs."""
        return self.__members

    def is_member(self, gid):
        """Identify if any member has the ID specified in the argument."""
        return gid in self.__members

    def __str__(self):
        """Print information on the team class."""
        return str(self.__dict__)
