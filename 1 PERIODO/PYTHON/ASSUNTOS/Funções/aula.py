def epar(x):
    return(x%2==0)

print(epar(2))

def par_ou_ímpar(x):
    if epar(x):
        return "par"
    else:
        return "ímpar"
