import random
import time

scores = []
multi_choices = []
times = []
custom_quizzes = {}
repeat = 0
YES = "y"
NO = "n"
MIN_QUESTIONS = 3
MULTI_CHOICE_QUESTIONS = 4
MIN_POSITION = 0
MAX_POSITION = 3
DIFFICULTY_1 = 1
DIFFICULTY_2 = 2
DIFFICULTY_3 = 3
PERCENT_80 = 0.8
PERCENT_50 = 0.5
SELECT_A_QUIZ = "1"
TRY_AGAIN = "2"
VIEW_PAST_SCORES = "3"
EXIT = "exit"
MATH = "math"
FRENCH = "french"
SCIENCE = "science"
ENGLISH = "english"
CUSTOM = "custom"
MAX_DIFFICULTY = 3
MIN_DIFFICULTY = 0
MIN_QUESTION_AMMOUNT = 0

MATH_DIFFICULTY_1 = {
"Solve: 5 + 3 x 2": "11",
"Solve: 12 ÷ 4 + 6": "9",
"What is 7²?": "49",
"Solve: 15 - 8": "7",
"What is 10% of 50?": "5",
"Solve: 3x = 12": "x = 4",
"What is the perimeter of a square with side 4?": "16",
"Convert 0.5 to a fraction": "1/2",
"Solve: 20 ÷ 5": "4",
"What is 9 x 6?": "54",
"Solve: x + 7 = 10": "x = 3",
"What is 100 - 45?": "55",
"Convert 25% to decimal": "0.25",
"What is 8³?": "512",
"Solve: 6x = 30": "x = 5",
"What is the area of a rectangle (l=5, w=3)?": "15",
"Solve: 14 + 9": "23",
"What is 81 ÷ 9?": "9",
"Round 4.6 to nearest whole": "5",
"What is 11 x 11?": "121"
}

MATH_DIFFICULTY_2 = {
"Solve: 2x + 3 = 11": "x = 4",
"Factor: x² + 5x": "x(x+5)",
"Solve: 3(x - 2) = 9": "x = 5",
"What is √144?": "12",
"Expand: (x + 4)(x + 2)": "x² + 6x + 8",
"Solve: x/2 = 7": "x = 14",
"What is 15% of 200?": "30",
"Simplify: 3x + 2x": "5x",
"Solve: x² = 25": "x = ±5",
"Area of triangle (b=10, h=5)": "25",
"Convert 3/4 to decimal": "0.75",
"Solve: 4x - 8 = 0": "x = 2",
"What is 2³ x 2²?": "32",
"Find mean of 2,4,6,8": "5",
"Solve: 5x = 3x + 10": "x = 5",
"Simplify: 10a ÷ 2": "5a",
"What is 1.2 + 3.8?": "5.0",
"Solve: 9x = 81": "x = 9",
"What is 50% of 90?": "45",
"Expand: 2(x + 3)": "2x + 6"
}

MATH_DIFFICULTY_3 = {
"Solve: x² - 9 = 0": "x = ±3",
"Factor: x² - 5x + 6": "(x-2)(x-3)",
"Solve: 2x² = 18": "x = ±3",
"Expand: (x + 3)²": "x² + 6x + 9",
"Solve: x² + 4x = 0": "x=0,-4",
"Find gradient between (1,2) and (3,6)": "2",
"Solve: 3x + 2 = 2x + 7": "x = 5",
"What is √200 (simplified)?": "10√2",
"Solve: 5x - 3 = 2x + 9": "x = 4",
"Factor: x² - 16": "(x-4)(x+4)",
"Solve: (x+2)(x-2)=0": "x=2,-2",
"Find midpoint of (2,4),(6,8)": "(4,6)",
"Solve: 4x² = 64": "x = ±4",
"What is sin(90°)?": "1",
"Solve: x² = 49": "x = ±7",
"Expand: (x-5)(x+5)": "x²-25",
"Solve: 6x + 1 = 13": "x = 2",
"What is log₁₀(100)?": "2",
"Solve: x² + 2x - 8 = 0": "(x+4)(x-2)",
"Find slope of horizontal line": "0"
}

