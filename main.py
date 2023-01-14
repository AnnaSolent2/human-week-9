class Human:

  # class (constant) attribute
  MAX_ENERGY = 100

  # initialiser
  def __init__(self, name="Human", age=0):
    self.name = name
    self.age = age
    self.energy = Human.MAX_ENERGY

  # magic methods
  def __repr__(self):
    return f'human(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'

  # instance methods
  def display(self):
    print(f"I am {self.name}")

  def grow(self):
    self.age += 1

  def eat(self, amount):
    potential_energy = self.energy + amount
    if (potential_energy > Human.MAX_ENERGY):
      self.energy = Human.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0

  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0


if (__name__ == "__main__"):
  human = Human()
  print(repr(human))
  human.move(10)
  print(repr(human))
  human.eat(5)
  print(repr(human))
  human.eat(20)
  print(repr(human))

class Robot:

  # class attribute
  laws = "Protect, Obey and Survive"
  
  # class (constant) attribute
  MAX_ENERGY = 100

  # A static method
  @staticmethod
  def the_laws():
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self, name="Robot", age=0):

    # An instance attribute
    self.name = name
    self.age = age
    self.energy = Robot.MAX_ENERGY

  def __repr__(self):
    return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'
  
  # An instance method
  def display(self):
    print(f"I am {self.name}")

  def eat(self, amount):
    potential_energy = self.energy + amount
    if (potential_energy > Robot.MAX_ENERGY):
      self.energy = Robot.MAX_ENERGY
      return potential_energy - self.energy
    else:
      self.energy = potential_energy
      return 0

  def grow(self):
    self.age += 1

  def move(self, distance):
    potential_energy = self.energy - distance
    if (potential_energy < 0):
      self.energy = 0
      return self.energy - abs(potential_energy)
    else:
      self.energy = potential_energy
      return 0

if (__name__ == "__main__"):
  robot = Robot()
  Robot.the_laws()
  print(repr(robot))
  robot.move(10)
  print(repr(robot))
  robot.eat(5)
  print(repr(robot))
  robot.eat(20)
  print(repr(robot))

from human import Human
from robot import Robot

class Planet:

  def __init__(self):
    self.inhabitants = {
      'humans':[],
      'robots':[]
    }

  def __repr__(self):
    return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots."

  def add_human(self, human):
    self.inhabitants['humans'].append(human)

  def add_robot(self, robot):
    self.inhabitants['robots'].append(robot)

  def remove_human(self, human):
    self.inhabitants['humans'].remove(human)

  def remove_robot(self, robot):
    self.inhabitants['robots'].remove(robot)

if (__name__ == "__main__"):
  planet = Planet()
  print(repr(planet))
  prins = Human("Prins")
  planet.add_human(prins)
  print(repr(planet))
  print(planet)

from planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt

import random

class Universe:

  def __init__(self):
    self.planets = []

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets."

  def generate(self):
    # create a new planet
    planet = Planet()

    # populate with random humans and robots
    for index in range(random.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot)

    for index in range(random.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add_human(human)

    # add to list of planets
    self.planets.append(planet)

  def show_populations(self):
    num_subplots = len(self.planets)
    
    fig, axs = plt.subplots(1, num_subplots)
    
    for index in range(num_subplots):
      planet = self.planets[index]
      num_humans = len(planet.inhabitants['humans'])
      num_robots = len(planet.inhabitants['robots'])

      if (num_subplots == 1):
        axs.bar([1, 2], [num_humans, num_robots])
      else:
        axs[index].bar([1, 2], [num_humans, num_robots])

    plt.tight_layout()  
    plt.show()


if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.show_populations()

from planet import Planet
from planet import Planet
from robot import Robot
from human import Human
import matplotlib.pyplot as plt

import random

class Universe:

  def __init__(self):
    self.planets = []

  def __repr__(self):
    return f"universe(planets={self.planets})"

  def __str__(self):
    return f"The universe contains {len(self.planets)} planets."

  def generate(self):
    # create a new planet
    planet = Planet()

    # populate with random humans and robots
    for index in range(random.randint(1, 10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot)

    for index in range(random.randint(1, 10)):
      human = Human(f"Human{index}")
      planet.add_human(human)

    # add to list of planets
    self.planets.append(planet)

  def show_populations(self):
    num_subplots = len(self.planets)
    
    fig = plt.figure()
    
    for index in range(num_subplots):
      planet = self.planets[index]
      num_humans = len(planet.inhabitants['humans'])
      num_robots = len(planet.inhabitants['robots'])

      ax = fig.add_subplot(1, num_subplots, index+1)
      ax.bar([1, 2], [num_humans, num_robots])

    plt.tight_layout()  
    plt.show()


if (__name__ == "__main__"):
  universe = Universe()
  universe.generate()
  universe.generate()
  universe.show_populations()

