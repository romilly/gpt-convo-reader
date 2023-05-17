import unittest

from hamcrest import assert_that, contains_string
import tempfile
import os
import shutil

from converter.config import Config


class ConfigTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.temp_dir = tempfile.mkdtemp()
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        self.config = Config(os.path.join(self.temp_dir, 'gpt-convo-reader'))

    def tearDown(self) -> None:
        try:
            shutil.rmtree(self.temp_dir)
        except: # I know, I know. But that's as good as it gets, I fear.
            pass

    def test_config_knows_ini_file_location(self):
        self.config = Config() # ensure that this finds the real directory, *not* the directory for testing
        assert_that(self.config.config_file_path, contains_string('gpt-convo-reader'))  # add assertion here
        assert_that(self.config.config_file_path, contains_string('config.ini'))  # add assertion here

    def test_config_creates_ini_file_if_missing(self):
        # uses the Config directory for testing.
        self.assertFalse(os.path.exists(self.temp_dir))
        self.config.ensure_ini_file_exists()
        self.assertTrue(os.path.exists(self.temp_dir))
        self.assertTrue(os.path.exists(
            os.path.join(self.temp_dir, 'gpt-convo-reader','config.ini')))



if __name__ == '__main__':
    unittest.main()
