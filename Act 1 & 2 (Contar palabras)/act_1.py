%%time
import re
with open("../Python2/assets/es-11663-8_UTF8.txt", encoding = 'utf-8') as f:
    lines=f.readlines()
    
crtrs = {}
comienzo = False

for renglon in lines:
    a = re.search('^\*', renglon)
    if (a != None) and (comienzo == False):
        print(renglon)
        comienzo = True
        a = None
        continue
     
    if (a != None) and (comienzo == True):
        print(renglon)
        break
    
    if comienzo == True :                 
        for ltra in renglon:               
            if ltra not in crtrs:
                crtrs[ltra] = 1
            if ltra in crtrs:
                crtrs[ltra] += 1

for ltra in crtrs: 
    sorted(crtrs)                                    
    print(f'Letra "{ltra}"  frecuencia -> "{crtrs[ltra]}"')
