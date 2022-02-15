# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:06:55 2021

@author: Rémi
"""

grammarTable={
    "PH":-1,
    -1:"PH",
    "PCT":0,
    0:"PCT",
    "NAM":1,
    1:"NAM",
    "VER":2,
    2:"VER",
    "ADV":3,
    3:"ADV",
    "ADJ":4,
    4:"ADJ",
    "AUX":5,
    5:"AUX",
    "PRO":6,
    6:"PRO",
    "ART":7,
    7:"ART",
    "PRE":8,
    8:"PRE",
    "CON":9,
    9:"CON",
    "ONO":10,
    10:"ONO",}
                    #NEXT PCT NAM VER ADV ADJ AUX PRO ART PRE CON ONO   #PREV
grammarTransitionTable=[[-1,  7,  6,  9,  5,  4,  8,  2,  1,  3,  0],   #PCT
                        [-1,  8,  7,  6,  9,  5,  3,  4,  2,  1,  0],   #NAM
                        [-1,  6,  0,  9,  7,  5,  4,  8,  3,  2,  1],   #VER
                        [-1,  6,  5,  4,  7,  3,  8,  2,  9,  1,  0],   #ADV
                        [-1,  9,  8,  7,  6,  5,  4,  2,  3,  1,  0],   #ADJ
                        [-1,  8,  9,  7,  6,  5,  4,  3,  2,  1,  0],   #AUX
                        [-1,  8,  9,  7,  6,  5,  4,  3,  2,  1,  0],   #PRO
                        [-1,  8,  7,  6,  9,  5,  4,  3,  2,  1,  0],   #ART
                        [-1,  8,  7,  6,  5,  4,  3,  9,  2,  1,  0],   #PRE
                        [-1,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0],   #CON
                        [-1,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0]]   #ONO


languages={
    "none":-1,
    -1:"none",
    "fr":0,
    0:"fr",
    "en":1,
    1:"en",
    "sp":2,
    2:"sp",
    "ru":3,
    3:"ru"}


frIndex={
    'a':range(1,12105),
    'b':range(12105,19238),
    'c':range(19238,34927),
    'd':range(34927,46862),
    'e':range(46862,54700),
    'f':range(54700,60590),
    'g':range(60590,65183),
    'h':range(65183,67817),
    'i':range(67817,73955),
    'j':range(73955,75127),
    'k':range(75127,75460),
    'l':range(75460,78756),
    'm':range(78756,86466),
    'n':range(86466,88629),
    'o':range(88629,91179),
    'p':range(91179,103795),
    'q':range(103795,104377),
    'r':range(104377,117201),
    's':range(117201,126653),
    't':range(126653,133412),
    'u':range(133412,133901),
    'v':range(133901,137227),
    'w':range(137227,137327),
    'x':range(137327,137350),
    'y':range(137350,137442),
    'z':range(137442,137702),
    'à':range(137702,137751),
    'â':range(137751,137791),
    'ç':range(137791,137795),
    'è':range(137795,137799),
    'é':range(137799,142651),
    'ê':range(142651,142658),
    'î':range(142658,142664),
    'ô':range(142664,142695)}
frVerbIndex={
    "acheter":0,
    "geler":1,
    "adirer":2,
    "aller":3,
    "tomber":4,
    "becter":5,
    "boumer":6,
    "béer":7,
    "clamecer":8,
    "courbaturer":9,
    "discontinuer":10,
    "dépecer":11,
    "envoyer":12,
    "ficher":13,
    "incomber":14,
    "moufeter":15,
    "moufter":16,
    "rapiécer":17,
    "résulter":18,
    "urger":19,
    "ayer":20,
    "placer":21,
    "jeter":22,
    "peser":23,
    "sevrer":24,
    "neiger":25,
    "oyer":26,
    "célébrer":27,
    "céder":28,
    "ébrécher":29,
    "régler":30,
    "protéger":31,
    "hypothéquer":32,
    "manger":33,
    "parler":34,
    "advenir":35,
    "apparoir":36,
    "asservir":37,
    "avenir":38,
    "avoir":39,
    "bienvenir":40,
    "bénir":41,
    "chaloir":42,
    "choir":43,
    "circonvenir":44,
    "convenir":45,
    "déchoir":46,
    "défaillir":47,
    "départir":48,
    "dépourvoir":49,
    "faillir":50,
    "falloir":51,
    "férir":52,
    "gésir":53,
    "huir":54,
    "impartir":55,
    "issir":56,
    "mentir":57,
    "messeoir":58,
    "mourir":59,
    "mouvoir":60,
    "ouïr":61,
    "partir":62,
    "pouvoir":63,
    "prévaloir":64,
    "prévoir":65,
    "rassir":66,
    "repentir":67,
    "ressortir":68,
    "revaloir":69,
    "saillir":70,
    "sortir":71,
    "surseoir":72,
    "vêtir":73,
    "échoir":74,
    "asseoir":75,
    "assoir":76,
    "bouillir":77,
    "recevoir":78,
    "courir":79,
    "cueillir":80,
    "devoir":81,
    "endormir":82,
    "dormir":83,
    "fuir":84,
    "haïr":85,
    "promouvoir":86,
    "ouvrir":87,
    "pleuvoir":88,
    "pourvoir":89,
    "quérir":90,
    "assaillir":91,
    "savoir":92,
    "seoir":93,
    "servir":94,
    "valoir":95,
    "venir":96,
    "vouloir":97,
    "voir":98,
    "dévêtir":99,
    "finir":100,
    "acariâtre":101,
    "accroire":102,
    "bruire":103,
    "circoncire":104,
    "croître":105,
    "déclore":106,
    "embatre":107,
    "enclore":108,
    "ensuivre":109,
    "forclore":110,
    "forfaire":111,
    "frire":112,
    "inclure":113,
    "maudire":114,
    "occire":115,
    "oindre":116,
    "parfaire":117,
    "paître":118,
    "poindre":119,
    "raire":120,
    "reclure":121,
    "recroître":122,
    "renaître":123,
    "repaître":124,
    "résoudre":125,
    "sourdre":126,
    "stupéfaire":127,
    "suffire":128,
    "taire":129,
    "tistre":130,
    "éclore":131,
    "être":132,
    "aindre":133,
    "battre":134,
    "iendre":135,
    "prendre":136,
    "répandre":137,
    "boire":138,
    "clore":139,
    "clure":140,
    "confire":141,
    "connaître":142,
    "coudre":143,
    "crire":144,
    "croire":145,
    "accroître":146,
    "dire":147,
    "faire":148,
    "foutre":149,
    "lire":150,
    "luire":151,
    "mettre":152,
    "moudre":153,
    "naître":154,
    "joindre":155,
    "ompre":156,
    "cloître":157,
    "plaire":158,
    "braire":159,
    "rire":160,
    "soudre":161,
    "suivre":162,
    "uire":163,
    "vaincre":164,}

enIndex={
    }
enVerbIndex={
    "be":0,
    "to be":0,
    "have":1,}

Indexes=[frIndex,enIndex]
VerbIndexes=[frVerbIndex,enVerbIndex]

class Word():
    def __init__(self,w,language,grammar):
        """
        Parameters
        ----------
        w : word to create, as a string
        language : language the word is typed in
        grammar : grammatical class of the word, refer to table
        """
        self.w=w
        self.language=language if language.__class__==int else languages[language]
        self.grammar=grammar
    
    def idGramClass(self,prevClass):
        if self.language==-1:
            return
        lexicon=open("lexiques\\"+languages[self.language]+"Lexicon.txt",'r',-1,'utf-8')
        lexiList=lexicon.read().split('\n')
        lexicon.close()
        lexiList.pop()
        for i in range(len(lexiList)):
            lexiList[i]=lexiList[i].split('\t')
        
        found=False
        for i in Indexes[self.language][self.w[0]]:
            if lexiList[i][0]==self.w and not found:
                possibleGrammar=lexiList[i][3].split(',')
                for j in range(len(possibleGrammar)):
                    possibleGrammar[j]=grammarTable[possibleGrammar[j][0:3]]
                if len(possibleGrammar)<=1:
                    self.grammar=grammarTable[lexiList[i][2][0:3]]
                else:
                    grammarOrd=grammarTransitionTable[prevClass].copy()
                    for j in range(len(possibleGrammar)):
                        grammarOrd[possibleGrammar[j]]+=10
                    self.grammar=grammarOrd.index(max(grammarOrd))
                found=True
            if found:
                if grammarTable[lexiList[i][2][0:3]]==self.grammar:
                    rad=lexiList[i][1]
                    break
        self.__class__=grammarClassTable[self.grammar]
        self.convert(rad)
        return False
        

    def translate(self,target):
        """
        Parameters
        ----------
        target : language, as a string
        
        Translates the word to the target language.
        """
        if self.language==-1:
            return
        lexicon=open("lexiques\\translated lexicons\\"+languages[self.language]+"Lexicon.txt",'r',-1,'utf-8')
        lexiListSrc=lexicon.read().split('\n')
        lexicon.close()
        lexiListSrc.pop()
        
        lexicon=open("lexiques\\translated lexicons\\"+target+"Lexicon.txt",'r',-1,'utf-8')
        lexiListDest=lexicon.read().split('\n')
        lexicon.close()
        lexiListDest.pop()
        
        for i in Indexes[self.language][self.w[0]]:
            if lexiListSrc[i]==self.w:
                self.w=lexiListDest[i]
                self.language=languages[target]
                return
        print("never heard of the word ",self.w," in ",languages[self.language])
        
    def display(self):
        """
        Displays the word and its grammatical type.
        """
        print(self.w,' '*(15-len(self.w)),grammarTable[self.grammar],' '*12,end="")
    
    def write(self):
        return self.w

class Punctuation(Word):
    def __init__(self,w):
        super().__init__(w,-1,0)
    
    def convert(self,rad):
        return
        
class Name(Word):
    def __init__(self,w,language):
        super().__init__(w,language,1)
    
    def convert(self,rad):
        return

class Verb(Word):
    def __init__(self,w,language,tense,person):
        super().__init__(w,language,2)
        self.tense=tense
        self.person=person

    def convert(self,rad):
        #checking for infinitive*
        if self.w==rad:
            self.tense=-1
            self.person=0
            return
        #reading appropriate verb lexicon
        lexicon=open("lexiques\\"+languages[self.language]+"VerbLexicon.txt",'r',-1,'utf-8')
        lexiList=lexicon.read().split('\n')
        lexicon.close()
        lexiList.pop()
        #putting lexicon in correct format
        for i in range(len(lexiList)):
            lexiList[i]=lexiList[i].split()
            for j in range(len(lexiList[i])):
                lexiList[i][j]=lexiList[i][j].split(',')
        
        for i in range(len(lexiList[frVerbIndex[rad]])):
            for j in range(len(lexiList[frVerbIndex[rad]][i])):
                if lexiList[frVerbIndex[rad]][i][j]==self.w:
                    self.w=rad
                    self.tense=i
                    self.person=j
                    break
    
    def display(self):
        super().display()
        print(self.tense,' '*14,self.person,end="")
    
    def write(self):
        #checking for infinitive
        if self.tense==-1:
            return self.w
        #reading verb lexicon
        lexicon=open("lexiques\\"+languages[self.language]+"VerbLexicon.txt",'r',-1,'utf-8')
        lexiList=lexicon.read().split('\n')
        lexicon.close()
        lexiList.pop()
        
        #putting verb lexicon in correct format
        for i in range(len(lexiList)):
            lexiList[i]=lexiList[i].split()
            for j in range(len(lexiList[i])):
                lexiList[i][j]=lexiList[i][j].split(',')
                
        return lexiList[VerbIndexes[self.language][self.w]][self.tense][self.person]

class Adverb(Word):
    def __init__(self,w,language):
        super().__init__(w,language,3)
    
    def convert(self,rad):
        return

class Adjective(Word):
    def __init__(self,w,language):
        super().__init__(w,language,4)
    
    def convert(self,rad):
        return

class Auxiliary(Word):
    def __init__(self,w,language):
        super().__init__(w,language,5)
    
    def convert(self,rad):
        return

class Pronoun(Word):
    def __init__(self,w,language):
        super().__init__(w,language,6)
    
    def convert(self,rad):
        return
    
class Article(Word):
    def __init__(self,w,language):
        super().__init__(w,language,7)
    
    def convert(self,rad):
        return
    
class Preposition(Word):
    def __init__(self,w,language):
        super().__init__(w,language,8)
    
    def convert(self,rad):
        return
    
class Conjunction(Word):
    def __init__(self,w,language):
        super().__init__(w,language,9)
    
    def convert(self,rad):
        return
    
class Onomatopoeia(Word):
    def __init__(self,w,language):
        super().__init__(w,language,10)
    
    def convert(self,rad):
        return

grammarClassTable={
    0:Punctuation,
    1:Name,
    2:Verb,
    3:Adverb,
    4:Adjective,
    5:Auxiliary,
    6:Pronoun,
    7:Article,
    8:Preposition,
    9:Conjunction,
    10:Onomatopoeia}

class Sentence():
    def __init__(self,s,language):
        """
        Parameters
        ----------
        s : sentence to create, as a string
        language : language the sentence is typed in, as a string
        """
        self.table=[]
        #turn apostrophes into spaces
        s=s.replace('\'',' ')
        
        #add spaces around punctuations
        for i in s:
            if not i.isalpha() and i!=' ':
                s=s.replace(i,' '+i+' ')
        s=s.split()
        s[0]=s[0].lower()
            
        
        #Identifying grammatical classes
        for i in range(len(s)):
            prevclass=self.table[i-1].grammar if i>0 else 0
            if s[i][0].isupper():
                self.table.append(Word(s[i],-1,-1))
            elif not s[i][0].isalpha():
                self.table.append(Word(s[i],-1,0))
                if i+1<len(s):
                    s[i+1]=s[i+1].lower()
            else:
                self.table.append(Word(s[i],languages[language],-1))
            self.table[i].idGramClass(prevclass)
        
        #turning verbs into auxiliaries if next word is verb
        for i in range(len(self.table)-1):
            if self.table[i].grammar==2 and self.table[i+1].grammar==2:
                self.table[i].grammar=5
                self.table[i].__class__=Verb


    def translate(self,target):
        """
        Parameters
        ----------
        target : language, as a string

        Translates the sentence to the target language.
        """
        for i in range(len(self.table)):
            self.table[i].translate(target)
    
    def display(self):
        """
        Displays each word of the sentence, its language, and its grammatical type.
        """
        for i in range(len(self.table)):
            self.table[i].display()
            print()
    
    def write(self):
        """
        Returns the sentence.
        """
        s=self.table[0].w.title()
        for i in range(1,len(self.table)):
            s+=(' '*((self.table[i].grammar!=0)&(self.table[i-1].w!="-")))+self.table[i].write()
        return s
  

test=Sentence("Je suis prêt à la mise sur le marché! Appuyer sur X pour douter.","fr")
print(test.write())
test.display()
test.translate("en")
print(test.write())
