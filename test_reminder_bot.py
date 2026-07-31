import unittest
import csv
from datetime import datetime
from carrybee_reminder_bot import parse_csv_line, build_reminder_message

class TestReminderBotSecurity(unittest.TestCase):
    def test_build_reminder_message_html_escape(self):
        issue = {
            'issueTag': 'Urgent <script>alert("tag")</script> & more',
            'merchant': 'Merchant <p>Name</p>',
            'consignmentId': 'CON-123 & 456',
            'details': 'Details containing < & > and & chars',
            'date': '2026-06-29',
            'timestamp': '12:00:00'
        }
        deadline = datetime(2026, 6, 29, 12, 30)
        message = build_reminder_message(issue, deadline, is_urgent=True)

        # Verify that raw HTML tags and characters are escaped
        self.assertNotIn('<script>', message)
        self.assertNotIn('<p>', message)
        self.assertNotIn('CON-123 & 456', message)  # should be escaped as &amp;

        self.assertIn('Urgent &lt;script&gt;alert(&quot;tag&quot;)&lt;/script&gt; &amp; more', message)
        self.assertIn('Merchant &lt;p&gt;Name&lt;/p&gt;', message)
        self.assertIn('CON-123 &amp; 456', message)
        self.assertIn('Details containing &lt; &amp; &gt; and &amp; chars', message)

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
