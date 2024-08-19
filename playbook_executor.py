class PlaybookExecutor:
    def __init__(self, nlq_engine, query_executor, data_manager, logger):
        self.nlq_engine = nlq_engine
        self.query_executor = query_executor
        self.data_manager = data_manager
        self.logger = logger

    def execute_playbook(self, playbook):
        self.logger.info("Starting playbook execution")
        for step in playbook.parse_steps():
            try:
                result = step.execute(self)
                self.data_manager.set(f"step_{playbook.steps.index(step)}_result", result)
            except Exception as e:
                self.logger.error(f"Error executing step: {e}")
                raise
        self.logger.info("Playbook execution completed")

