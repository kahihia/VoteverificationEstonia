import pandas


class Bayes_Election:
	def __init__(self):
		self.age =[]
		self.female_voters = []
		self.male_voters = []
		self.female_verifiers = []
		self.male_verifiers = []
		self.sum_voters=[]
		self.probability_yes=[]
		self.probability_no=[]
		self.probability_men_yes=[]
		self.probability_men_no=[]
		self.probability_female_no=[]
		self.probability_female_yes=[]
		self.probability_mobile=[]
		self.probability_os=[]
		self.probability_voters=[]
		self.voters=[]
		self.verifiers =[]
		self.total_male_non_verifiers=0
		self.total_non_verifiers=0
		self.total_female_non_verifiers =0
		self.prob_mobile_yes=0
	def load_femalever(self, filename):
		#filename = input("Choose femaleverpercentage csv to load")
		#print filename
		colnames = ["","age","female_voters","male_voters","procf.x","procm.x","female_verifiers","male_verifiers","procf.y","procm.y","propprocf"]
		data = pandas.read_csv(filename, names=colnames)
		return data
	def load_verifiersag(self, filename):
		#filename = input("Choose femaleverpercentage csv to load")
		#print filename
		colnames = ["","age","voters", "verifiers", "activity"]
		data = pandas.read_csv(filename, names=colnames)
		return data
	def populate_data(self, data, data2):
		self.age = data.age.tolist()
		self.female_voters = data.female_voters.tolist()
		self.male_voters = data.male_voters.tolist()
		self.female_verifiers = data.female_verifiers.tolist()
		self.male_verifiers = data.male_verifiers.tolist()
		self.age.pop(0)
		self.female_voters.pop(0)
		self.female_verifiers.pop(0)
		self.male_voters.pop(0)
		self.male_verifiers.pop(0)
		self.voters=data2.voters.tolist()
		self.verifiers=data2.verifiers.tolist()
		self.voters.pop(0)
		self.verifiers.pop(0)
		self.sum_verifiers=sum(int(x) for x in self.verifiers)
		self.sum_voters = sum(int(x) for x in self.voters)
		self.total_non_verifiers =  self.sum_voters -self.sum_verifiers
		self.total_male_non_verifiers =sum(float(x) for x in self.male_voters)-sum(float(x) for x in self.male_verifiers)
		self.total_female_non_verifiers =sum(float(x) for x in self.female_voters)-sum(float(x) for x in self.female_verifiers)
		
	def prob_yes(self):
		for x in range(len(self.age)):
			x=int(x)
			self.probability_yes.append(float(self.verifiers[x])/self.sum_verifiers)
			#print float(self.verifiers[x])
	def prob_no(self):
		for x in range(len(self.age)):
			x=int(x)
			self.probability_no.append((float(self.voters[x])-float(self.verifiers[x]))/(self.sum_voters-self.sum_verifiers))
			#print float(self.verifiers[x])
	def prob_voters(self):
		for x in range(len(self.age)):
			x=int(x)
			self.probability_voters.append(float(self.voters[x])/self.sum_voters)
	def prob_male_yes(self):
		self.probability_men_yes.append(sum(float(x) for x in self.male_verifiers)/self.sum_verifiers)

	def prob_male_no(self):
		self.probability_men_no.append(self.total_male_non_verifiers/self.total_non_verifiers)
		#print self.total_male_non_verifiers
		#print self.total_non_verifiers
	def prob_female_yes(self):
		self.probability_female_yes.append(sum(float(x) for x in self.female_verifiers)/self.sum_verifiers)

	def prob_female_no(self):
		self.probability_female_no.append(self.total_female_non_verifiers/self.total_non_verifiers)
		#print self.total_male_non_verifiers
		#print self.total_non_verifiers
	def prob_mob_yes(self, mobile):
		self.prob_mobile_yes=float(mobile)/self.sum_verifiers
	def prob_mob_no(self, mobile):
		self.prob_mobile_no=mobile/self.total_non_verifiers
if __name__ == '__main__':
	x=Bayes_Election()
	data=x.load_femalever('2015_femaleverpercage.csv')
	data2=x.load_verifiersag('2015_verifiersage.csv')
	x.populate_data(data, data2)
	x.prob_yes()
	x.prob_no()
	x.prob_voters()
	x.prob_male_yes()
	x.prob_male_no()
	x.prob_female_no()
	x.prob_female_yes()
	
