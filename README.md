# num2wordshindi

Convert number to hindi string

How to Use:
  convert number to currency
  >>> engine = Num2wordshindi(num) # enter the number you want to change
  >>> converted_string = engine.to_words() # to convert in words
  >>> converted_currency = engine.to_currency() # to converrt in indian currency (ruppes, paisa)
  
Eg:
  >>> engine = Num2wordshindi(3265.21)
  >>> words = engine.to_words()
  >>> curency = engine.to_currency()
  >>> print(words)
  तीन हजार दौ सौ पेनसठ दशमलव इक्कीस
  >>> print(currency)
	तीन हजार दौ सौ पेनसठ रुपये, इक्कीस पैसे
  
  make sure you have a hindi font installed in your system
  
  
