import unittest
import csv
from carrybee_reminder_bot import parse_csv_line

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


class TestReminderBotSecurity(unittest.TestCase):
    def test_build_reminder_message_escapes_html(self):
        from carrybee_reminder_bot import build_reminder_message
        from datetime import datetime

        issue = {
            "issueTag": "<script>alert('tag')</script>",
            "merchant": "<b>Evil Merchant</b>",
            "consignmentId": "consignment & co",
            "details": "something <br> evil & dangerous",
            "date": "2026-06-29",
            "timestamp": "12:00"
        }
        deadline = datetime(2026, 6, 29, 12, 30)
        message = build_reminder_message(issue, deadline)

        # Ensure raw tags are escaped
        self.assertNotIn("<script>", message)
        self.assertNotIn("<b>Evil Merchant</b>", message)
        self.assertNotIn("something <br>", message)

        # Ensure escaped entities exist
        self.assertIn("&lt;script&gt;alert(&#x27;tag&#x27;)&lt;/script&gt;", message)
        self.assertIn("&lt;b&gt;Evil Merchant&lt;/b&gt;", message)
        self.assertIn("consignment &amp; co", message)
        self.assertIn("something &lt;br&gt; evil &amp; dangerous", message)


if __name__ == '__main__':
    unittest.main()
