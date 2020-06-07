import os
from voice_input import voice_input
from spell import spell
import time

command_keywords_pair = []


class CommandAndKeywords:
    def __init__(self, command_keywords_pair=command_keywords_pair):
        self.command_keywords_pair = command_keywords_pair
        self.keywords_list = []
        self.command = ''

    def add_new_command(self, command_to_execute, keywords_list, final_phrase):
        self.command_keywords_pair.append(
            [str(command_to_execute), list(keywords_list), str(final_phrase)])

    def show_all_commands(self):
        for i in self.command_keywords_pair:
            command = i[0]
            keywords_list = i[1]
            print(command +  '=' + str(keywords_list))

    def execute_os_command(self, user_input_phrase=None, voice=False):
        if voice:
            user_input_phrase = voice_input()
        for i in self.command_keywords_pair:
            command = i[0]
            keywords_list = i[1]
            final_phrase = i[2]

            for keyword in keywords_list:
                if user_input_phrase and keyword in user_input_phrase:
                    spell(final_phrase)
                    os.system(command)


ob = CommandAndKeywords()
ob.add_new_command('taskmgr.exe', ['task manager', 'system monitor'], final_phrase='Opening Task Manager')
ob.add_new_command('explorer.exe', ['explorer', 'file manager', 'my files'], final_phrase='Starting File Explorer')



if __name__ == '__main__':
    ob1 = CommandAndKeywords()
    ob1.show_all_commands()

    spell("I am ready for the command")
    while 1:
        ob1.execute_os_command(voice=True)
