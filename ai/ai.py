from database import DataBase
from database import Questions
from database import Question
from database import Answers
from database import Answer
from database import Results


class ArtificialIntelligence(object):

	def __init__(self, allQuests, mainQuests, resultsFile):
		db = DataBase(allQuests, mainQuests, resultsFile)
		self.questions = db.getQuestions()
		print(self.questions)
		self.mainQuestions = db.getMainQuestionsPos()
		print(self.mainQuestions)
		self.results = db.getResults()
		print(self.results)

		self.beginFlag = False
		self.userAnswers = []

		self.currentMainQPos = 0


	def begin(self):
		self.userAnswers = []
		self.beginFlag = True
		self.currentMainQPos = 0
		return self.getMainQuestion()

	def getMainQuestion(self):
		if self.currentMainQPos >= len(self.mainQuestions):
			self.beginFlag = False
			return None
		else:
			i = self.mainQuestions[self.currentMainQPos]
			q = self.questions.getQuestion(i)
			self.currentMainQPos += 1
			return q

	def isNoLink(self, answer):
		if answer.getQLink() == None:
			return True
		else:
			return False

	def getNextQuestion(self, answer):
		if self.beginFlag == True:
			self.addUserAnswer(answer)
			if self.isNoLink(answer):
				return self.nextMainQ()
			else:
				return self.nextChainQuestion(answer)
		else:
			return None

	def nextMainQ(self):
		return self.getMainQuestion()

	def addUserAnswer(self, answer):
		self.userAnswers.append(answer)

	def nextChainQuestion(self, answer):
		return self.questions.getQuestion(answer.getQLink())

	def getUserAnswers(self):
		return self.userAnswers

	def findFilm(self):
		for result in self.results:
			if self.isItFilm(result) == True:
				return result
		return None

	def isItFilm(self, result):
		if(len(self.userAnswers) <= len(result.getShortNames())):
			for userAnswer in self.userAnswers:
				if self.checkCriteria(userAnswer.getShortName(), result.getShortNames()) != True:
					return False
			return True
		else:
			return False

	def checkCriteria(self, criteria, shortNames):
		for shortName in shortNames:
			if shortName == criteria:
				return True
		return False	