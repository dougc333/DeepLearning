import json
import yaml
from ruamel.yaml import YAML
import traceback
import pdb
import sys
import os

class FindError():
    """
    takes in misformed filename data.json and outputs line num where error messages is
    split data.json into smaller files
    """
    def __init__(self):
        self.yaml = YAML(typ='safe')
        #filename = '/Users/dc/Desktop/small.json'
        #fixed = '/Users/dc/Desktop/small_fixed.json'

        self.filename = '/Users/dc/Desktop/data.json'
        self.fixed = '/Users/dc/Desktop/data_fixed.json'
        self.line_num = None
        self.line_num = self.findlinenum_error(self.filename,self.fixed)

    def findlinenum_error(self,read_file,write_file):
        with open(read_file, "r") as fh_read:
            try:
                data = self.yaml.load(fh_read)
            except:
                print("-------=----")
                foo = traceback.format_exc()
                lines = foo.split("\n")
                for x,i in enumerate(lines):
                    if('data.json' in i):
                        print(x,i)
                        findline_num = i.split(",")
                        print(findline_num[1])
                        print(findline_num[1].split()[1]) #143
                        #parse out line number and column
                        return findline_num[1].split()[1]
                print("end err")

        with open(write_file,"w") as fh_write:
            try:
                json.dump(data,fh_write)
            except(Exception) as ex:
                print("before second ex.message")
                print("end 2nd")
        fh_read.close()
        fh_write.close()

    def create_json_files(self):
        """
        start with self.findlinenum and use this
        :return:
        """
        if(self.line_num==None):
            print("cant do anything no line_num, None")
            return
        else:
            print("create_json_files:{}".format(self.line_num))
            small_file = open("small.json","w")
            big_file = open("big.json","w")
            with open(self.filename) as fh:
                for i,file_line in enumerate(fh):
                    print(i,file_line)
                    if i < self.line_num:
                        #write to smallfile
                        small_file.write(file_line)
                    else:
                        #write to original data.json
                        big_file.write(file_line)
        small_file.close()
        big_file.close()
        #swap_files(orig_datajson, temp_file)

    def get_newfilename(self,i):
        return str(i)+".json"

    def swap_files(self,first_file,second_file):
        """
        preserves first_file as tmp. Do we need the first file?
        :param first_file:
        :param second_file:
        :return:
        """
        os.rename(tmp,first_file)
        os.rename(first_file,second_file)

if __name__ == "__main__":
   f = FindError()
   f.create_json_files()

