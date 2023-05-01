from django import template


register=template.Library()

@register.filter(name='swapping')
def swap(value):
    return value.swapcase()

@register.filter()
def counting(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg):]==arg:
            c+=1
    return c
@register.filter(name='replace')
def remove(value,arg):
    for i in range(len(value)):
       return value.replace(arg,'@!!@#$%^&&&&&&&&&&&&&&&&&&&&*()')
@register.filter()   
def deler(value,arg):
   for i in range(len(value)):
        return value[:arg]+value[arg+1:]
@register.filter()  
def index(value):
    list=[]
    list1=[]
    for k,v in enumerate(value):
        list.append(k)
        list.append(v)
    return list
    


   
#register.filter('deler',deler)
#register.filter('swapping',swap)
#register.filter('counting',counting)
#register.filter('replace',remove)