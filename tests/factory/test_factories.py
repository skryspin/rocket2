"""Tests for factories."""
import pytest

from factory import make_command_parser, CommandParser, \
    make_github_webhook_handler, GitHubWebhookHandler, \
    make_slack_events_handler, SlackEventsHandler
from unittest import mock
from config import Credentials


@pytest.mark.db
def test_make_command_parser():
    """Test the make_command_parser function."""
    test_config = {
        'testing': True,
        'aws': {
            'users_table': 'users_test',
            'teams_table': 'teams_test',
            'projects_table': 'projects_test'
        }
    }
    parser = make_command_parser(test_config, mock.MagicMock(Credentials))
    assert isinstance(parser, CommandParser)


@pytest.mark.db
@mock.patch('factory.Credentials')
def test_make_github_webhook_handler(mock_creds):
    """Test the make_command_github_webhook_handler function."""
    test_config = {
        'testing': True,
        'aws': {
            'users_table': 'users_test',
            'teams_table': 'teams_test',
            'projects_table': 'projects_test'
        }
    }
    mock_creds.github_webhook_secret = "secret"
    handler = make_github_webhook_handler(test_config,
                                          mock_creds)
    assert isinstance(handler, GitHubWebhookHandler)


@pytest.mark.db
def test_make_slack_events_handler():
    """Test the make_command_slack_events_handler function."""
    test_config = {
        'testing': True,
        'aws': {
            'users_table': 'users_test',
            'teams_table': 'teams_test',
            'projects_table': 'projects_test'
        }
    }
    handler = make_slack_events_handler(test_config,
                                        mock.MagicMock(Credentials))
    assert isinstance(handler, SlackEventsHandler)
