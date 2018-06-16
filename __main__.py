import Tkinter
import tkFileDialog
import tkMessageBox
import sys
from sortfiles.bin import sort_directory


def run():
    root = Tkinter.Tk()
    root.withdraw()

    if not len(sys.argv) > 1:
        file_path = tkFileDialog.askdirectory()
    else:
        file_path = sys.argv[1]

    try:
        sort_directory(file_path)
        tkMessageBox.showinfo(
            'Success', 'Your directory is now clean: {}'
            .format(str(file_path))
        )
    except Exception as e:
        tkMessageBox.showinfo('Error', str(e))


if __name__ == '__main__':
    run()
