import re

Chemicals = {
    "H": 1.00794,
    "He": 4.00260,
    "Li": 6.94,
    "Be": 9.01218,
    "B": 10.81,
    "C": 12.011,
    "N": 14.0067,
    "O": 15.999,
    "F": 18.998403,
    "Ne":20.17,
    "Na": 22.98977,
    "Mg": 24.305,
    "Al": 26.98154,
    "Si": 28.085,
    "P": 30.97376,
    "S": 32.066,
    "Cl": 35.453,
    "Ar": 39.94
}

def AllElements(Formula):
    return re.findall("[A-Z][a-z]*[0-9]*", Formula)
def CountElement(Element):
    Count = re.findall("[1-9]{1,3}", Element)
    if len(Count) > 0:
        return int(Count[0])
    else:
        return 1
def GetElement(Element):
    return re.findall("[A-Z][a-z]*", Element)[0]
def CalculateFormula(Formula, roundTo=2):
    Result = 0
    StepOne = AllElements(Formula)
    for i in StepOne:
        Result += (Chemicals[GetElement(i)]*CountElement(i))
    return round(Result, roundTo)
def ElementInfo(Formula):
    StepOne = CalculateFormula(Formula)
    StepTwo = AllElements(Formula)
    for i in StepTwo:
        # Chemicals[GetElement(i)]*CountElement(i)
        print("Element (" + GetElement(i) + "):", str(round(Chemicals[GetElement(i)]*CountElement(i)/StepOne*100, 2)) + "%")

while True:
    Formula = input("Enter chemical formula: ")
    print("Molar mass:", CalculateFormula(Formula))
    ElementInfo(Formula)
