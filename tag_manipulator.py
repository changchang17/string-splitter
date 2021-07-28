class TagManipulator:

    def parse_string(self, tags):
        result = []

        if len(tags) < 1 or tags == ",":
            return result

        result = tags.split(",")
        for index in range(0, len(result)):
            new_entry = result[index].strip()
            result[index] = new_entry

        return result
