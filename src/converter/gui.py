from guizero import App, ListBox, TextBox, Box, TitleBox, MenuBar
from converter.convert import convert, Conversation


class ConversationGUI:
    def __init__(self, conversations: dict[str, Conversation]):
        self.conversations = conversations
        self.selected_conversation = None
        self.app = App(title="Conversations")



        menubar = MenuBar(self.app,
                          toplevel=["File"],
                          options=[
                              [["Save", self.save_function]],
                          ])

        # Create a Box to contain the ListBox and TextBox
        self.conversation_box = TitleBox(self.app, 'Conversations', width='fill')

        # Create a ListBox to display the conversation titles
        self.conversation_list = ListBox(self.conversation_box, command=self.show_conversation, width = 'fill')

        # Add the conversation titles to the ListBox
        for title in self.conversations:
            self.conversation_list.append(title)

        # Create a TextBox to display the conversation messages
        self.conversation_text = TextBox(self.conversation_box, multiline=True, scrollbar=True, width= 'fill', height='fill')


        # Show the app
        self.app.display()

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

    def save_function(self):
        file_name = self.app.select_file(filetypes=[['Markdown Files', '*.md']], save=True)
        with open(file_name, 'w') as mdf:
            mdf.write(f'# {self.selected_conversation.title}\n\n')
            mdf.write(f'{self.selected_conversation.updated()}\n\n')
            for message in self.selected_conversation.messages:
                mdf.write(message.markdown())
                mdf.write('\n\n')




ZIP_FILE_NAME = 'sample.zip'

gui = ConversationGUI(convert(ZIP_FILE_NAME))