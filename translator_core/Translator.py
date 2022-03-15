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
                        #SELF PCT NAM VER ADV ADJ AUX PRO ART PRE CON ONO   #PREV
grammarTransitionTablePrev=[[-1,  7,  6,  9,  5,  4,  8,  2,  1,  3,  0],   #PCT
                            [-1,  6,  7,  6,  9,  5,  9,  4,  2,  1,  0],   #NAM
                            [-1,  6,  0,  9,  6,  5,  7,  8,  3,  2,  1],   #VER
                            [-1,  6,  5,  4,  7,  3,  8,  2,  9,  1,  0],   #ADV
                            [-1,  9,  8,  7,  6,  5,  4,  7,  3,  1,  0],   #ADJ
                            [-1,  8,  9,  7,  6,  5,  4,  3,  2,  1,  0],   #AUX
                            [-1,  3,  9,  7,  6,  5,  4,  5,  2,  1,  0],   #PRO
                            [-1,  8,  7,  6,  8,  5,  9,  3,  2,  1,  0],   #ART
                            [-1,  8,  7,  6,  5,  4,  3,  9,  2,  1,  0],   #PRE
                            [-1,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0],   #CON
                            [-1,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0]]   #ONO

                        #SELF PCT NAM VER ADV ADJ AUX PRO ART PRE CON ONO   #NEXT
grammarTransitionTableNext=[[-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  0],   #PCT
                            [-1,  6,  7,  6,  7,  5,  9,  8,  2,  1,  0],   #NAM
                            [-1,  6,  0,  9,  7,  5,  4,  8,  3,  2,  1],   #VER
                            [-1,  6,  5,  4,  7,  3,  8,  2,  9,  1,  0],   #ADV
                            [-1,  9,  2,  7,  6,  5,  4,  2,  3,  1,  0],   #ADJ
                            [-1,  8,  9,  7,  6,  5,  4,  3,  2,  1,  0],   #AUX
                            [-1,  8,  9,  7,  6,  5,  8,  3,  2,  1,  0],   #PRO
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
    "es":2,
    2:"es",
    "ru":3,
    3:"ru",
    "us":4,
    4:"us",
    "it":5,
    5:"it",
    "po":6,
    6:"po",
    "de":7,
    7:"de"}


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
    "vaincre":164,
    "appeler":165,
    "lancer":166,
    "rigoler":167,
    "jouer":168,
    "choisir":169,
    "collecter":170,
    "marcher":171,
    "combattre":172,
    "aimer":173,
    "chanter":174,
    "danser":175,
    "discuter":176,
    "comprendre":177,
    "apprendre":178,}

enIndex={
    }
enVerbIndex={
    "be":0,
    "to be":0,
    "have":1,    
    "go":2,
    "fall":3,
    "send":4,
    "place":5,
    "discard":6,
    "weigh":7,
    "snow":8,
    "celebrate":9,
    "set":10,
    "protect":11,
    "eat":12,
    "talk":13,
    "enslave":14,
    "agree":15,
    "lie":16,
    "die":17,
    "can":18,
    "plan":19,
    "exit":20,
    "dress":21,
    "sit":22,
    "boil":23,
    "receive":24,
    "run":25,
    "collect":26,
    "must":27,
    "sleep":28,
    "flee":29,
    "hate":30,
    "promise":31,
    "open":32,
    "know":33,
    "serve":34,
    "come":35,
    "want":36,
    "see":37,
    "finish":38,
    "include":39,
    "curse":40,
    "pay":41,
    "resolve":42,
    "suffice":43,
    "beat":44,
    "take":45,
    "spread":46,
    "drink":47,
    "know":48,
    "sew":49,
    "shout":50,
    "believe":51,
    "increase":52,
    "say":53,
    "do":54,
    "read":55,
    "put":56,
    "enclose":57,
    "please":58,
    "laugh":59,
    "follow":60,
    "overcome":61,
    "call":62,
    "launch":63,
    "play":64,
    "choose":65,
    "walk":66,
    "fight":67,
    "like":68,
    "love":69,
    "sing":70,
    "dance":71,
    "discuss":72,
    "understand":73,
    "learn":74}

esIndex={
    }
