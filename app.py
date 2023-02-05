from gui import Gui

import os
from pygltflib.utils import gltf2glb


def convert_to_glb(gltf_filename, target_directory):
    gltf2glb(gltf_filename, destination=target_directory, override=True)


def convert(source_directory, target_directory):
    total_count = 0
    success_count = 0

    for filename in os.listdir(source_directory):
        if filename.endswith(".gltf"):
            total_count += 1
            print(f"Found .gltf file: {filename}")
            try:
                convert_to_glb(os.path.join(source_directory, filename), os.path.join(target_directory, filename))
                success_count += 1
                print(f"Successfully converted {filename} to .glb")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

    print(f"Successfully converted {success_count} of {total_count} gltf files")


if __name__ == "__main__":
    def callback(**kwargs):
        source_folder = kwargs["source_folder"]
        target_folder = kwargs["target_folder"]
        convert(source_folder, target_folder)

    gui = Gui(callback)
    gui.run()
