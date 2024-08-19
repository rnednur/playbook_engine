from abc import ABC, abstractmethod

class Step(ABC):
    @abstractmethod
    def execute(self, context):
        pass

class SQLStep(Step):
    def __init__(self, query):
        self.query = query

    def execute(self, context):
        return context.query_executor.execute_query(self.query)

class BranchStep(Step):
    def __init__(self, condition, true_branch, false_branch):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def execute(self, context):
        if eval(self.condition, {}, context.data_manager.data):
            return self.true_branch.execute(context)
        else:
            return self.false_branch.execute(context)

class LoopStep(Step):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def execute(self, context):
        results = []
        while eval(self.condition, {}, context.data_manager.data):
            results.append(self.body.execute(context))
        return results
