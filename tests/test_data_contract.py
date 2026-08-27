import math
import unittest

from projects.lerobot_data_contract.core.data_contract import ConversionToken, convert_degrees_to_radians_once


class DataContractTest(unittest.TestCase):
    def test_conversion_token_prevents_double_degree_to_radian_conversion(self):
        converted, token = convert_degrees_to_radians_once([180.0], ConversionToken.fresh())
        self.assertAlmostEqual(converted[0], math.pi)
        with self.assertRaises(ValueError):
            convert_degrees_to_radians_once(converted, token)

    def test_rejects_nonfinite_values(self):
        with self.assertRaises(ValueError):
            convert_degrees_to_radians_once([float("inf")], ConversionToken.fresh())


if __name__ == "__main__":
    unittest.main()

