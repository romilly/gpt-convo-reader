import appdirs
import os

# TODO: Make ABC, MockConfig, and inject Config into GUI so other tests can avoid clobbering user data

DEFAULT_CONFIGFILE_CONTENTS = """
[default directory locations]
zip directory = .
save directory = .
"""
class Config:
    """
    maintain the configuration for the gpt-convo-reade application

    The configuration is persisted in a file.

    In normal use, that file is `gpt-convo-reader/config.ini`
    in the user's config directory.

    Typical user config directories are:
        Mac OS X:               same as user_data_dir:  ~/Library/Application Support/<AppName>
        Unix:                   ~/.config/<AppName>     # or in $XDG_CONFIG_HOME, if defined
        Win *:                  same as user_data_dir

    The default can be overriden.
    That allows tests that read from or write to the directory
    to avoid interacting with the real file as defined by the user,
    """
    def __init__(self, config_directory: str = None):
        self.config_directory = config_directory or appdirs.user_config_dir("gpt-convo-reader")
        self.config_file_path = os.path.join(self.config_directory, "config.ini")

    def ensure_ini_file_exists(self):
        if not os.path.exists(self.config_directory):
            os.makedirs(self.config_directory, exist_ok=True)
            with open(self.config_file_path, 'w') as cfg:
                cfg.write(DEFAULT_CONFIGFILE_CONTENTS)



