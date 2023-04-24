while True:
    def transalt(str):
        transaltion = ''
        for leeter in str:
            if leeter.lower() in 'zsdfjkl;':
                transaltion = transaltion + 'x'
                if leeter.isupper():
                    transaltion = transaltion + 'X'
            else:
                transaltion = transaltion + leeter
        return transaltion
    print(transalt(input('enter a prompter to translater: '))) 
