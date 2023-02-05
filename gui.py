import PySimpleGUI as sg
import os


class Gui:
    def __init__(self, start_callback):
        self.start_callback = start_callback

        layout = [
            [sg.Text('Select the source folder (gltf)'), sg.Input(), sg.FolderBrowse()],
            [sg.Text('Select the target save folder (glb)'), sg.Input(), sg.FolderBrowse()],
            [sg.Stretch(), sg.Button('Start convert'), sg.Stretch()],
            [sg.Output(size=(80, 20), key='_output_')],
            [sg.Button('Clear log'), sg.Button('Exit app')]
        ]

        self.window = sg.Window('GLTF to GLB File Converter', element_justification='l').Layout(layout)

    def run(self):
        while True:
            event, values = self.window.Read()
            if event is None or event == 'Exit app':
                print('Exit app')
                break

            elif event == 'Clear log':
                print('Log cleared')
                self.window.FindElement('_output_').Update('')

            elif event == 'Start convert':
                folder_path = values[0]
                target_path = values[1]

                if not os.path.isdir(folder_path):

                    # folder_path is not a valid folder path
                    print(f"{folder_path} is not a valid folder path")

                if not os.path.isdir(target_path):
                    # target_path is not a valid folder path
                    print(f"{target_path} is not a valid folder path")

                else:
                    # folder_path is a valid folder path
                    self.start_callback(
                        source_folder=values[0],
                        target_folder=values[1],
                    )

        self.window.Close()


if __name__ == '__main__':
    def callback(**kwargs):
        for key, value in kwargs.items():
            print(f"Key: {key} | Value: {value}")


    gui = Gui(callback)
    gui.run()
