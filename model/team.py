"""Represent a data model for a team."""


class Team:
    """Represent a team with related fields and methods."""

    def __init__(self, github_team_name, display_name):
        """Initialize the team.

        Parameters are a valid Github team name and display name.
        """
        self.__github_team_name = github_team_name
        self.__display_name = display_name
        self.__platform = ""
        self.__members = set()

    @staticmethod
    def is_valid(team):
        """Return true if this team has no missing fields."""
        return all(map(lambda f: len(f) > 0, team.__dict__.values()))

    def __eq__(self, other):
        """Return true if this team has the same attributes as the other."""
        return str(self.__dict__) == str(other.__dict__)

    def __ne__(self, other):
        """Return the opposite of what is returned in self.__eq__(other)."""
        return not (self == other)

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

    def add_member(self, slack_id):
        """Add a new member's Slack ID to the team's set of members' IDs."""
        self.__members.add(slack_id)

    def discard_member(self, slack_id):
        """Discard the member of the team with the Slack ID in the argument."""
        self.__members.discard(slack_id)

    def get_members(self):
        """Return the set of all members' Slack IDs."""
        return self.__members

    def is_member(self, slack_id):
        """Identify if any member has the ID specified in the argument."""
        return slack_id in self.__members

    def __str__(self):
        """Print information on the team class."""
        return str(self.__dict__)
