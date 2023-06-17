from abc import ABC, abstractmethod


class ISceneManager(ABC):
    @abstractmethod
    def nextScene(self, scene):
        pass
