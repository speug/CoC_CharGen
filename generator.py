import random as r
class RangeDict(dict):
    def __getitem__(self, item):
        if type(item) != range: # or xrange in Python 2
            for key in self:
                if item in key:
                    return self[key]
        else:
            return super().__getitem__(item)

class character:
    DB = RangeDict({range(2,64) : ('-2',-2), range(65,84) : ('-1',-1), range(85,124) : ('',0), range(125,164) : ('+1d4',1), range(165,204) : ('+1d6',2), range(205,284) : ('+2d6',3), range(285,364) : ('+3d6',4), range(365,444) : ('+4d6',5), range(445,524) : ('+5d6',6)})

    def __init__(self,f):

        self.content = fileread(f)
	self.STR = roll(self.content["STR"])
	self.DEX = roll(self.content["DEX"])
	self.CON = roll(self.content["CON"])
	self.SIZ = roll(self.content["SIZ"])
	self.APP = roll(self.content["APP"])
	self.INT = roll(self.content["INT"])
	self.POW = roll(self.content["POW"])
	self.EDU = roll(self.content["EDU"])
        self.HP = int((self.CON + self.SIZ)/10) 
        self.phys = DB[(self.STR+self.SIZ)]
        self.db = self.phys[0]
        self.build = self.phys[1]

    def fileread(self,f):
	expect = {"NAME","EDITION","STR","DEX","CON","APP","SIZ","INT","POW","EDU","COMBAT","GENERAL"}
	with open(f) as generator:
            content = generator.readlines()
	    generator.close()
	content = [x.strip('\n') for x in content]
	found = {}
	for l in content:
	    found.append(l.split('\t')[0])
	diff = lambda l1,l2: [x for x in l1 if x not in l2]
	d = set(diff(found,expect)) + set(diff(expect,found))
	if d:
	    raise Exception("Invalid values: {}. Check source file for missing values/duplicates".format(', '.join(d)))
	content = {x.split('\t')[0] : x.split('\t')[1] for x in content}
	return content

        def roll(self,rollstr):
            s = rollstr.split('d')
            D = s[1]
            rolls = [0] * s[0]
            rolls = [r.randint(1,D) for x in rolls]
            return sum(rolls)*5

