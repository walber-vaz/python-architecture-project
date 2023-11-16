from dataclasses import dataclass

from src.modules.datalayer.base import RepositoryInterface


@dataclass
class ServiceBase:
    repository: RepositoryInterface
