class character:
		
		def __init__(self,f):
			
			self.file = fileread(f)
			
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
			d = set(diff(found,expect))
			if d:
				raise Exception("Invalid values: {}. Check source file for missing values/duplicates".format(', '.join(d)))
			content = {x.split('\t')[0] : x.split('\t')[1] for x in content}
			return content