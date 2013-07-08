class ScenarioSelector(object):

    def __init__(self,scenario):
	self.scenario = scenario

    def return_scenario(self,user_data):
        return self.scenario(user_data)

    def scenario_prompts(self):
	return self.scenario.prompts()
