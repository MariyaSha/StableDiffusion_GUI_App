from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField, MDTextFieldMaxLengthText, MDTextFieldHintText
from kivymd.uix.button import MDButton, MDButtonIcon, MDButtonText
from kivy.uix.image import Image
from PIL import Image as PIL_Image

class ImageGenApp(MDScreen):

    def __init__(self, **kwargs):
        super(ImageGenApp, self).__init__(**kwargs)
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        
        self.cols = 1
        self.rows = 7
        self.update_text = "What kind of image would you like to generate?"
        
        # create main window grid
        self.window = MDGridLayout(
            cols = self.cols, 
            rows = self.rows
        )
        # main window grid settings
        self.window.spacing = (5, 20)
        self.window.padding = (20, 20, 20, 20)
        
        # create instructions label
        self.message = MDLabel(
                text = self.update_text,
                halign = "center",
                font_size = "30dp"
                )
        
        # create input field for user prompt
        self.userinput = MDTextField(
                MDTextFieldHintText(
                    text = "customize prompt",
                    theme_text_color = "Custom",
                    text_color_focus="#FFFFFF",
                ),
                MDTextFieldMaxLengthText(max_text_length = 100),
                mode = "outlined",
                theme_line_color = "Custom",
                line_color_focus= "#A1DB00",
        )
        
        # cteate GENERATE button
        self.button = MDButton(
                # icon syle
                MDButtonIcon(
                    icon = "image",
                    theme_icon_color = "Custom",
                    icon_color = "#FFFFFF",
                    pos_hint = {"center_x": 0.42, "center_y": 0.5}
                ),
                # button text style
                MDButtonText(
                    text = "GENERATE",
                    theme_text_color = "Custom",
                    text_color = "#FFFFFF",
                    theme_font_size = "Custom",
                    font_size = 18,
                    pos_hint = {"center_x": 0.5, "center_y": 0.5},
                    bold = True
                ),
                # button style
                style = "filled",
                theme_bg_color = "Custom",
                md_bg_color = "#A1DB00",
                theme_width = "Custom",
                width = 1,
            )
        
        # attach "generate" button callback
        self.button.bind(on_release=self.prompt_callback)

        # place logo
        self.window.add_widget(
            Image(
                source="logo.png",
                size_hint_y = None,
                height = "100dp"
            )
        )
        
        # vertical grid container for main images
        self.grid = MDGridLayout(cols=3)
        self.grid.spacing = (60, 60)
        self.grid.padding = (20, 10, 20, 10)
        self.grid.size_hint_y = None 
        self.grid.height = "200dp"
        
        # main images, initialized
        self.img1 = Image(source="placeholder_image.png")
        self.img2 = Image(source="placeholder_image.png")
        self.img3 = Image(source="placeholder_image.png")
        
        # vertical grid container for "save" buttons
        self.grid2 = MDGridLayout(cols=3)
        self.grid2.spacing = (15, 0)

        # "save" buttons initialized
        self.btn1 = self.create_save_button("save image", "download")
        self.btn2 = self.create_save_button("save image", "download")
        self.btn3 = self.create_save_button("save image", "download")
        
        # bind callback function with correct arguments to buttons
        self.btn1.bind(on_release=self.save_callback)
        self.btn2.bind(on_release=self.save_callback)
        self.btn3.bind(on_release=self.save_callback)
        
        # add main images to grid
        self.grid.add_widget(self.img1)
        self.grid.add_widget(self.img2)
        self.grid.add_widget(self.img3)
        
        # add "save" buttons to grid
        self.grid2.add_widget(self.btn1)
        self.grid2.add_widget(self.btn2)
        self.grid2.add_widget(self.btn3)
        
        # add widgets to window
        self.window.add_widget(self.message)
        self.window.add_widget(self.userinput)
        self.window.add_widget(self.button)
        self.window.add_widget(self.grid)   
        self.window.add_widget(self.grid2)
        
        # add window to app screen
        self.add_widget(self.window)
        
    def save_callback(self, instance):
        print("save button was clicked!")

    def prompt_callback(self, instance):
        print("generate button was clicked!")

    def create_save_button(self, button_text, button_icon):
        """
        a method to create a 'save' button
        
        - input button_text: string containing the button label
        - input button_icon: string containing the MD icon code
        
        - output: an MDButton object
        """
        my_button = MDButton(
            # icon style
            MDButtonIcon(
                icon = button_icon,
                pos_hint = {"center_x": 0.3, "center_y": 0.5},
                theme_icon_color = "Custom",
                icon_color = "#FFFFFF",
            ),
            # button text style
            MDButtonText(
                text = button_text,
                pos_hint = {"center_x": 0.5, "center_y": 0.5},
                theme_text_color = "Custom",
                text_color = "#FFFFFF",
            ),
            # button style
            style = "filled",
            theme_width = "Custom",
            width = 0.3,
            theme_bg_color = "Custom",
            md_bg_color = "#3CA7F8",
        )
        return my_button

class MyApp(MDApp):

    def build(self):
        self.title = "Generative AI Application"
        return ImageGenApp()

if __name__ == '__main__':
    MyApp().run()