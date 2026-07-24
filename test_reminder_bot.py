import unittest
import os
import sys
from datetime import datetime
from unittest.mock import patch, MagicMock

# Set a mock environment variable for testing when importing/loading the bot code
os.environ["TELEGRAM_BOT_TOKEN"] = "mock_token_for_testing_123456"

# Import bot module
import carrybee_reminder_bot

class TestCarryBeeReminderBot(unittest.TestCase):

    def setUp(self):
        # Ensure the test environment is consistent
        os.environ["TELEGRAM_BOT_TOKEN"] = "mock_token_for_testing_123456"

    def test_bot_token_loaded_from_env(self):
        """Test that BOT_TOKEN is loaded correctly from the environment variable."""
        self.assertEqual(carrybee_reminder_bot.BOT_TOKEN, "mock_token_for_testing_123456")

    def test_calculate_deadline_overnight(self):
        """Test deadline calculation for overnight window (7:00 PM – 11:00 AM)"""
        # Testing date in the middle of overnight: 10:00 PM (22:00) on 2026-06-29
        test_dt = datetime(2026, 6, 29, 22, 0, 0)
        expected_deadline = datetime(2026, 6, 30, 11, 30, 0)
        result = carrybee_reminder_bot.calculate_deadline(test_dt)
        self.assertEqual(result, expected_deadline)

    def test_calculate_deadline_midday(self):
        """Test deadline calculation for 11:00 AM – 1:00 PM window"""
        # Testing date: 12:00 PM (12:00) on 2026-06-29
        test_dt = datetime(2026, 6, 29, 12, 0, 0)
        expected_deadline = datetime(2026, 6, 29, 12, 30, 0)
        result = carrybee_reminder_bot.calculate_deadline(test_dt)
        self.assertEqual(result, expected_deadline)

    def test_get_status(self):
        """Test correct status mapping based on inProcess and solved values"""
        issue_open = {"inProcess": False, "solved": False}
        issue_progress = {"inProcess": True, "solved": False}
        issue_resolved = {"inProcess": False, "solved": True}

        self.assertEqual(carrybee_reminder_bot.get_status(issue_open), "Open")
        self.assertEqual(carrybee_reminder_bot.get_status(issue_progress), "In Progress")
        self.assertEqual(carrybee_reminder_bot.get_status(issue_resolved), "Resolved")

    def test_parse_csv_line(self):
        """Test CSV line parser with quotes and commas"""
        line = '123, "Merchant, LLC", "Delivery delay", "Details, details"'
        parsed = carrybee_reminder_bot.parse_csv_line(line)
        self.assertEqual(parsed, ["123", "Merchant, LLC", "Delivery delay", "Details, details"])

if __name__ == "__main__":
    unittest.main()
