from abc import ABC, abstractmethod
import pandas as pd

class BaseFeature(ABC):
    """피처 생성의 기본 인터페이스를 정의하는 추상 클래스"""

    @abstractmethod
    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        주어진 데이터프레임에서 피처를 생성하는 메서드

        Args:
            df (pd.DataFrame): 원본 데이터프레임

        Returns:
            pd.DataFrame: 생성된 피처가 포함된 데이터프레임
        """
        pass

    @abstractmethod
    def schema(self) -> dict:
        """
        생성된 피처의 스키마를 반환하는 메서드

        Returns:
            dict: 피처 이름과 데이터 타입을 포함하는 딕셔너리
        """
        pass