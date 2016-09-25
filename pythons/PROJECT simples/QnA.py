#! usr/bin/env python3.5

"""
this short program is a question and answers thingy that asks the user a question and based on the answer provided
to the questions validates the users answer. and then it keeps a log of all the correct answers that there are.

so to the pseudo-code of the how the thing will work is this.

provide the test as single multiList.
Within the test multiList is a list containing the 'question item' and 'answer item' respectively.
therefore the 'question item will have index of 0' and the 'answer item, an index of 1'.
see an example over here.

test = [["What color is the daytime sky on a clear day? ", "blue"],
["What is the answer to life, the universe and everything? ", "42"],
["What is a three letter word for mouse trap? ", "cat"]]

first of all i think we should have a questions creator of some sort.

len = get the length of questions in the test.
using the while loop, get all the questions and the answers to the questions individually and then store the rights.
"""

test = [
    ["What color is the daytime sky on a clear day? ", "blue"],
    ["What is the answer to life, the universe and everything? ", "42"],
    ["What is a three letter word for mouse trap? ", "cat"]
]


class Test:
    """
    this is just a simple class tool that is supposed to be used to create a multi list for questions and
    answers that will be used by the exams method to take the test.
    """

    def __init__(self, name):
        """
        first of all the test should take the name of the test as the first argument.
        """
        self.name = name
        self.questions = []

    def add_q_a(self, question, answer=None):
        if type(question) == list:
            q = question
        else:
            q = [question, answer]
        self.questions.append(q)

    def exam(self):
        # takes an argument of the multiList and then performs the necessary actions on it

        if type(self.questions) != list:
            raise Exception("exam accepts only a list containing list of questions")
        total_questions = len(self.questions)
        right = 0
        index = 0
        print("{:^20}you are taking a ".upper().format(" ") + self.name.upper() + " test".upper(), end="\n\n")

        while index < total_questions:
            response = input(self.questions[index][0] + " ")
            print(response.lower() == str(self.questions[index][1]), end="\n\n")

            if response.lower() == str(self.questions[index][1]):
                right += 1
            index += 1

        percent = right * 100 / total_questions

        print(right, " / ", total_questions)
        print("percentage = ", str(abs(percent))+"%")
        return [total_questions, right]


if __name__ == '__main__':

    t = Test(" General ")
    for i in test:
        t.add_q_a(i)
    t.add_q_a("what is my name ?  ", "danny mcwaves")
    t.add_q_a("what is my favorite food ?  ", "idk")
    t.add_q_a("how old am i ?  ", 19)

    t.exam()
