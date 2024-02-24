from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import math

class Container(BoxLayout):
    lbl = ObjectProperty()
    formula = "0"
    ops = ('+','-','/', '*')
    def add_number(self, instance):
        if(self.formula == '0'):
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label(self.formula)
    
    def add_operation(self, instance):
        instance = instance.text
        # for op in self.ops:
        #    if (op in self.formula):
        #        if (instance != "=" or instance != "C"):
        #            return
        
        if (instance == "sin"):
            self.update_label(f"sin({self.formula})")
            self.formula = str(math.sin(float(self.formula)))

        elif (instance == "cos"):
            self.update_label(f"cos({self.formula})")
            self.formula = str(math.cos(float(self.formula)))

        elif (instance == "tg"):
            self.update_label(f"tan({self.formula})")
            self.formula = str(math.tan(float(self.formula)))

        elif (instance == "ctg"):
            self.update_label(f"ctg({self.formula})")
            self.formula = str(1/(math.tan(float(self.formula))))

        elif (instance == "abs"):
            self.update_label(f"abs({self.formula})")
            self.formula = str(abs(float(self.formula)))

        elif (instance == "factorial"):
            self.update_label(f"({self.formula})!")
            self.formula = str(math.factorial(int(self.formula)))

        elif (instance == "bin"):
            self.update_label(f"bin({self.formula})")            
            self.formula = bin(int(float(self.formula)))[2:]

        elif (instance == "oct"):
            self.update_label(f"oct({self.formula})")
            self.formula = oct(int(float(self.formula)))[2:]

        elif (instance == "hex"):
            self.update_label(f"hex({self.formula})")
            self.formula = hex(int(float(self.formula)))[2:]

        elif (instance == "1/x"):
            self.update_label(f"1 / ({self.formula})")
            self.formula = str(1/(float(self.formula)))
       
        elif (instance == "sqrt(x)"):
            self.update_label(f"sqrt({self.formula})")
            self.formula = str(math.sqrt(float(self.formula)))

        elif (instance == "x^^2"):
            self.update_label(f"({self.formula})^^2")
            self.formula = str((float(self.formula) * float(self.formula)))
            
        elif (instance == "+/-"):
            self.formula = str(-(float(self.formula)))
            self.update_label(self.formula)
        
        elif (instance == "ln(x)"):
            self.update_label(f"ln({self.formula})")
            self.formula = str(math.log(float(self.formula), math.exp(1)))
        
        elif (instance == "C"):
            self.formula = "0"
            self.update_label(self.formula)
        
        elif (instance == "="):
            self.calculate()
        
        else:
            self.formula += str(instance)
            self.update_label(self.formula)
    
    def calculate(self):
        try:
            self.formula = str(eval(self.formula))
            self.update_label(self.formula)
        except:
            self.formula = "0"
            self.update_label("Ошибка!")          

    def update_label(self, formula):
        try:
            self.lbl.text = formula
        except:
            self.formula = '0'
            self.lbl.text = 'Ошибка!'

class CalculatorApp(App):
    def build(self):      
        return Container()

if __name__ == '__main__':
    CalculatorApp().run()