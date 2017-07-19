import random as r

class character:
		
		def __init__(self,f):
			
			self.content = fileread(f)
			
		def fileread(f):
			expect = ["NAME","EDITION","STR","DEX","CON","APP","SIZ","INT","POW","COMBAT","GENERAL"]
			with open(f) as generator:
				content = generator.readlines()
				generator.close()
			content = [x.strip('\n') for x in content]
			found = []
			for l in content:
				found.append(l.split('\t')[0])
			diff = lambda l1,l2: [x for x in l1 if x not in l2]
			d = set(diff(found,expect)) + set(diff(expect,found))
			if d:
				raise Exception("Invalid values: {}. Check source file for missing values/duplicates".format(', '.join(d)))
			content = {x.split('\t')[0] : x.split('\t')[1] for x in content}
			return content

                def roll(rollstr):
                    s = rollstr.split('d')
                    D = s[1]
                    rolls = [0] * s[0]
                    rolls = [r.randint(1,D) for x in rolls]
                    return sum(rolls)