ENGLISH_DIFFICULTY_1 = {
"What is a noun?": "A naming word",
"What is a verb?": "An action word",
"Identify adjective in: 'blue sky'": "blue",
"Plural of 'child'?": "children",
"What is a sentence?": "A complete idea",
"Synonym for 'happy'?": "joyful",
"Antonym for 'big'?": "small",
"What is a pronoun?": "Replaces noun",
"Identify verb: 'She runs'": "runs",
"Capital of sentence needed?": "Yes",
"Full stop used for?": "End of sentence",
"What is an adverb?": "Describes verb",
"Synonym for 'fast'?": "quick",
"Opposite of 'hot'?": "cold",
"What is a paragraph?": "Group of sentences",
"Identify noun: 'dog barks'": "dog",
"What is punctuation?": "Writing symbols",
"What is a question mark used for?": "Questions",
"What is dialogue?": "Conversation",
"What is a title?": "Name of text"
}

ENGLISH_DIFFICULTY_2 = {
"What is a metaphor?": "Direct comparison",
"What is a simile?": "Comparison using like/as",
"Identify simile: 'as fast as lightning'": "simile",
"What is tone?": "Author's attitude",
"What is theme?": "Main idea",
"What is alliteration?": "Same starting sounds",
"Define imagery": "Descriptive language",
"What is a clause?": "Group of words",
"What is a compound sentence?": "Two clauses",
"Synonym for 'angry'?": "furious",
"What is formal writing?": "Serious style",
"What is informal writing?": "Casual style",
"What is personification?": "Human traits to objects",
"Identify verb tense in 'ran'": "past",
"What is a conjunction?": "Joining word",
"What is structure?": "Organisation of text",
"Define narrative": "Story writing",
"Define persuasive": "Convincing text",
"What is dialogue used for?": "Character speech",
"What is audience?": "Who it's for"
}

ENGLISH_DIFFICULTY_3 = {
"Analyse metaphor purpose": "Adds deeper meaning",
"What is irony?": "Opposite expectation",
"Define satire": "Humour to criticise",
"What is juxtaposition?": "Contrasting ideas",
"Define symbolism": "Represents ideas",
"What is connotation?": "Implied meaning",
"What is denotation?": "Literal meaning",
"Explain tone shift": "Change in attitude",
"Define rhetorical question": "No answer needed",
"What is ethos?": "Credibility appeal",
"What is pathos?": "Emotional appeal",
"What is logos?": "Logical appeal",
"What is ambiguity?": "Multiple meanings",
"Define motif": "Recurring idea",
"What is genre?": "Type of text",
"Explain bias": "One-sided view",
"Define thesis": "Main argument",
"What is cohesion?": "Text flow",
"What is syntax?": "Sentence structure",
"What is diction?": "Word choice"
}

SCIENCE_DIFFICULTY_1 = {
"What is the boiling point of water (°C)?": "100",
"What planet do we live on?": "Earth",
"What gas do humans breathe in?": "Oxygen",
"What is H2O?": "Water",
"What force pulls objects to Earth?": "Gravity",
"What part of plant makes food?": "Leaf",
"What is the center of an atom called?": "Nucleus",
"What state of matter is air?": "Gas",
"What do plants need for photosynthesis?": "Sunlight",
"What is freezing point of water (°C)?": "0",
"What organ pumps blood?": "Heart",
"What do we use to see?": "Eyes",
"What is a solid?": "Fixed shape",
"What is a liquid?": "Flows",
"What is a gas?": "Spreads out",
"What is the Sun?": "Star",
"What do animals need to survive?": "Food",
"What is energy?": "Ability to do work",
"What is a habitat?": "Living place",
"What is a magnet attracted to?": "Metal"
}

SCIENCE_DIFFICULTY_2 = {
"What is photosynthesis?": "Plants make food",
"What gas do plants release?": "Oxygen",
"What is an atom?": "Smallest particle",
"What is evaporation?": "Liquid to gas",
"What is condensation?": "Gas to liquid",
"What is friction?": "Force resisting motion",
"What is gravity?": "Pulling force",
"What is a chemical reaction?": "Substances change",
"What is speed?": "Distance over time",
"What is a cell?": "Basic unit of life",
"What is a circuit?": "Path of electricity",
"What is voltage?": "Electrical force",
"What is mass?": "Amount of matter",
"What is density?": "Mass per volume",
"What is a solution?": "Mixed substances",
"What is a vertebrate?": "Has backbone",
"What is an invertebrate?": "No backbone",
"What is renewable energy?": "Can be replaced",
"What is non-renewable energy?": "Runs out",
"What is insulation?": "Reduces heat transfer"
}

