# Taking input for the weights
converting = input('Do you want to convert in kilos(kg) or puonds(lb)? (k/p): ')
def weight_calculating():
    if converting == 'k':
        wheight_pounds = input('Enter the weight in pounds(lb): ')
        pound =  float(wheight_pounds) * 0.45359237
        print(f'The weight in kg is {pound}')
    elif converting == 'p':
        wheight_kilos = input('Enter the weight in kilograms(kg): ')
        kilo = float(wheight_kilos) * 2.20462262
        print(f'The weight in kg is {kilo}')
weight_calculating()