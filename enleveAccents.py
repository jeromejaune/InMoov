txt = "t�l�charg�"

def Enleve_Accents(txt):
    ch1 = u"��������������"
    ch2 = u"aaceeeeiiouuuy"
    s = ""
    for c in txt:
        i = ch1.find(c)
        if i>=0:
            s += ch2[i]
        else:
            s += c
    return s