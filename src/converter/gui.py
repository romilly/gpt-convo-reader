from guizero import App, ListBox, TextBox, TitleBox, MenuBar
from pathlib import Path
from converter.convert import convert


class ConversationGUI(App):
    def __init__(self, default_zip_folder: Path ='.', default_save_folder: Path = '.'):
        super().__init__(title='ChatGPT Conversation Reader', height=800, width=1400)
        self.default_zip_folder = default_zip_folder
        self.default_save_folder = default_save_folder
        self.conversations = {}
        self.selected_conversation = None
        menubar = MenuBar(self,
                          toplevel=["File"],
                          options=[
                              [["Open", self.open_function],["Save", self.save_function]],
                          ])
        # Create a Box to contain the ListBox and TextBox
        self.conversation_box = TitleBox(self, 'Conversations', width='fill')
        # Create a ListBox to display the conversation titles
        self.conversation_list = ListBox(self.conversation_box, command=self.show_conversation, width = 'fill')
        # Create a TextBox to display the conversation messages
        self.conversation_text = TextBox(self.conversation_box, multiline=True, scrollbar=True, width= 'fill', height='fill')

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

    def open_function(self):
        file_name = self.select_file(filetypes=[['zip files', '*.zip']],
                                     folder=self.default_zip_folder)
        if len(file_name) > 0:
            self.conversations = convert(file_name)
            # Add the conversation titles to the ListBox
            for title in self.conversations:
                self.conversation_list.append(title)

    def save_function(self):
        file_name = self.select_file(filetypes=[['Markdown Files', '*.md']], save=True,
                                     folder=self.default_save_folder)
        if len(file_name) > 0:
            with open(file_name, 'w') as mdf:
                mdf.write(f'# {self.selected_conversation.title}\n\n')
                mdf.write(f'{self.selected_conversation.updated()}\n\n')
                for message in self.selected_conversation.messages:
                    mdf.write(message.markdown())
                    mdf.write('\n\n')


if __name__ == "__main__":
    app = ConversationGUI()
    app.font ="Helvetica"
    app.text_size = 12
    # Show the app
    app.display()