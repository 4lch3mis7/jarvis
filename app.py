from applications.command_and_keywords import CommandAndKeywords
from applications.spell import spell

spell('I am ready for the command!')

com1 = CommandAndKeywords()
com1.show_all_commands()

com1.execute_os_command(voice=True)

    
