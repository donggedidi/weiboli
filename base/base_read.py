import yaml
class BaseRead:
    def base_get(self,filename):
        filedir="./data/"+filename
        with open(filedir,"r")as f:
            data=yaml.load(f,Loader=yaml.FullLoader)
            return data

    def base_read(self,filename,key):

        datas=self.base_get(filename)[key]
        arr=[]
        for data in datas.values():
            arr.append((data["account"],data["password"],data["result"],data["status"]))
        return arr

if __name__ == '__main__':
    print(BaseRead().base_read("login.yaml","test_login"))