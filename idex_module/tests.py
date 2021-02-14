from django.test import TestCase

# Create your tests here.
isT = True
n = 0
while isT:
    try:
        n += 1
        print(n)
        if n < 5:
            isT = True
        else:
            isT = False
    except:
        isT = True
