# from old_fletsb.tools.create_new_storyboard_file import CreateStoryBoardFile
# import os

# p = "Rasool.fletsb"

# if not os.path.isfile(p):
#     CreateStoryBoardFile(file_path=p)

# from old_fletsb.application import Application


# Application(storyboard_file_path=p)

from fletsb.app import Application
file_path = ""


Application(fletsb_file_path=file_path)