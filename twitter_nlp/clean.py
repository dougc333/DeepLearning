import os

class Clean:
    def __init__(self,user_name):
        """
        cleans and verifies the userid directory for min/max
        """
        self.user_name=user_name
        self.path = os.getcwd()
        self.file_list = [ f for f in os.listdir(os.path.join(self.path,self.user_name)) if f.endswith(self.user_name)]
        print(len(self.file_list))
        # get list of ids from file_list
        self.list_ids = [f[0:len(self.file_list[0])-8] for f in self.file_list]
        self.min = sorted(self.list_ids)[0]
        self.max = sorted(self.list_ids)[-1]
        print("clean min:{}, max:{}".format(self.min,self.max))

if __name__ == "__main__":
    c = Clean("dougc333")
    print(c.file_list)
    print(c.list_ids)
