from collections import Counter 

def first_star(group_answers):
    return sum([len(set(ans.replace("\n", ""))) for ans in group_answers])


def second_star(group_answers):
    return sum(map(answers_per_group, group_answers))
    

def answers_per_group(answers):
    num_of_ppl = len(answers.split("\n"))
    occurences = Counter(answers.replace("\n", ""))
    return len([x for x in occurences.values() if x == num_of_ppl])



if __name__ == "__main__":
    group_answers = open('src/main/resources/day06/input.txt', 'r').read().split("\n\n")
    print(first_star(group_answers))
    print(second_star(group_answers))
