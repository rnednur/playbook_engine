from playbook_engine.nlq_engine import NLQEngine
from playbook_engine.query_executor import QueryExecutor
from playbook_engine.data_manager import DataManager
from playbook_engine.logger import Logger
from playbook_engine.config import Config
from playbook_engine.models.playbook import Playbook
from playbook_engine.playbook_executor import PlaybookExecutor

def main():
    nlq_engine = NLQEngine(Config.NLQ_API_URL)
    query_executor = QueryExecutor(Config.DB_TYPE, Config.DB_CONNECTION_PARAMS)
    data_manager = DataManager()
    logger = Logger("PlaybookEngine")

    playbook_executor = PlaybookExecutor(nlq_engine, query_executor, data_manager, logger)

    playbook = Playbook("path/to/your/playbook.yaml")
    playbook_executor.execute_playbook(playbook)

if __name__ == "__main__":
    main()

