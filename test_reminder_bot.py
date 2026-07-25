import os
import unittest
from unittest.mock import patch
import carrybee_reminder_bot

class TestReminderBotSecurity(unittest.TestCase):
    def setUp(self):
        # Clear/backup env variables
        self.original_env = os.environ.get("TELEGRAM_BOT_TOKEN")
        if "TELEGRAM_BOT_TOKEN" in os.environ:
            del os.environ["TELEGRAM_BOT_TOKEN"]

        # Ensure any existing .env is temporarily ignored/renamed if exists
        self.env_existed = os.path.exists(".env")
        if self.env_existed:
            os.rename(".env", ".env.bak")

    def tearDown(self):
        # Restore environment variables
        if self.original_env is not None:
            os.environ["TELEGRAM_BOT_TOKEN"] = self.original_env
        elif "TELEGRAM_BOT_TOKEN" in os.environ:
            del os.environ["TELEGRAM_BOT_TOKEN"]

        # Restore .env if it was backed up
        if os.path.exists(".env"):
            os.remove(".env")
        if self.env_existed and os.path.exists(".env.bak"):
            os.rename(".env.bak", ".env")

    def test_load_bot_token_from_env(self):
        """Test that token is loaded from environment variable"""
        os.environ["TELEGRAM_BOT_TOKEN"] = "env_token_123"
        token = carrybee_reminder_bot.load_bot_token()
        self.assertEqual(token, "env_token_123")

    def test_load_bot_token_from_dot_env(self):
        """Test that token is loaded from .env file when env var is not set"""
        with open(".env", "w") as f:
            f.write("TELEGRAM_BOT_TOKEN=dot_env_token_456\n")

        token = carrybee_reminder_bot.load_bot_token()
        self.assertEqual(token, "dot_env_token_456")

    def test_load_bot_token_prefer_env_over_dot_env(self):
        """Test that environment variables take precedence over .env file"""
        os.environ["TELEGRAM_BOT_TOKEN"] = "env_wins"
        with open(".env", "w") as f:
            f.write("TELEGRAM_BOT_TOKEN=dot_env_loses\n")

        token = carrybee_reminder_bot.load_bot_token()
        self.assertEqual(token, "env_wins")

    def test_load_bot_token_missing(self):
        """Test fallback when neither env var nor .env contains the token"""
        token = carrybee_reminder_bot.load_bot_token()
        self.assertIsNone(token)

if __name__ == "__main__":
    unittest.main()
