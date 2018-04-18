from datetime import datetime
import glob2

def merge_files(input_files, output_file):
    with open(output_file, "w") as outfile:
        for input_file in input_files:
            with open(input_file, "r") as infile:
                content = infile.read()
        
                outfile.write(content + '\n')

filename = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + '.txt'

# merge_files(["content1.txt","content2.txt","content3.txt"], filename)
merge_files(glob2.glob('content*.txt'), filename)