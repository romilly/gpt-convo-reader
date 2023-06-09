#!/usr/bin/env python
# coding: utf-8
import time

import os.path
from configparser import ConfigParser
from guizero import App, ListBox, TextBox, TitleBox, MenuBar, PushButton

from converter import config
from converter.config import Configuration
from converter.convert import convert, convert_all

import re


def replace_spaces_and_remove_special_chars(string):
    # Replace spaces with minus signs
    string = string.replace(" ", "-")

    # Remove special characters
    string = re.sub(r"[^\w-]", "", string)

    return string


class ConversationGUI(App):
    def __init__(self, testing=False):
        super().__init__(title='ChatGPT Conversation Reader', height=800, width=1400)
        if testing:
            self.configuration = Configuration()
        else:
            self.configuration = config.get_configuration()
        self.conversations = {}
        self.selected_conversation = None
        menubar = MenuBar(self,
                          toplevel=["File"],
                          options=[
                              [["Open", self.open_function],
                               ['Load all', self.load_all],
                               ["Save", self.save_function]],
                          ])
        # Create a Box to contain the ListBox and TextBox
        self.conversation_box = TitleBox(self, 'Conversations', width='fill')
        # Create a ListBox to display the conversation titles
        self.conversation_list = ListBox(self.conversation_box, command=self.show_conversation, width = 'fill')
        self.search_box = TitleBox(self.conversation_box,'Search', width='fill')
        self.search_button= PushButton(self.search_box, text='Search', command=self.filter_convos, align='left')
        self.search_field = TextBox(self.search_box, width='fill', align='left')
        # Create a TextBox to display the conversation messages
        self.conversation_text = TextBox(self.conversation_box, multiline=True, scrollbar=True, width= 'fill', height='fill')

    def filter_convos(self):
        self.conversation_list.clear()
        wanted = self.search_field.value.strip()
        if len(wanted) == 0:
            self.show_full_convo_list()
            return
        for title in self.conversations:
            for message in self.conversations[title].messages:
                if wanted in message.text():
                    self.conversation_list.append(title)
                    break

    def show_conversation(self):
        # Get the selected conversation from the ListBox
        title = self.conversation_list.value
        # Get the conversation object from the dictionary
        self.selected_conversation = self.conversations[title]
        # Clear the TextBox
        self.conversation_text.clear()
        # Add the messages to the TextBox
        for message in self.selected_conversation.messages:
            self.conversation_text.append(str(message))
            self.conversation_text.append('\n')

    def open_function(self):
        file_name = self.select_file(filetypes=[['zip files', '*.zip']],
                                     folder=self.configuration.zip_directory)
        if len(file_name) > 0:
            self.conversations = convert(file_name)
            self.sort_conversations()
            # Add the conversation titles to the ListBox
            self.show_full_convo_list()

    def load_all(self):
        self.conversations = convert_all(self.configuration.zip_directory, self.configuration.prefix)
        self.sort_conversations()
        self.show_full_convo_list()

    def show_full_convo_list(self):
        for title in self.conversations:
            self.conversation_list.append(title)

    def save_function(self):

        # file_name = self.select_file(filetypes=(), save=True,
        #                              folder=self.configuration.save_directory)
        safe_title = replace_spaces_and_remove_special_chars(self.selected_conversation.title)
        file_name = f'gpt%2F{safe_title}.md'
        file_path = os.path.join(self.configuration.save_directory, file_name)
        with open(file_path, 'w') as mdf:
            mdf.write(f'# {self.selected_conversation.title}\n\n')
            mdf.write(f'{self.selected_conversation.updated()}\n\n')
            for message in self.selected_conversation.messages:
                mdf.write(message.markdown())
                mdf.write('\n\n')

    def sort_conversations(self):
        self.conversations = dict(sorted(self.conversations.items()))


if __name__ == "__main__":
    app = ConversationGUI()
    app.font ="Helvetica"
    app.text_size = 12
    # Show the app
    app.display()