import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

#Builder.load_file("my.kv")
Window.size= (500,500)
class Calculator(Widget):
    def clear(self):
        self.ids.calc_input.text=''
        self.ids.calc_input.background_color= (1,1,1,1)
    def change(self,x):
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""
        self.ids.calc_input.text += x
    def dot(self,x):
        if "." in self.ids.calc_input.text:
            pass
        else:
            if self.ids.calc_input.text == "0":
                self.ids.calc_input.text = ""
            self.ids.calc_input.text += x
    def sum(self,x):
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""
        self.ids.calc_input.text += x
    def sub(self,x):
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""
        self.ids.calc_input.text += x
    def multiply(self,x):
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""
        self.ids.calc_input.text += x
    def divide(self,x):
        if self.ids.calc_input.text == "0":
            self.ids.calc_input.text = ""
        self.ids.calc_input.text += x
    def changeSign(self):
        if len(self.ids.calc_input.text)>0:
            if "." in self.ids.calc_input.text:
                self.ids.calc_input.text = str(object=float(self.ids.calc_input.text)*(-1))
            else:
                self.ids.calc_input.text = str(int(self.ids.calc_input.text)*(-1))
    def equals(self):
        last = self.ids.calc_input.text
        if "+" in last:
            dob_list = []
            num_list = last.split("+")
            for nums in num_list:
                if "." in nums:
                    nos = nums.split(".")
                    dob0 = (int(nos[0])*len(nos[1])*10+int(nos[1]))/len(nos[1])
                    dob_list.append(dob0)
            
            if dob_list == []:
                ans = 0
                for n in num_list:
                    ans += int(n)
                self.ids.calc_input.text = str(ans)
            else:
                ans = 0.0
                for n in num_list:
                    ans += float(n)
                self.ids.calc_input.text = str(ans)
        elif "*" in last:
            dob_list = []
            num_list = last.split("*")
            for nums in num_list:
                if "." in nums:
                    nos = nums.split(".")
                    dob0 = (int(nos[0])*len(nos[1])*10+int(nos[1]))/len(nos[1])
                    dob_list.append(dob0)
            if dob_list == []:
                ans = int(num_list[0])
                for n in num_list:
                    if n != num_list[0]:
                        ans *= int(n)
                self.ids.calc_input.text = str(ans)
            else:
                ans = float(num_list[0])
                for n in num_list:
                    if n != num_list[0]:
                        ans *= float(n)
                self.ids.calc_input.text = str(ans)
        elif "/" in last:
            dob_list = []
            num_list = last.split("/")
            for nums in num_list:
                if "." in nums:
                    nos = nums.split(".")
                    dob0 = (int(nos[0])*len(nos[1])*10+int(nos[1]))/len(nos[1])
                    dob_list.append(dob0)
            if dob_list == []:
                ans = int(num_list[0])
                for n in num_list:
                    if n != num_list[0]:
                        ans /= int(n)
                self.ids.calc_input.text = str(ans)
            else:
                ans = float(num_list[0])
                for n in num_list:
                    if n != num_list[0]:
                        ans /= float(n)
                self.ids.calc_input.text = str(ans)
        elif "-" in last:
            dob_list = []
            num_list = last.split("-")
            if num_list[0] == '':
                    num_list.pop(0)
                    if "." in num_list[0]:
                        num_list[0] = str(float(num_list[0]) * (-1))
                    elif "." not in num_list[0]:
                        num_list[0] = str(int(num_list[0]) * (-1))
            for nums in num_list:
                if "." in nums:
                    nos = nums.split(".")
                    dob0 = (int(nos[0])*len(nos[1])*10+int(nos[1]))/len(nos[1])
                    dob_list.append(dob0)
            if dob_list == []:
                ans = int(num_list[0])
                for n in num_list:
                    if n != num_list[0]:
                        ans -= int(n)
                self.ids.calc_input.text = str(ans)
            else:
                ans = float(num_list[0])
                for n in num_list:
                    if n != num_list[0]:
                        ans -= float(n)
                self.ids.calc_input.text = str(ans)
class MyApp(App):
    def build(self):
        Window.clearcolor=(0.9,0.4,0.7,1)
        return Calculator()
        
if __name__ == '__main__':
    MyApp().run()
 