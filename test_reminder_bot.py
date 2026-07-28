import unittest
import csv
from carrybee_reminder_bot import parse_csv_line

from carrybee_reminder_bot import escape_html, build_reminder_message
from datetime import datetime

class TestReminderBotSecurity(unittest.TestCase):
    def test_escape_html(self):
        self.assertEqual(escape_html("Hello <World> & Co."), "Hello &lt;World&gt; &amp; Co.")
        self.assertEqual(escape_html(None), "")
        self.assertEqual(escape_html(123), "123")

    def test_build_reminder_message_escapes_inputs(self):
        issue = {
            'issueTag': 'Urgent <script>',
            'merchant': '<b>Merchant</b>',
            'consignmentId': 'ID & stuff',
            'details': 'Details <br> here',
            'date': '2026-06-29',
            'timestamp': '12:00:00'
        }
        deadline = datetime(2026, 6, 29, 12, 30)
        msg = build_reminder_message(issue, deadline)

        # Verify that HTML characters are escaped inside the dynamic values
        self.assertIn("Urgent &lt;script&gt;", msg)
        self.assertIn("&lt;b&gt;Merchant&lt;/b&gt;", msg)
        self.assertIn("ID &amp; stuff", msg)
        self.assertIn("Details &lt;br&gt; here", msg)

        # Verify that the message contains the expected formatted date/time and static bold text
        self.assertIn("<b>CarryBee Issue Reminder</b>", msg)
        self.assertIn("<code>ID &amp; stuff</code>", msg)

class TestReminderBotCSVParser(unittest.TestCase):
    def test_parse_simple_line(self):
        line = "2026-06-29,9:21:40,F06289AV8CW,Paperfly"
        expected = ["2026-06-29", "9:21:40", "F06289AV8CW", "Paperfly"]
        self.assertEqual(parse_csv_line(line), expected)

    def test_parse_quoted_fields(self):
        line = '2026-06-29,12:41:08,F0627SXWXUE,"Sumaiya, Hair, Tonic"'
        expected = ["2026-06-29", "12:41:08", "F0627SXWXUE", "Sumaiya, Hair, Tonic"]
        self.assertEqual(parse_csv_line(line), expected)

    def test_parse_empty_line(self):
        self.assertEqual(parse_csv_line(""), [])

    def test_parse_quotes_with_embedded_newlines(self):
        # Even though parse_csv_line is deprecated, let's verify it behaves reasonably with single lines
        line = '"Line 1\nLine 2",field2'
        expected = ["Line 1\nLine 2", "field2"]
        self.assertEqual(parse_csv_line(line), expected)

if __name__ == '__main__':
    unittest.main()
