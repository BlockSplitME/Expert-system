from ai import ArtificialIntelligence
from flask import Flask, redirect, render_template, request, jsonify
import numpy as np

way = "ai/db/"
allQuestionsFile = way+"AllQuestions.json"
mainQuestionsFile = way+"MainQuestions.json"
resultsFile = way+"Results.json"

AI = ArtificialIntelligence(allQuestionsFile, mainQuestionsFile, resultsFile)
question = None
answer = None
resultNum = None

def getBeginQuestion():
	global question
	question = AI.begin()
	return question

def getNextQuestion():
	global question
	question = AI.getNextQuestion(answer)
	return question

def getAnswersStr():
	global question
	context = {}
	context["question"] = str(question.getName())
	context["image"] = str(question.getImage())
	context["answers"] = []
	for answer in question.getAnswers():
			context["answers"].append({"answer" : str(answer.getName()), "pos": str(answer.getPosition()), "answer_image" : str(answer.getAnsImage())})
			# answers += (str(answer) + "| " + str(answer.getPosition()) + "<br>")
	return context

def getResult(result):
	global resultNum
	context = {}
	films = result.getFilm()
	images = result.getImage()
	resultNum = np.random.uniform(0, len(films))
	context["film"] = str(films[int(resultNum)])
	context["image"] = str(images[int(resultNum)])
	return context

def nextResult(result):
	global resultNum
	context = {}
	films = result.getFilm()
	images = result.getImage()
	if((resultNum + 1) >= len(films)):
		resultNum = 0
	else:
		resultNum += 1

	context["film"] = str(films[int(resultNum)])
	context["image"] = str(images[int(resultNum)])
	return context

def getAnswer_(index):
	global answer
	global question
	answers = question.getAnswers()
	answer = answers.getAnswer(index)

def createApp():
	app = Flask(__name__)

	@app.route("/")
	def hello():
		question = getBeginQuestion()
		context = getAnswersStr()
		return render_template("index.html", context=context)

	@app.route("/question")
	def quest():
		context = getAnswersStr()
		return render_template("question.html", context=context)

	@app.route("/result")
	def resilt():
		context = getResult(AI.findFilm())
		return render_template("result.html", context=context)
	
	@app.route("/newresult")
	def newresult():
		context = nextResult(AI.findFilm())
		return render_template("result.html", context=context)
	
	# начало
	@app.route("/begin")
	def begin():
		question = getBeginQuestion()
		return redirect("question")

	@app.route("/next")
	def next():
		question = getNextQuestion()
		if question != None:
			return redirect("/question")
		else:
			return redirect("/result")

	@app.route("/answer", methods=['POST'])
	def answer():
		getAnswer_(int(request.form["position"]))
		# question = getNextQuestion()
		return redirect("next")

	return app