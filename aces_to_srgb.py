import os
import re


def aces_to_srgb(folder):
    try:
        # Test if folder
        if not os.path.isdir(folder):
            print("Give a folder")
            os.system("pause")
            return
        input_file = None
        range_0 = None
        range_1 = None
        # Retrieve the sequence and the range of frames
        for child_name in os.listdir(folder):
            path = os.path.join(folder, child_name)
            match = re.match(r"^(.+[\\\/][\w\.]*\.)([0-9]{4})\.exr$", path)
            if not match:
                break
            if input_file is None:
                input_file = (match.group(1) + "####.exr").replace("\\", "/")
            frame = int(match.group(2))
            if range_0 is None or range_0 > frame: range_0 = frame
            if range_1 is None or range_1 < frame: range_1 = frame
        # Test if a sequence has been found
        if input_file is None:
            print("Give a folder with EXR")
            os.system("pause")
            return
        input_dirname, input_basename = os.path.split(input_file)
        output_file = os.path.join(input_dirname, "srgb", input_basename).replace("\\", "/")
        # Create Reader
        reader = app.createReader(input_file)
        colorSpaceOut = reader.getParam("ocioInputSpaceIndex")
        colorSpaceOut.setValue(4)
        # Create Writer
        writer = app.createWriter(output_file)
        # Change Format Type
        formatType = writer.getParam("formatType")
        formatType.setValue(0)
        # Change Output Colorspace to sRGB index 105)
        colorSpaceOut = writer.getParam("ocioOutputSpaceIndex")
        colorSpaceOut.setValue(105)
        # Connect the writer to the reader
        writer.connectInput(0, reader)
        # Render
        app.render(writer, range_0, range_1)
    except Exception as e:
        print(str(e))
        os.system("pause")


aces_to_srgb(folder)
