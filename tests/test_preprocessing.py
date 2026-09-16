import unittest

from src.codemix_nlp.preprocessing import normalize_text, script_ratio


class PreprocessingTests(unittest.TestCase):
    def test_normalize_whitespace_and_punctuation(self):
        text = "  Hello   world!!!  "
        self.assertEqual(normalize_text(text), "Hello world!")

    def test_script_ratio(self):
        ratios = script_ratio("Hello नमस्ते")
        self.assertGreater(ratios["latin"], 0)
        self.assertGreater(ratios["devanagari"], 0)
        self.assertAlmostEqual(sum(ratios.values()), 1.0)


if __name__ == "__main__":
    unittest.main()
