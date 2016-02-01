freqs = dict(zip(
    ['e', 't', 'a', 'o', 'i',   'n',   's',   'h',   'r',   
     'd', 'l', 'u', 'c', 'm',  'w',   'f',   'y',   'g',   
     'p',   'b',   'v',   'k',   'x',   'j',   'q',   'z'],
    [12.7,   9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.3, 
      4.0, 2.8, 2.8, 2.4, 2.4, 2.2, 2.0, 2.0, 1.9, 1.5, 
      1.0, 0.8, 0.2, 0.2, 0.1, 0.1]
    ))

def scoreByte(b): 
    return freqs(b.lower()]

def scoreStr(string):
    score = 0.0
    for s in string:
        score += scoreByte(s)
    return score / len(string)
