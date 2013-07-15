class PlayerInput(object):

    def call(self):
        return raw_input()

class InputValidator(object):

    @staticmethod
    def return_valid_response(input_source,valid_responses):
        data_type = type(valid_responses[0])
        user_input = "junky text that shouldn't be VaLid"
        while user_input not in valid_responses:
            try:
                user_input = data_type(input_source.call())
            except:
                continue
        return user_input
