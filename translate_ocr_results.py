from image_finder import potlines

single_lines_dict = {"BD":['Boss Damage: +30%', 'Boss Damage: +35%', 'Boss Damage: +40%', 'Boss Damage: +45%', 'Boss Damage: +50%'],"IA":['tem Acquisition Rate: +12%','tem Acquisition Rate: +10%'],"CD":['Critical Damage: +3%', 'Critical Damage: +6%'],"ATT":['ATT: +9%','ATT: +6%'],"MATT":['Magic ATT: +6%','Magic ATT: +9%']}
double_lines_dict = {"IED":['Attacks ignore 30% Monster', 'Attacks ignore 35% Monster', 'Attacks ignore 40% Monster', 'Attacks ignore 45% Monster', 'Attacks ignore 50% Monster'],'Drop':['Increases Item Drop Rate by a'],}
single_lines_list = ['Boss Damage: +30%', 'Boss Damage: +35%', 'Boss Damage: +40%', 'Boss Damage: +45%', 'Boss Damage: +50%','tem Acquisition Rate: +12%','tem Acquisition Rate: +10%','Critical Damage: +3%', 'Critical Damage: +6%','ATT: +9%','ATT: +6%','Magic ATT: +6%','Magic ATT: +9%']
double_lines_list = ['Attacks ignore 30% Monster', 'Attacks ignore 35% Monster', 'Attacks ignore 40% Monster', 'Attacks ignore 45% Monster', 'Attacks ignore 50% Monster','Increases Item Drop Rate by a','Increases tem and Meso Drop']
raw_lines = potlines()
def get_lines():
    lines = raw_lines.get_ocr_result()
    return lines
#print(single_lines_dict.values())
def split_lines(lines):
    splitlines = lines.split("\n")
    splitlines.remove(splitlines[-1])
    #print(splitlines)
    return splitlines

def set_lines(splitlines):
    if len(splitlines) ==2:
        line1 = splitlines[0]
        line2 = splitlines[1]
        return line1,line2
    if len(splitlines) ==3:
        if splitlines[0] in double_lines_list:
            line1 = splitlines[0]
            line2 = splitlines[2]
            return line1,line2
        elif splitlines[1] in double_lines_list:
            line1 = splitlines[0]
            line2 = splitlines[1]
            return line1,line2
        
        elif splitlines[0] in single_lines_list:
            line1 = splitlines[0]
            line2 = splitlines[1]
            return line1,line2
        else:
            return "Trash","Trash"

    if len(splitlines) >3:
        if splitlines[0] in double_lines_dict['IED'] and splitlines[3] in double_lines_dict['IED']:
            line1 = splitlines[0]
            line2 = splitlines[3]
            return line1,line2
        else:
            return "Trash","Trash"

def process_lines():
    splitlines = split_lines(get_lines())
    potential_lines = set_lines(splitlines)
    return potential_lines

#print(process_lines())
#print(process_lines())

