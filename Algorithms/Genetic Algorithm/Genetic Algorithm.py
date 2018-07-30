import random
import string

TargetWord = "HelloWorld"
max_population = 200
wordsize = len(TargetWord)
population = []
new_population = []
good_population = []
generation = 0
scores = []

# Creating the Next generation of members by joining the first and second halves
# of two randomly chosen members


def next_gen(member1, member2, score1, score2):
    temp = []
    list1 = list(member1)
    list2 = list(member2)
    for i in range(len(list1)):
        if(i < int(len(list1)/2)):
            temp.append(list1[i])
        else:
            temp.append(list2[i])
    new_member = ''.join(temp)

    return new_member

# Create a mutation so that the population does not stagnate


def mutation(member1, member2, score1, score2):
    temp = []
    list1 = list(member1)
    list2 = list(member2)
    randchar1 = random.randrange(0, int(len(list1)/2))
    randchar2 = random.randrange(int(len(list2)/2), len(list2))
    list1[randchar1] = random.choice(string.ascii_letters)
    list2[randchar2] = random.choice(string.ascii_letters)
    for i in range(len(list1)):
        if(i < int(len(list1)/2)):
            temp.append(list1[i])
        else:
            temp.append(list2[i])
    new_member = ''.join(temp)
    return new_member


# A class that assigns score and names to members of the population
class Population_properties:

    def __init__(self, member):
        self.member = member
        self.score = 0

    def score_update(self):
        count = 0
        for i in range(len(self.member)):
            if(self.member[i] == TargetWord[i]):
                count += 1
        self.score = (float(count)/len(self.member))*100



# Creating the First population
for i in range(max_population):
    temp = []
    for j in range(wordsize):
        x = random.choice(string.ascii_letters)
        temp.append(x)
    temp1 = ''.join(temp)

    object = Population_properties(temp1)
    population.append(object)

# creating 1000 generations that come after the first gen
while(generation < 1000):
    for i in range(len(population)):
        population[i].score_update()

        scores.append(population[i].score)

        if(population[i].score == 100):
            print("completed. Target Word: ", population[i].member)
            generation = 1000000
            break
        print(i, population[i].member, population[i].score, generation)

    max_score = max(scores)

    for i in range(len(population)):
        if(population[i].score >= 0.9*max_score):
            good_population.append(population[i])

    # Natural Selection. Survival of the fittest
    for i in range(max_population):
        randnum = random.random()
        if(randnum > 0.1):
            x = random.randrange(0, len(good_population))
            y = random.randrange(0, len(good_population))
            data = next_gen(good_population[x].member, good_population[y].member,
                            good_population[x].score, good_population[y].score)

        elif (randnum > 0.05 and randnum < 0.1):
            x = random.randrange(0, max_population)
            y = random.randrange(0, max_population)
            data = next_gen(population[x].member, population[y].member,
                            population[x].score, population[y].score)

        else:
            x = random.randrange(0, max_population)
            y = random.randrange(0, max_population)
            data = mutation(population[x].member, population[y].member,
                            population[x].score, population[y].score)

        # creating a new generation of population
        offspring = Population_properties(data)
        new_population.append(offspring)

    population = new_population
    new_population = []
    good_population = []

    generation += 1
