import wolframalpha

def WolfRamAlpha(Data):
    apikey = "3P3LUE-Y86UATQ3E2"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(Data)

    try:
        answer = next(requested.results).text
        return answer
    except:
        print("The value is not answerable")

def Calc(Data):
    Term = str(Data)
    Term = Term.replace("jarvis","")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        print(result)

    except:
        print("The value is not answerable")        