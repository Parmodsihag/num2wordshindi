
'''
This module convert number to indian rupees in hindi
step 1:
    >>> #start engine and give number as argument
    >>> e = Num2Word_HI(num)
    
step 2:
    >>> # converting to currency hindi
    >>> result = e.to_currency()

In 1 step:
    >>> result = Num2Word_HI(num).to_currency()

Change to Normal Str:
    >>> result = Num2Word_HI(num).to_words()

'''


class Num2wordshindi:
    low_num_dict = {'1':'एक','2':'दौ','3':'तीन','4':'चार','5':'पाँच',
    '6':'छः','7':'सात','8':'आठ','9':'नौ', '0':'शून्य'
    }
    mid_num_dict = {'10':'दस', '11': 'ग्यारह', '12': 'बारह', '13': 'तेरह', '14':'चौदह', '15': 'पंद्रह', '16': 'सोलह', '17': 'सत्रह', '18': 'अठारह', '19': 'उन्नीस',
    '20': 'बीस', '21': 'इक्कीस', '22': 'बाईस', '23': 'तेईस', '24': 'चौबीस', '25': 'पच्चीस', '26': 'छब्बीस', '27': 'सत्ताईस', '28': 'अट्ठाईस', '29': 'उनतीस',
    '30': 'तीस', '31': 'इकतीस', '32': 'बत्तीस', '33': 'तैंतीस', '34': 'चौंतीस', '35': 'पैंतीस', '36': 'छतीस', '37': 'सैंतीस', '38': 'अड़तीस', '39': 'उनतालीस',
    '40': 'चालीस', '41': 'इकतालीस', '42': 'बयालीस', '43': 'तैंतालीस', '44': 'चवालीस', '45': 'पैंतालीस', '46': 'छियालीस', '47': 'सैंतालीस', '48': 'अड़तालीस', '49': 'उड़ंचास',
    '50': 'पचास', '51': 'इक्यावन', '52': 'बावन', '53': 'तिरेपन', '54': 'चौवन', '55': 'पचपन', '56': 'छप्पन', '57': 'सत्तावन', '58': 'अट्ठावन', '59': 'उनसठ',
    '60': 'साठ', '61': 'इकसठ', '62': 'बासठ', '63': 'तिरेसठ', '64': 'चौसठ', '65': 'पैंसठ', '66': 'छियासठ', '67': 'सड़सठ', '68': 'अड़सठ', '69': 'उनहत्तर',
    '70': 'सत्तर', '71': 'इकहत्तर', '72': 'बहत्तर', '73': 'तिहत्तर', '74': 'चौहत्तर', '75': 'पिचहत्तर', '76': 'छिहत्तर', '77': 'सतत्तर', '78': 'अठहत्तर', '79': 'उनासी',
    '80': 'अस्सी', '81': 'इक्यासी', '82': 'बियासी', '83': 'तिरासी', '84': 'चौरासी', '85': 'पिचासी', '86': 'छियासी', '87': 'सत्तासी', '88': 'अट्ठासी', '89': 'नवासी',
    '90': 'नब्बे', '91': 'इक्यानवे', '92': 'बानवे', '93': 'तिरानवे', '94': 'चौरानवे', '95': 'पिचानवे', '96': 'छियानवे', '97': 'सत्तानवे', '98': 'अट्ठानवे', '99': 'निन्यानवे',
    '100': 'सौ' , '00': ' '
    }
    
    def __init__(self, number):
        self.nummber_to_change = number
        
    def change_to_lst(self):
        my_lst = str(self.nummber_to_change).split('.')
        return my_lst

    def lst1str(self, lst):
        if lst == '0':
            return ''
        else:
            return self.low_num_dict.get(lst)
    
    def lst2str(self, lst):
        
        if lst == '00':
            return ''
        
        elif lst[0] == '0':
            return self.low_num_dict.get(lst[1])
        
        else:
            return self.mid_num_dict.get(lst)

    def lst3str(self, lst):
        if lst == '000':
            return ''
        
        elif lst[0] == '0':
            return self.lst2str(lst[1:])

        else:
            return f'{self.lst1str(lst[0])} सौ {self.lst2str(lst[1:])}'

    def lst4str(self, lst):
        if lst == '0000':
            return ''
        elif lst[0] == '0':
            return self.lst3str(lst[1:])
        else:
            return f'{self.lst1str(lst[0])} हजार {self.lst3str(lst[1:])}'

    def lst5str(self, lst):
        if lst == '00000':
            return ''
        elif lst[0] == '0':
            return self.lst4str(lst[1:])
        else:
            return f'{self.lst2str(lst[0])} हजार {self.lst3str(lst[1:])}'
    
    def lst_to_str(self, lst):
        length = len(lst)
        name_list = ['हज़ार', 'हज़ार','लाख','लाख', 'करोड़', 'करोड़', 'अरब', 'अरब', 'खरब', 'खरब', \
        'नील', 'नील', 'पद्म', 'पद्म', 'शंख', 'शंख', 'महाशंख', 'महाशंख', 'महाउपाध', 'महाउपाध', 'जलद', 
        'जलद', 'माध', 'माध', 'परार्ध', 'परार्ध', 'अंत', 'अंत', 'महा अंत', 'महा अंत', 'शिष्ट', 'शिष्ट', 'सिंघर', 'सिंघर', 
        'महा सिंघर', 'महा सिंघर', 'अदंत सिंघर', 'अदंत सिंघर']

        if lst == '0':
            return self.low_num_dict.get(lst)

        elif length == 1:
            return self.lst1str(lst)

        elif length == 2:
            return self.lst2str(lst)

        elif length == 3:
            return self.lst3str(lst)

        elif 42 > length > 3:# 35 23 548
            n = length - 3
            lst2 = lst[:n]
            return_str = ''
            while length > 3:
                if length%2 == 0:
                    if lst2[0] == '0':
                        length -= 1
                        lst2 = lst2[1:]
                        
                    else:
                        return_str = return_str + f'{self.lst1str(lst2[0])} {name_list[length-3]} '
                        length -= 1
                        lst2 = lst2[1:]
                else:
                    if lst2[0:2] == '00':
                        length -= 2
                        lst2 = lst2[2:]

                    else:
                        return_str = return_str + f'{self.lst2str(lst2[0:2])} {name_list[length-4]} '
                        length -= 2
                        lst2 = lst2[2:]
            
            return_str =  return_str + self.lst3str(lst[n:])
    
            return return_str
        else:
            return 'Number Too Long must be <= pow(10, 41)' 
                
    def to_currency(self):
        length = len(self.change_to_lst())
        lst1 = self.change_to_lst()[0]

        if length == 1:
            if lst1 == '1' :
                return 'एक रुपया'
            else:
                return f'{self.lst_to_str(lst1)} रूपये'
            
        elif length == 2:
            lst2 = self.change_to_lst()[1]
            if lst1 == '1' and lst2 == '01':
                return 'एक रुपया, एक पैसा'
            elif lst2 == '01':
                return f'{self.lst_to_str(lst1)} रूपये, एक पैसा'
            elif lst2 == '00':
                return f'{self.lst_to_str(lst1)} रूपये, शून्य पैसे'
            elif len(lst2) == 1:
                lst2 = lst2+'0'
                return f'{self.lst_to_str(lst1)} रूपये, {self.lst_to_str(lst2)} पैसे'
            else: 
                return f'{self.lst_to_str(lst1)} रूपये, {self.lst_to_str(lst2)} पैसे'
        
    def to_words(self):
        length = len(self.change_to_lst())
        lst1 = self.change_to_lst()[0]
        if length == 1:
            return self.lst_to_str(lst1)
        elif length == 2:
            lst2 = self.change_to_lst()[1]
            return f'{self.lst_to_str(lst1)} दशमलव {self.lst_to_str(lst2)}'
        elif length == 3:
            lst2 = self.change_to_lst()[1]
            lst3 = self.change_to_lst()[2]
            return f'{self.lst_to_str(lst1)} दशमलव {self.lst_to_str(lst2)} दशमलव {self.lst_to_str(lst3)}'
        else:
            return None

