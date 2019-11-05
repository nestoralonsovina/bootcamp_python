class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1

        result = 0

        for coef, word in zip(coefs, words):
            result += coef * len(word)

        return result


    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1

        result = 0

        for i, word in enumerate(words):
            result += coefs[i] * len(word)

        return result
