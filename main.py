from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder 
from kivymd.toast import toast
from kivy.utils import platform 

if platform =="android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.WRITE_EXTERNAL_STORAGE,Permission.READ_EXTERNAL_STORAGE])
    from android.storage import primary_external_storage_path
    my_path = primary_external_storage_path()
else:
    my_path = "/"
Builder.load_string('''
<ken>:
    MDScreen:
        MDBoxLayout:
            orientation: 'vertical'
            MDTopAppBar:
                title: "filemanager"
                elevation: 5
                left_action_items: [["menu", lambda x: None]]
            MDBoxLayout:
                orientation: 'vertical'
                MDList:
                    MDCard:
                        adaptive_height: True
                        pos_hint: {'center_x': 0.5,'center_y': 0.5}
                        md_bg_color: "cyan"
                        
                        MDBoxLayout:
                            orientation: 'vertical'
                            TwoLineListItem:
                                text: "open the filemanager"
                                secondary_text: "Open the file manager for android & desktop"
                                icon_left: "folder"
                                md_bg_color: "white"
                                on_release: root.file_manager_open()                                        
''')
class ken(BoxLayout):
    def __init__(self):
        super().__init__()
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
           # previous=True,
        )
    def file_manager_open(self):
        self.file_manager.show(my_path)  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

class runmyapk(MDApp):
    def build(self):
        toast("made by @ wambugu kinyua")
        return ken()
    
runmyapk().run()
