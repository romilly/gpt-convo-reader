# ChatGPT Convo Reader

The reader lets you find, view and format the conversations you've had with ChatGPT in the playground.

It does so by reading the zip file that ChatGPT saves when you ask it to dump your data.

**Please note:** this is an independently developed project, and it has no official connection with ChatGPT or OpenAI.

It will read, list and display the conversations from a ChatGPT dump file:

![Gui](docs/img/gui.png)

You can use it to save a conversation as a nicely formatted Markdown document.

_Here's one I prepared earlier._

![Markdown](docs/img/markdown.png)

## Installation

run `pip install gpt-convo-reader`

## Usage

The application now tries to configure itself using data in a config file.

That file is `gpt-convo-reader/config.ini` in the user's config directory.

Typical user config directories are:
  Mac OS X:               same as user_data_dir:  ~/Library/Application Support/<AppName>
  Unix:                   ~/.config/<AppName>     # or in $XDG_CONFIG_HOME, if defined
  Win *:                  same as user_data_dir


1. Create a directory gpt-convo directory in your config direectoy
2. Create a file `convert.ini` file with the following format:
   ```text
   [default directory locations]
   zip directory = foo
   save directory = bar
   prefix = xhxhazhdsxhnxznsds
   ```
   where `foo` is the relative path to the directory in which OpenAI'a dumped zip file is located, `bar`
   is the default directory into which you will save markdown files, and prefix is set to the prefix that OpenAI adds to the start of the zip files it creates for you.
1. In your chosen directory, run `gpt_reader_gui`
2. From the `File/Open` menu, open the dumped zip file you want to examine. A list of title will be displayed.
5. If you want to load all the files that OpenAI has dumped, select te `File/Load All` option.
3. Select a conversation you want to examine from the list of titles.
4. If you want to export a conversation as a neatly formatted markdown file, you can do so from the `File/Save` menu. It now saves a markdown file to save directory as convo title with prefix gpt%2F.

If you are only interested in converations containing a given string, type the string in the entry field by the search buton and press `Search`.

The list will show only those converastions that contain that string.

If you want to see all the conversations again, delete the search string and press `Search The full list of converations will be displayed.`
## How to contribute

Please raise any issues (bugs or feature requests) on GitHub.

## Contact details

I'm Romilly Cocking: @RAREblog on twitter, @romilly@fosstodon.org





