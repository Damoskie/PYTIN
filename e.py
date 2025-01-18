# Define the Robot class
class Robot:
    # Constructor to initialize the robot's name, model, and version
    def __init__(self, name, model, version):
        self.name = name
        self.model = model
        self.version = version
    
    # Method to introduce the robot
    def introduce(self):
        return f"Hello, I am {self.name}. I am a {self.model} model, version {self.version}."
    
    # Method to display robot's capabilities
    def capabilities(self):
        return f"I am capable of performing various tasks such as cleaning, assisting, and interacting with humans."
    
    # Method to show robot's status
    def status(self):
        return f"{self.name} is currently active and operational."


# Create an instance of the Robot class
robot1 = Robot("RoboX", "X500", "1.0")

# Introduce the robot
print(robot1.introduce())

# Show the robot's capabilities
print(robot1.capabilities())

# Show the robot's current status
print(robot1.status())