esVerbIndex={
    "estar":0,
    "ser":1,    
    "haber":2,
    "ir":3,
    "caigar":4,
    "enviar":5,
    "poner":6,
    "tirar":7,
    "pesar":8,
    "celebrar":9,
    "ajustar":10,
    "proteger":11,
    "comer":12,
    "hablar":13,
    "esclavizar":14,
    "mentir":15,
    "morir":16,
    "marchar":17,
    "poder":18,
    "proveer":19,
    "salir":20,
    "vestir":21,
    "sentar":22,
    "hervir":23,
    "recibir":24,
    "correr":25,
    "recoger":26,
    "deber":27,
    "dormir":28,
    "huir":29,
    "odiar":30,
    "prometer":31,
    "abrir":32,
    "saber":33,
    "conocer":34,
    "servir":35,
    "valer":36,
    "venir":37,
    "querer":38,
    "ver":39,
    "terminar":40,
    "incluir":41,
    "pagar":42,
    "resolver":43,
    "satisfacer":44,
    "callar":45,
    "batir":46,
    "llevar":47,
    "beber":48,
    "coser":49,
    "gritar":50,
    "creer":51,
    "aumentar":52,
    "decir":53,
    "hacer":54,
    "leer":55,
    "nacer":56,
    "complacer":57,
    "reír":58,
    "seguir":59,
    "fracasar":60,
    "llamar":61,
    "tirar":62,
    "jugar":63,
    "escoger":64,
    "caminar":65,
    "combatir":66,
    "amar":67,
    "cantar":68,
    "bailar":69,
    "discutir":70,
    "comprender":71,
    "aprender":72}

deIndex={
    }
deVerbIndex={
    "sein":0,
    "haben":1,    
    "gehen":2,
    "fallen":3,
    "schicken":4,
    "platzen":5,
    "werfen":6,
    "wiegen":7,
    "feiern":8,
    "anpassen":9,
    "beschützen":10,
    "essen":11,
    "sprechen":12,
    "lüge":13,
    "sterben":14,
    "verlassen":15,
    "können":16,
    "vorhersagen":17,
    "ausgehen":18,
    "kleid":19,
    "sitzen":20,
    "kochen":21,
    "bekommen":22,
    "lauf":23,
    "sammeln":24,
    "müssen":25,
    "einschlafen":26,
    "schlafen":27,
    "fliehen":28,
    "hassen":29,
    "versprechen":30,
    "offen":31,
    "wissen":32,
    "dienen":33,
    "kommen":34,
    "wollen":35,
    "sehen":36,
    "beenden":37,
    "enthalten":38,
    "zahlen":39,
    "lösen":40,
    "genügen":41,
    "vertuschen":42,
    "schlagen":43,
    "nehmen":44,
    "trinken":45,
    "nähen":46,
    "schreien":47,
    "glauben":48,
    "steigen":49,
    "sagen":50,
    "machen":51,
    "lesen":52,
    "stellen":53,
    "geboren":54,
    "zufrieden stellen":55,
    "lachen":56,
    "scherzen":57,
    "folgen":58,
    "besiegen":59,
    "anrufen":60,
    "werfen":61,
    "spieler":62,
    "wählen":63,
    "kampf":64,
    "mögen":65,
    "singen":66,
    "tanzen":67,
    "diskutieren":68,
    "verstehen":69,
    "lernen":70}

itIndex={
    }
itVerbIndex={
    "essere":0,
    "andare":1,    
    "cadere":2,
    "inviare":3,
    "risultare":4,
    "collocare":5,
    "gettare":6,
    "pesare":7,
    "celebrare":8,
    "cedere":9,
    "regolare":10,
    "proteggere":11,
    "mangiare":12,
    "parlare":13,
    "asservire":14,
    "mentire":15,
    "morire":16,
    "scommettere":17,
    "potere":18,
    "prevedere":19,
    "uscire":20,
    "vestire":21,
    "sedere":22,
    "bollire":23,
    "ricevere":24,
    "correre":25,
    "dovere":26,
    "addormentare":27,
    "dormire":28,
    "fuggire":29,
    "odiare":30,
    "promettere":31,
    "aprire":32,
    "sapere":33,
    "servire":34,
    "valere":35,
    "venire":36,
    "volere":37,
    "vedere":38,
    "finire":39,
    "includer":40,
    "pagare":41,
    "risolvere":42,
    "bastare":43,
    "tacere":44,
    "battere":45,
    "prendere":46,
    "bere":47,
    "cucire":48,
    "urlare":49,
    "credere":50,
    "aumentare":51,
    "dire":52,
    "fare":53,
    "leggere":54,
    "mettere":55,
    "nascere":56,
    "aderire":57,
    "piacere":58,
    "ridere":59,
    "seguire":60,
    "sconfiggere":61,
    "chiamare":62,
    "giocatore":63,
    "scegliere":64,
    "camminare":65,
    "lottare":66,
    "amare":67,
    "cantare":68,
    "danzare":69,
    "discutere":70,
    "comprendere":71,
    "imparare":72}

