from ..utils.yaml_parser import load_yaml
from .step import SQLStep, BranchStep, LoopStep

class Playbook:
    def __init__(self, yaml_file):
        self.steps = load_yaml(yaml_file)

    def parse_steps(self):
        parsed_steps = []
        for step in self.steps:
            if 'sql' in step:
                parsed_steps.append(SQLStep(step['sql']))
            elif 'branch' in step:
                condition = step['branch']['condition']
                true_branch = self.parse_steps(step['branch']['true'])
                false_branch = self.parse_steps(step['branch']['false'])
                parsed_steps.append(BranchStep(condition, true_branch, false_branch))
            elif 'loop' in step:
                condition = step['loop']['condition']
                body = self.parse_steps(step['loop']['body'])
                parsed_steps.append(LoopStep(condition, body))
        return parsed_steps

