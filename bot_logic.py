from translate_ocr_results import process_lines
from macro_controls import time_to_start , click
import keyboard
import time
#single_lines_dict = {"BD":['Boss Damage: +30%', 'Boss Damage: +35%', 'Boss Damage: +40%', 'Boss Damage: +45%', 'Boss Damage: +50%'],"IA":['Item Acquisition Rate: +12%','Item Acquisition Rate: +10%','tem Acquisition Rate: +12%','tem Acquisition Rate: +10%'],"CD":['Critical Damage: +6%', 'Critical Damage: +3%'],"ATT":['ATT: +9%','ATT: +6%'],"MATT":['Magic ATT: +6%','Magic ATT: +9%']}
single_lines_dict = {"BD":['Boss Damage: +35%', 'Boss Damage: +40%', 'Boss Damage: +45%', 'Boss Damage: +50%'],"IA":['Item Acquisition Rate: +12%','Item Acquisition Rate: +10%','tem Acquisition Rate: +12%','tem Acquisition Rate: +10%'],"CD":['Critical Damage: +6%', 'Critical Damage: +3%'],"ATT":['ATT: +9%','ATT: +6%'],"MATT":['Magic ATT: +6%','Magic ATT: +9%']}
double_lines_dict = {"IED":['Attacks ignore 30% Monster', 'Attacks ignore 35% Monster', 'Attacks ignore 40% Monster', 'Attacks ignore 45% Monster', 'Attacks ignore 50% Monster'],'Drop':['Increases Item Drop Rate by a'],'MnD':['Increases tem and Meso Drop']}


class potential:
    line1=None
    line2=None
    stop_bot = False

    def get_lines(self):
        lines = process_lines()
        self.line1 = lines[0]
        self.line2 = lines[1]

    def check_roll_2L_BD(self):
        if self.line1 in single_lines_dict["BD"] and self.line2 in single_lines_dict['BD']:
            self.stop_bot = True
            return print(self.line1,self.line2,"    PASS")
        else:
            return 

    def check_roll_2L_IA(self):
        if self.line1 in single_lines_dict['IA'] and self.line2 in single_lines_dict['IA']:
            self.stop_bot = True
            return print(self.line1,self.line2,"    PASS")
        else:
            return 

    def check_roll_2L_CD_6(self):
        if self.line1 == single_lines_dict['CD'][0] and self.line2 == single_lines_dict['CD'][0]:
            self.stop_bot = True
            return print(self.line1,self.line2,"    PASS")
        else:
            return

    def check_roll_2L_ATT_18(self):
        if self.line1 in single_lines_dict['ATT'][0] and self.line2 in single_lines_dict['ATT'][0]:
            self.stop_bot = True
            return print(self.line1,self.line2,"    PASS")
        else:
            return 
    
    def check_roll_2L_ATT_15(self):
        if self.line1 in single_lines_dict['ATT'][0] and self.line2 in double_lines_dict['ATT'][1]:
            self.stop_bot = True
            return 'Done'
        elif self.line2 in single_lines_dict['ATT'][0] and self.line1 in double_lines_dict['ATT'][1]:
            self.stop_bot = True
            return 'Done'
        else:
            return "Trash"
    
    def check_roll_BD_IED(self):
        if self.line1 in single_lines_dict['BD'] and self.line2 in double_lines_dict['IED']:
            self.stop_bot = True
            return 'Done'
        elif self.line2 in single_lines_dict['BD'] and self.line1 in double_lines_dict['IED']:
            self.stop_bot = True
            return 'Done'
        else:
            return "Trash"

    def check_roll_1L_IA(self):
        if self.line1 in single_lines_dict['IA'] or self.line2 in single_lines_dict['IA']:
            self.stop_bot = True
            return print(self.line1,self.line2,"    PASS")
        else:
            return 
    
    def check_roll_IA_DR(self):
        if self.line1 in single_lines_dict['IA'][2] and self.line2 in double_lines_dict['Drop']:
            self.stop_bot=True
            return print(self.line1,self.line2,"    PASS")
        elif self.line2 in single_lines_dict['IA'] and self.line1 in double_lines_dict['Drop']:
            self.stop_bot = True
            return print(self.line1,self.line2,"    PASS")

        else:
            return



    def startbot(self):
        time_to_start()
        while self.stop_bot== False and keyboard.is_pressed('q')==False:
            click()
            time.sleep(1)
            self.get_lines()
            self.check_roll_2L_IA()
            #self.check_roll_IA_DR()
            #self.check_roll_2L_ATT_18()
            #self.check_roll_2L_BD()
            #self.check_roll_2L_CD_6()
            #self.check_roll_1L_IA()
            if self.stop_bot == False:
                print(self.line1,self.line2,"    REJECT")
                time.sleep(1)
            else:
                time.sleep(1)
                return








pot = potential()
pot.startbot()
