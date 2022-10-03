
# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!


from game.casting.actor import Actor


class Artifact(Actor):
    def __init__(self):
        self.message = ""

    def get_message(self):

        return self.message

    def set_message(self, message):
        self.message = message
