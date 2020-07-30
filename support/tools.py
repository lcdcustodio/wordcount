
class WCTools():

    def __init__(self):

        self.temp = []

    def no_case_sensitive(self, wordlist):

        count = 0

        for word in wordlist:

            if word.lower() not in self.temp:
                count += 1
                self.temp.append(word.lower())

        return count