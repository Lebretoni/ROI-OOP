class Calculator:
    
    
    def __init__(self, annualCF, totalCI,output):
        self.annualCF = annualCF
        self.totalCI = totalCI
        self.output = output
        
     
    def calculation(self):
        while True:
            question = input('Hello would you like to find out your ROI today?(type yes if yes)(type quit to quit)')
            if question.lower() == 'quit':
                print('have a nice day')
                break
            if question.lower() == 'yes':
                annualCF = input('please enter your annual cash flow')
                totalCI = input('please enter your total cash invested')
                output = (int(annualCF) / int(totalCI)) * 100;
                percent = '%'
                print(f'your ROI is: {output}{percent}')
            
            if question.lower() != 'yes' and 'quit':
                print('please type yes or quit')
                break
                
         
            
            
calc = Calculator(0,0,0)
calc.calculation()