SCIENCE_DIFFICULTY_3 = {
"What is the formula for photosynthesis?": "CO2 + H2O → glucose + O2",
"What is acceleration?": "Change in velocity",
"What is Newton's First Law?": "Objects stay at rest/motion unless force",
"What is kinetic energy?": "Energy of motion",
"What is potential energy?": "Stored energy",
"What is the periodic table?": "Elements chart",
"What is an ion?": "Charged particle",
"What is pH scale?": "Acidity measure",
"What is DNA?": "Genetic material",
"What is evolution?": "Change over time",
"What is natural selection?": "Survival of fittest",
"What is wavelength?": "Distance between waves",
"What is frequency?": "Wave cycles per second",
"What is electricity?": "Flow of electrons",
"What is power?": "Energy per second",
"What is force formula?": "F = ma",
"What is velocity?": "Speed with direction",
"What is ecosystem?": "Living system",
"What is homeostasis?": "Stable conditions",
"What is respiration?": "Energy release in cells"
}

FRENCH_DIFFICULTY_1 = {
"Hello in French": "Bonjour",
"Goodbye in French": "Au revoir",
"Thank you in French": "Merci",
"Yes in French": "Oui",
"No in French": "Non",
"Please in French": "S'il vous plaît",
"What is 'dog' in French?": "Chien",
"What is 'cat' in French?": "Chat",
"What is 'house' in French?": "Maison",
"What is 'water' in French?": "Eau",
"What is 'bread' in French?": "Pain",
"What is 'school' in French?": "École",
"What is 'friend' in French?": "Ami",
"What is 'book' in French?": "Livre",
"What is 'car' in French?": "Voiture",
"What is 'red' in French?": "Rouge",
"What is 'blue' in French?": "Bleu",
"What is 'one' in French?": "Un",
"What is 'two' in French?": "Deux",
"What is 'three' in French?": "Trois"
}

FRENCH_DIFFICULTY_2 = {
"Translate: I am": "Je suis",
"Translate: You are": "Tu es",
"Translate: He is": "Il est",
"Translate: She is": "Elle est",
"Translate: We are": "Nous sommes",
"Translate: They are": "Ils sont",
"Translate: I have": "J'ai",
"Translate: You have": "Tu as",
"Translate: He has": "Il a",
"Translate: She has": "Elle a",
"What is 'to eat' in French?": "Manger",
"What is 'to go' in French?": "Aller",
"What is 'to do' in French?": "Faire",
"Translate: I eat": "Je mange",
"Translate: I go": "Je vais",
"Translate: I do": "Je fais",
"What is 'big' in French?": "Grand",
"What is 'small' in French?": "Petit",
"What is 'happy' in French?": "Heureux",
"What is 'sad' in French?": "Triste"
}

FRENCH_DIFFICULTY_3 = {
"Translate: I will go": "J'irai",
"Translate: I went": "Je suis allé",
"Translate: I have eaten": "J'ai mangé",
"What is past tense called?": "Passé composé",
"What is future tense called?": "Futur simple",
"What is present tense called?": "Présent",
"Translate: We are eating": "Nous mangeons",
"Translate: They went": "Ils sont allés",
"Translate: She will do": "Elle fera",
"What is 'because' in French?": "Parce que",
"What is 'however' in French?": "Cependant",
"What is 'always' in French?": "Toujours",
"What is 'never' in French?": "Jamais",
"What is 'sometimes' in French?": "Parfois",
"Translate: I like": "J'aime",
"Translate: I don't like": "Je n'aime pas",
"What is reflexive verb?": "Verb with self",
"Translate: I wake up": "Je me réveille",
"What is 'must' in French?": "Devoir",
"Translate: I must go": "Je dois aller"
}



