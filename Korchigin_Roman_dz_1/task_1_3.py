def transform_string(number:int) ->str:
    if n == 1:
        return (str(number)+" процент");
    elif n%10 == 2 and n!=12:
        return (str(number)+' процента');
    elif n%10 == 3 and n!=13:
        return (str(number)+' процента');
    elif n%10 == 4 and n!=14:
        return (str(number)+' процента');
    else:
        return (str(number)+' процентов');
for n in range(1,101):
    print (transform_string(n))