# tests/test_feature_store.py
import unittest
import pandas as pd
from feature_store.loader import FeatureLoader

class TestFeatureStore(unittest.TestCase):

    def test_loader(self):
        # 샘플 CSV 생성

        # ======================================
        #             Fill your code
        # ======================================
        sample = pd.DataFrame({
            'user_id': [1, 2],
            'item_id': [10, 20],
            'event_type': ['view', 'click'],
            'ts': ['2025-01-01 10:00', '2025-01-01 10:02']
        })
        sample.to_csv('tests/sample.csv', index=False)

        loader = FeatureLoader()
        loaded = loader.load_logs('tests/sample.csv')

        assert len(loaded) == 2


if __name__ == '__main__':
    unittest.main()
