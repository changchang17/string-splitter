class TagManipulator:

    def parse_string(self, tags):
        result = []

        if len(tags) < 1 or tags == ",":
            return result

        result = tags.split(",")

        return result