poIndex={
    }
poVerbIndex={
    "estar":0,
    "ser":1,    
    "ter":2,
    "ir":3,
    "outonar":4,
    "enviar":5,
    "colocar":6,
    "pesar":7,
    "celebrar":8,
    "regular":9,
    "proteger":10,
    "comer":11,
    "falar":12,
    "subjugar":13,
    "mentir":14,
    "morrer":15,
    "poder":16,
    "prever":17,
    "sair":18,
    "vestir":19,
    "sentar":20,
    "ferver":21,
    "receber":22,
    "correr":23,
    "coletar":24,
    "dever":25,
    "adormecer":26,
    "dormir":27,
    "fugir":28,
    "odiar":29,
    "prometer":30,
    "abrir":31,
    "saber":32,
    "conhecer":33,
    "servir":34,
    "valer":35,
    "vir":36,
    "querer":37,
    "ver":38,
    "terminar":39,
    "incluir":40,
    "pagar":41,
    "resolver":42,
    "bastar":43,
    "silenciar":44,
    "lutar":45,
    "tomar":46,
    "beber":47,
    "coser":48,
    "gritar":49,
    "acreditar":50,
    "aumentar":51,
    "dizer":52,
    "fazer":53,
    "ler":54,
    "nascer":55,
    "juntar":56,
    "gostar":57,
    "seguir":58,
    "superar":59,
    "chamar":60,
    "lançar":61,
    "rir":62,
    "jogar":63,
    "escolher":64,
    "andar":65,
    "combater":66,
    "amar":67,
    "cantar":68,
    "dançar":69,
    "discutir":70,
    "compreender":71,
    "aprender":72}

ruIndex={
    }
ruVerbIndex={
    "estar":0,
    "ser":1,    
    "haber":2,
    "ir":3,
    "caigar":4,
    "enviar":5,
    "poner":6,
    "tirar":7,
    "pesar":8,
    "celebrar":9,
    "ajustar":10,
    "proteger":11,
    "comer":12,
    "hablar":13,
    "esclavizar":14,
    "mentir":15,
    "morir":16,
    "marchar":17,
    "poder":18,
    "proveer":19,
    "salir":20,
    "vestir":21,
    "sentar":22,
    "hervir":23,
    "recibir":24,
    "correr":25,
    "recoger":26,
    "deber":27,
    "dormir":28,
    "huir":29,
    "odiar":30,
    "prometer":31,
    "abrir":32,
    "saber":33,
    "conocer":34,
    "servir":35,
    "valer":36,
    "venir":37,
    "querer":38,
    "ver":39,
    "terminar":40,
    "incluir":41,
    "pagar":42,
    "resolver":43,
    "satisfacer":44,
    "callar":45,
    "batir":46,
    "llevar":47,
    "beber":48,
    "coser":49,
    "gritar":50,
    "creer":51,
    "aumentar":52,
    "decir":53,
    "hacer":54,
    "leer":55,
    "nacer":56,
    "complacer":57,
    "reír":58,
    "seguir":59,
    "fracasar":60,
    "llamar":61,
    "tirar":62,
    "jugar":63,
    "escoger":64,
    "caminar":65,
    "combatir":66,
    "amar":67,
    "cantar":68,
    "bailar":69,
    "discutir":70,
    "comprender":71,
    "aprender":72}


