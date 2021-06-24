import subprocess, time, requests, json

class controller():

    def __init__(self, ScreenID):
        self.screenid = ScreenID

    def whitelist_Add(self,player_name):
        self.user = str(player_name)
        self.CheckUserURL = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{self.user}")
        self.UserJson = json.loads(self.CheckUserURL.text)
        if str(self.UserJson['name']) == self.user:
            subprocess.call(f'screen -S {self.screenid} -p 0 -X stuff "/whitelist add {self.user}^M"', shell=True)
            return True
        else:
            return False

    def whitelist_remove(self,player_name):
        self.user = str(player_name)
        self.CheckUserURL = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{self.user}")
        self.UserJson = json.loads(self.CheckUserURL.text)
        if str(self.UserJson["name"]) == self.user:
            subprocess.call(f'screen -S {self.screenid} -p 0 -X stuff "/whitelist remove {self.user}^M"', shell=True)
            return True
        else:
            return False
    
    def commands(self, command):
        self.Command = command
        subprocess.call(f'screen -S {self.screenid} -p 0 -X stuff "/{self.Command}^M"', shell=True)
        return True
    
    def Start(self):
        subprocess.call(f'screen -S {self.screenid} -p 0 -X stuff "java -Xmx20G -Xms20G -jar server.jar nogui^M"', shell=True)
        return True

    def Stop(self):
        subprocess.call(f'screen -S {self.screenid} -p 0 -X stuff "/stop^M"', shell=True)
        return True
    
