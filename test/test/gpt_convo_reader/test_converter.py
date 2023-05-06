import unittest

from converter.convert import convert


ZIP_FILE_NAME = "../data/sample.zip"


class ConverterTestCase(unittest.TestCase):
    def test_conversion(self):
        conversations = convert(ZIP_FILE_NAME)
        self.assertEqual(3, len(conversations))
        convo_key = list(conversations.keys())[0]
        convo = conversations[convo_key]
        self.assertEqual('Automating Tasks with Python', convo.title)
        self.assertEqual('2023-04-27T11:26:14', convo.updated())
        messages = convo.messages
        self.assertEqual(5, len(messages))


if __name__ == '__main__':
    unittest.main()
