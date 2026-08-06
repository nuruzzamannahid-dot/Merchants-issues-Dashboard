import unittest
import csv
from datetime import datetime
from carrybee_reminder_bot import parse_csv_line, build_reminder_message

class TestReminderBotMessageBuilder(unittest.TestCase):
    def test_build_reminder_message_escapes_html(self):
        issue = {
            'issueTag': '<b>Urgent</b>',
            'merchant': 'A & B Corp',
            'consignmentId': 'CB-123 <script>',
            'details': 'Please "fix" this immediately!',
            'date': '2026-06-29',
            'timestamp': '10:00:00'
        }
        deadline = datetime(2026, 6, 29, 11, 30)
        message = build_reminder_message(issue, deadline, is_urgent=False)

        # Verify that original tags are escaped and not rendered raw
        self.assertNotIn("<b>Urgent</b>", message)
        self.assertIn("&lt;b&gt;Urgent&lt;/b&gt;", message)

        self.assertNotIn("A & B Corp", message)
        self.assertIn("A &amp; B Corp", message)

        self.assertNotIn("CB-123 <script>", message)
        self.assertIn("CB-123 &lt;script&gt;", message)

        self.assertNotIn('Please "fix"', message)
        self.assertIn("Please &quot;fix&quot;", message)


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
