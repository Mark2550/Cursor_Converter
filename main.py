from os import listdir
from os.path import isfile, join
import subprocess


def main():
    # Paths
    cursor_dir = r"C:\Users\Márk\Documents\cursors"
    output_dir = r"C:\Users\Márk\Documents\cursor_new"
     
    defaultFiles = [f for f in listdir(cursor_dir) if isfile(join(cursor_dir, f))]
    script = "x2wincur [input] -o [output]"
    for f in defaultFiles:
        subprocess.run(script.replace("[input]", join(cursor_dir, f)).replace("[output]", output_dir))
        print (f)
    
if __name__ == "__main__":
    main()