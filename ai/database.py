import json

allQ = "questions"
pos = "position"
Q = "question"
answrs = "answers"
answr = "answer"
answer_image = "answer-image"
linkToQ = "qlink"
shortName = "shortName"
image = "image"

mainQ = "MainQuestions"
qPos = "qPos"

res = "results"
film = "film"
shortNames = "shortNames"


class DataBase(object):

	def __init__(self, allQuests, mainQuests, results):
		self.database = self.__getBD(allQuests)
		self.mainQuestions = self.__getBD(mainQuests)
		self.results = self.__getBD(results)

	def __getBD(self, filename):
		with open(filename, "r") as db:
			datab = json.load(db)
			return datab

	def getQuestions(self):
		return Questions(self.database.get(allQ))

	def getMainQuestionsPos(self):
		objPoses = self.mainQuestions.get(mainQ) 
		poses = []
		for pos in objPoses:
			poses.append(pos.get(qPos))
		return poses

	def getResults(self):
		return Results(self.results.get(res))


class Questions(object):

	def __init__(self, questions_):
		self.questions = self.__getQuestions(questions_)

	def __getQuestions(self, questions_):
		questionsArr = []
		for question in questions_:
			questionsArr.append(Question(question))
		return questionsArr

	def __getitem__(self,index):
		if index > len(self.questions):
			return None
		else:
			return self.questions[index]

	def getQuestion(self, position):
		for question in self.questions:
			if(question.getPosition() == position):
				return question
		return None

	def __str__(self):
		string = "QUESTIONS {\n"
		for question in self.questions:
			string +=  str(question) + "\n"
		return string + "}"


class Question(object):

	def __init__(self, question_):
		self.question = question_

	def getPosition(self):
		return self.question.get(pos)

	def getName(self):
		return self.question.get(Q)

	def getImage(self):
		return self.question.get(image)

	def getAnswers(self):
		return Answers(self.question.get(answrs))

	def __str__(self):
		# return str(self.getName())
		return "\tQUESTION:\n\t" + str(self.getPosition()) + "\n\t" + str(self.getName()) + "\n" + str(self.getAnswers())


class Answers(object):

	def __init__(self, answers_):
		self.answers = self.__getAnswers(answers_)

	def __getAnswers(self, answers_):
		answersArr = []
		for answer in answers_:
			answersArr.append(Answer(answer))
		return answersArr

	def __getitem__(self,index):
		if index > len(self.answers):
			return None
		else:
			return self.answers[index]

	def getAnswer(self, position):
		for answer in self.answers:
			if(answer.getPosition() == position):
				return answer
		return None

	def __str__(self):
		string = "\tANSWERS {\n"
		for answer in self.answers:
			string +=  str(answer) + "\n"
		return string + "}"


class Answer(object):

	def __init__(self, answer_):
		self.answer = answer_

	def getName(self):
		return self.answer.get(answr)

	def getPosition(self):
		return self.answer.get(pos)

	def getShortName(self):
		return self.answer.get(shortName)

	def getQLink(self):
		return self.answer.get(linkToQ)

	def getAnsImage(self):
		return self.answer.get(answer_image)
	
	def __str__(self):
		# return str(self.getName())
		return "\t\tANSWER:\n\t\t\t" + str(self.getPosition()) + "\n\t\t\t" + str(self.getName()) + "\n\t\t\t" + str(self.getShortName()) + "\n\t\t\t" + str(self.getQLink())


class Results(object):

	def __init__(self, results_):
		self.results = self.__getResults(results_)

	def __getResults(self, results_):
		resultsArr = []
		for result in results_:
			resultsArr.append(Result(result))
		return resultsArr

	def __getitem__(self,index):
		if index > len(self.results):
			return None
		else:
			return self.results[index]

	def __str__(self):
		string = "RESULTS {\n"
		for result in self.results:
			string +=  str(result) + "\n"
		return string + "}"


class Result(object):

	def __init__(self, result_):
		self.result = result_

	def getFilm(self):
		
		return self.result.get(film)

	def getShortNames(self):
		return self.result.get(shortNames)

	def getImage(self):
		return self.result.get(image)

	def __str__(self):
		# return self.getPlace()
		return "\tRESULT:\n\t\t" + str(self.getFilm()) + "\n\t\t" + str(self.getShortNames())