Indexes=[frIndex,enIndex,esIndex,deIndex,itIndex,poIndex,ruIndex]
VerbIndexes=[frVerbIndex,enVerbIndex,esVerbIndex,deVerbIndex,itVerbIndex,poVerbIndex,ruVerbIndex]

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
        self.possibleGrammar=None
        self.lexicalIndex=-1
    
    def initIdGramClass(self,lexiList):
        if self.language==-1:
            self.possibleGrammar=[[0,1]]
            return
        
        #finding the word in lexiList and extracting its possible grammar types
        for i in Indexes[self.language][self.w[0]]:
            if lexiList[i][0]==self.w:
                self.possibleGrammar=lexiList[i][3].split(',')
                for j in range(len(self.possibleGrammar)):
                    self.possibleGrammar[j]=[grammarTable[self.possibleGrammar[j][0:3]],1/len(self.possibleGrammar)]
                self.lexicalIndex=i
                break
    
    def iterIdGramClass(self,prevPossibleGrammar,nextPossibleGrammar):
        if self.language==-1:
            return
        for i in range(len(self.possibleGrammar)):
            factor=0
            for j in range(len(prevPossibleGrammar)):
                factor+=prevPossibleGrammar[j][1]*grammarTransitionTablePrev[prevPossibleGrammar[j][0]][self.possibleGrammar[i][0]]
            self.possibleGrammar[i][1]=self.possibleGrammar[i][1]*factor
            
            factor=0
            for j in range(len(nextPossibleGrammar)):
                factor+=nextPossibleGrammar[j][1]*grammarTransitionTableNext[nextPossibleGrammar[j][0]][self.possibleGrammar[i][0]]
            self.possibleGrammar[i][1]=self.possibleGrammar[i][1]*factor
        
        self.possibleGrammar[:]=[pG for pG in self.possibleGrammar if pG[1]!=0]
        totalWeight=sum([pG[1] for pG in self.possibleGrammar])
        self.possibleGrammar[:]=[[pG[0],pG[1]/totalWeight] for pG in self.possibleGrammar]
    
    def finaIdGramClass(self,lexiList,debug):
        if self.language==-1:
            return
        if debug:
            print(self.w)
            print([[grammarTable[pG[0]], pG[1]] for pG in self.possibleGrammar])
        
        if len(self.possibleGrammar)<=1:
            self.grammar=self.possibleGrammar[0][0]
        else:
            weightList=[pG[1] for pG in self.possibleGrammar]
            self.grammar=self.possibleGrammar[weightList.index(max(weightList))][0]
        
        for i in range(self.lexicalIndex,self.lexicalIndex+10):
            if grammarTable[lexiList[i][2][0:3]]==self.grammar:
                rad=lexiList[i][1]
                break
        self.__class__=grammarClassTable[self.grammar]
        self.convert(rad)

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
    
    def copy(self):
        return Word(self.w,self.language,self.grammar)

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
    
    def copy(self):
        c=super().copy()
        c.__class__=Verb
        c.tense=self.tense
        c.person=self.person
        return c

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
    def __init__(self,s=None,language=None,debug=False):
        self.table=[]
        if s==None:
            return
        #turn apostrophes into spaces
        s=s.replace('\'',' ')
        
        #add spaces around punctuations
        for i in s:
            if not i.isalpha() and i!=' ':
                s=s.replace(i,' '+i+' ')
        s=s.split()
        s[0]=s[0].lower()
            
        #formatting lexiList
        lexicon=open("lexiques\\"+(languages[language] if language.__class__==int else language)+"Lexicon.txt",'r',-1,'utf-8')
        lexiList=lexicon.read().split('\n')
        lexicon.close()
        lexiList.pop()
        for i in range(len(lexiList)):
            lexiList[i]=lexiList[i].split('\t')
        
        #Identifying grammatical classes
        for i in range(len(s)):
            if s[i][0].isupper():
                self.table.append(Word(s[i],-1,-1))
            elif not s[i][0].isalpha():
                self.table.append(Word(s[i],-1,0))
                if i+1<len(s):
                    s[i+1]=s[i+1].lower()
            else:
                self.table.append(Word(s[i],languages[language],-1))
            self.table[i].initIdGramClass(lexiList)
        for i in range(10):
            possibleGrammar=[w.possibleGrammar for w in self.table]
            possibleGrammar.insert(0,[[0,1]])
            possibleGrammar.append([[0,1]])
            for j in range(len(self.table)):
                self.table[j].iterIdGramClass(possibleGrammar[j], possibleGrammar[j+2])
        for i in range(len(self.table)):
            self.table[i].finaIdGramClass(lexiList,debug)

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
    
    def copy(self):
        """
        returns a copy of this sentence
        """
        c=Sentence()
        c.table=[w.copy() for w in self.table]
        return c

test=Sentence("Ceci est un test","fr",True)
test2=test.copy()
print(test.write())
test.display()
test.translate("en")
print(test.write())
print(test2.write())