user_action  = SELECT_A_QUIZ
while True:

    if user_action == SELECT_A_QUIZ:
        print(f"Welcome to MAGS quizzes we offer a range of quizzes these include \nMath, English, Science and French for english and science multichoice is suggested")

        #prints custom quizzes if there are any
        if custom_quizzes != {}:
            print("You also have custom quizzes: ")
            for custom_questions in custom_quizzes:
                print(custom_questions)
        
        print()
        while True:
            subject = input("What subject would you like to study (to create or edit your own subject type custom): ").lower()
            if subject == "":
                print("Please enter a subject")
            else:
                print(f"{subject} selected")
                break
        
        #sets difficulty for not custom subjects
        if subject == MATH or subject == ENGLISH or subject == FRENCH or subject == SCIENCE:
            while True:
                try:
                    difficulty = int(input("What difficulty would you like 1 2 or 3: "))
                    if difficulty < MIN_DIFFICULTY or difficulty > MAX_DIFFICULTY:
                        print("Please select a number between 1 and 3")
                        print()
                    else:
                        print(f"Difficulty set to {difficulty}")
                        break
                except ValueError:
                    print("Thats not a number")
                    print()

    #makes it if you are trying to retry a custom game 
    #that you just made you dont have to re enter all the questions
    if user_action == TRY_AGAIN and subject == CUSTOM:
        subject = custom_name
        

    if user_action == SELECT_A_QUIZ or user_action == TRY_AGAIN:
        correct = 0

    #sets the question dictionary to the preset dictionarys
        if subject == MATH:
            if difficulty == DIFFICULTY_1:
                questions = MATH_DIFFICULTY_1

            elif difficulty == DIFFICULTY_2:
                questions = MATH_DIFFICULTY_2

            elif difficulty == DIFFICULTY_3:
                questions = MATH_DIFFICULTY_3
            
        elif subject == FRENCH:
            if difficulty == DIFFICULTY_1:
                questions = FRENCH_DIFFICULTY_1

            elif difficulty == DIFFICULTY_2:
                questions = FRENCH_DIFFICULTY_2

            elif difficulty == DIFFICULTY_3:
                questions = FRENCH_DIFFICULTY_3

        elif subject == SCIENCE:
            if difficulty == DIFFICULTY_1:
                questions = SCIENCE_DIFFICULTY_1

            elif difficulty == DIFFICULTY_2:
                questions = SCIENCE_DIFFICULTY_2

            elif difficulty == DIFFICULTY_3:
                questions = SCIENCE_DIFFICULTY_3

        elif subject == ENGLISH:
            if difficulty == DIFFICULTY_1:
                questions = ENGLISH_DIFFICULTY_1

            elif difficulty == DIFFICULTY_2:
                questions = ENGLISH_DIFFICULTY_2

            elif difficulty == DIFFICULTY_3:
                questions = ENGLISH_DIFFICULTY_3

        #adds a custom subject
        elif subject == CUSTOM:
            while True:
                custom_name = input("What is the name of your custom quiz (you can add or edit): ")
                if custom_name == "":
                    print("Please enter a name")
                    print()

                elif custom_name == CUSTOM:
                    print("You cant name your quiz custom")
                    print()

                else:
                    break

            #creates a custom dictionary if one 
            #dosen't already exist with that name
            if custom_name not in custom_quizzes:
                    custom_quizzes[custom_name] = {}
                    print("creating custom quiz")
            else:
                print("Editing previous quiz")
            
            #asks for the number of questions
            print("Your quiz needs at least 4 questions")
            while True:
                try:
                    custom_question_amount = int(input("How many questions do you want to add: "))
                    if (custom_question_amount > MIN_QUESTIONS and custom_name):
                        break
                    else:
                        print("The minimum amount of questions is 4 please enter 4 or greater")
                        print()
                except ValueError:
                    print("Thats not a number of questions")
                    print()
            
            for custom_num in range(custom_question_amount):
                #adds custom question
                while True:
                    custom_question = input(f"What is question {custom_num + 1}: ")
                    if custom_question == "":
                        print("Please enter a question")
                        print()

                    elif custom_question in custom_quizzes[custom_name].keys():
                        print("Please don't add duplicate questions")
                        print()
                        
                    else:
                        break
                
                #adds custom awnsers
                while True:
                    custom_answer = input(f"What is answer {custom_num + 1}: ")
                    if custom_answer == "":
                        print("Please enter an answer")
                        print()

                    elif custom_answer in custom_quizzes[custom_name].keys():
                        print("Please don't add duplicate answers")
                        print()

                    else:
                        break

                custom_quizzes[custom_name][custom_question] = custom_answer

            questions = custom_quizzes[custom_name]

        #if the subject is a custom subject it sets
        #the questions to the questions from that subject
        elif subject in list(custom_quizzes.keys()):
            questions = custom_quizzes[subject]

        else:
            print()
            print("We don't offer that subject yet but you can add it yourself")
            print()
            continue

        #gives the option for multi choice
        while True:

            multi_choice = input("Would you like it to be multi choice (y/n): ").lower()
            if multi_choice == YES:
                print("Multi choice enabled")
                break

            elif multi_choice == NO:
                print("multi choice disabled")
                break

            else:
                print("Please enter y or n")
                print()

        #gets the amount of questions
        if user_action == SELECT_A_QUIZ:
            while True:
                try:
                    question_amount = int(input("How many questions would you like to do: "))
                    if question_amount > MIN_QUESTION_AMMOUNT:
                        break
                    else:
                        print("You need to enter a positive interger")
                        print()
                except ValueError:
                    print("Thats not a number of questions")
                    print()

        #repeats getting a question checking it against an input and printing if its right or wrong
        print()
        print("Quizz started")
        starting_time = time.time()
        for question_num in range(question_amount):
            print(f"Question {question_num + 1} of {question_amount}")

            random_key = random.choice(list(questions.keys()))  #random questions
            print(random_key)

            #prints 4 options incluiding the right one
            if multi_choice == YES:
                print("The awnser is one of these four")

                repeat = 0
                multi_choices = []
                print_answer_at = random.randint(MIN_POSITION,MAX_POSITION)
                for question_number in range(MULTI_CHOICE_QUESTIONS):

                    #picks a random position to print the random answer
                    if repeat == print_answer_at:
                        multi_choices.append(questions[random_key])
                        print(f"{question_number + 1}) {questions[random_key]}")

                    #prints 3 not duplicate answers in positions that are not already occupied
                    else:
                        while True:
                            rand_multi_choice = random.choice(list(questions.keys()))

                            if (questions[rand_multi_choice] not in multi_choices 
                            and rand_multi_choice != random_key):
                                
                                break

                        multi_choices.append(questions[rand_multi_choice])
                        print(f"{question_number + 1}) {questions[rand_multi_choice]}")

                    repeat += 1

            #takes the input and answer removes the spaces and makes it lowercase
            while True:
                answer = input("Enter the answer: ")
                if answer == "":
                    print("Please enter an answer")
                    print()
                else:
                    break

            answer = answer.replace(" ", "")
            answer = answer.lower()
            correct_answer = questions[random_key].replace(" ", "")
            correct_answer = correct_answer.lower()

            #checks if the input is equal to the awnser or the number of the awnser 
            #if multi choice is selected
            try:
                answer_number = int(answer)
                num_ans = YES

            except ValueError:  
                num_ans = NO

            if (answer == correct_answer) or (multi_choice == YES and num_ans == YES              
                and answer_number - 1 == multi_choices.index(questions[random_key])):
                    print("Correct")
                    correct += 1
            else:
                print(f"That is wrong the answer was {questions[random_key]}: ")

            print()

        ending_time = time.time()

        #all correct
        print(f"You got {correct} right and {question_amount - correct} wrong")
        if correct == question_amount:
            print("You got them all right amazing job")

        #80% to 100%
        elif correct >= question_amount * PERCENT_80:
            print("You got more than 80 percent right good work")

        #50% to 80%
        elif correct >= question_amount * PERCENT_50:
            print("You got between 50 and 80 percent getting there")

        #less than 50%
        else:
            print("You got less that half right room for improvement")

        
        scores.append(f"{correct}/{question_amount}")

        #looks at the time taken to complete the quiz
        time_taken = round(ending_time - starting_time, 1)
        print(f"You took {time_taken} seconds to complete the quiz")
        
        times.append(time_taken)

    #looks at all past scores
    elif user_action == VIEW_PAST_SCORES:
        quiz_num = 0
        for score, times_taken in zip(scores, times):
            print(f"The score for quiz {quiz_num + 1} is {score}")
            print(f"The time for {quiz_num + 1} is {times_taken} seconds")
            quiz_num += 1

    #checks a quiz that corresponds to enterd input
    elif user_action == EXIT:
        print("Exited quizzes")
        print("Here are your scores")
        quiz_num = 0
        for score, times_taken in zip(scores, times): #this makes a list where they are together like (a,b), (c,d)
            print(f"The score for quiz {quiz_num + 1} is {score}")
            print(f"The time for {quiz_num + 1} is {times_taken} seconds")
            quiz_num += 1
        break

    #gives player options of things to do when the quiz is finished
    while True:
        user_action = input("What would you like to do 1 try another quiz 2 restart the quiz 3 view past test scores or exit: ").lower()
        if user_action == "":
            print("Please enter one of the 4 choices")
            print()
        else:
            break
