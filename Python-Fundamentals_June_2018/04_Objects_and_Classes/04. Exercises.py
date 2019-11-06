#define class Exercise
class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems

#collect inputs and sort them into Exercise class
r_inp = input()
while r_inp != "go go go":
    topic_inp, courseName, judgeLink, exercise_string = r_inp.split(" -> ")
    exercise_list = exercise_string.split(", ")
    result = Exercise(topic_inp, courseName, judgeLink, exercise_list)

#print results
    print(f"Exercises: {result.topic}")
    print(f"Problems for exercises and homework for the \"{result.course_name}\" course @ SoftUni.")
    print(f"Check your solutions here: {result.judge_contest_link}")

#print problems
    i = 0
    for each in result.problems:
        i += 1
        print(f"{i}. {each}")

    r_inp = input()
