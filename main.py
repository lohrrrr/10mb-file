import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window
import file_tool
import tkinter as tk
from tkinter import filedialog

Window.size = (800, 700)

class FileCompressorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        title_label = Label(text="File Compressor", font_size='24sp', size_hint=(1, 0.1))
        main_layout.add_widget(title_label)

        file_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        self.file_path = TextInput(hint_text="Select file", multiline=False, readonly=True, font_size='18sp')
        file_layout.add_widget(self.file_path)

        select_file_button = Button(text="Browse", size_hint=(None, None), size=(120, 40))
        select_file_button.bind(on_press=self.open_file_chooser)
        file_layout.add_widget(select_file_button)

        main_layout.add_widget(file_layout)

        size_label = Label(text="Output Size (MB):", font_size='18sp', size_hint=(1, 0.1))
        main_layout.add_widget(size_label)

        self.size_input = TextInput(hint_text="Enter target size", multiline=False, input_type='number', font_size='18sp', width=100)
        main_layout.add_widget(self.size_input)

        save_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        self.save_path = TextInput(hint_text="Select save location", multiline=False, readonly=True, font_size='18sp')
        save_layout.add_widget(self.save_path)

        select_save_button = Button(text="Browse", size_hint=(None, None), size=(120, 40))
        select_save_button.bind(on_press=self.open_save_chooser)
        save_layout.add_widget(select_save_button)

        main_layout.add_widget(save_layout)

        compress_button = Button(text="Compress", size_hint=(None, None), size=(150, 50), font_size='18sp', background_color=(0, 0.5, 1, 1))
        compress_button.bind(on_press=self.compress_file)
        main_layout.add_widget(compress_button)

        self.progress_bar = ProgressBar(max=100, value=0, size_hint=(1, 0.1))
        main_layout.add_widget(self.progress_bar)

        return main_layout

    def open_file_chooser(self, instance):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.file_path.text = file_path

    def open_save_chooser(self, instance):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg" if self.file_path.text.endswith(('.jpg', '.jpeg', '.png', '.gif')) else ".mp4")
        self.save_path.text = file_path

    def compress_file(self, instance):
        file_path = self.file_path.text
        if not file_path:
            self.show_popup("Error", "Please select a file.")
            return

        size_out = self.size_input.text
        if not size_out.isdigit():
            self.show_popup("Error", "Please enter a valid output size.")
            return

        size_out = int(size_out)

        save_path = self.save_path.text
        if not save_path:
            self.show_popup("Error", "Please select a save location.")
            return

        self.progress_bar.value = 0
        Clock.schedule_interval(self.update_progress, 1/25)

        if file_path.endswith(('.mp4')):
            current_dir = os.getcwd()
            video_full_path = os.path.join(current_dir, file_path)
            output_file_name = os.path.basename(file_path).split('.')[0] + '(cmprs).mp4'
            save_dir = os.path.dirname(save_path)
            file_tool.compress_video(video_full_path, os.path.join(save_dir, output_file_name), size_out * 1000)
        elif file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            file_tool.image_type(file_path, size_out * 10, save_path)
        else:
            self.show_popup("Error", "Unsupported file type.")

    def update_progress(self, dt):
        if self.progress_bar.value < 100:
            self.progress_bar.value += 5
        else:
            Clock.unschedule(self.update_progress)
            self.show_popup("Success", "Compression completed!")

    def show_popup(self, title, message):
        layout = BoxLayout(orientation='vertical', padding=10)
        label = Label(text=message, size_hint=(1, 0.8))
        close_button = Button(text="Close", size_hint=(1, 0.2))
        layout.add_widget(label)
        layout.add_widget(close_button)

        popup = Popup(title=title, content=layout, size_hint=(0.8, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    FileCompressorApp().run()