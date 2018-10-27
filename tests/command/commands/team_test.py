"""Test team command parsing."""
from command.commands.team import TeamCommand


help_text = ""


def test_get_command_name():
    """Test team command get_name method."""
    testcommand = TeamCommand()
    assert testcommand.get_name() == "team"


def test_get_help():
    """Test team command get_help method."""
    testcommand = TeamCommand()
    assert testcommand.get_help() == help_text


def test_handle_list():
    """Test team command list parser."""
    testcommand = TeamCommand()
    assert testcommand.handle("team list") == "listing all teams"


def test_handle_view():
    """Test team command view parser."""
    testcommand = TeamCommand()
    assert testcommand.handle("team view b-s") == "viewing b-s"


def test_handle_help():
    """Test team command help parser."""
    testcommand = TeamCommand()
    assert testcommand.handle('team help') == help_text


def test_handle_delete():
    """Test team command delete parser."""
    testcommand = TeamCommand()
    assert testcommand.handle("team delete b-s") == "b-s was deleted"


def test_handle_create():
    """Test team command create parser."""
    testcommand = TeamCommand()
    assert testcommand.handle("team create b-s 'B S'") == "team B S, id b-s"


def test_handle_add():
    """Test team command add parser."""
    testcommand = TeamCommand()
    assert testcommand.handle("team add b-s ID") == "added ID to b-s"


def test_handle_remove():
    """Test team command remove parser."""
    testcommand = TeamCommand()
    assert testcommand.handle("team remove b-s ID") == "removed ID from b-s"
