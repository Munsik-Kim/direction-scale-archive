"""Semantic checks for denominators, duplicate keys and registered trapezoids."""
import unittest, sys
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from reproduce_summaries import exact_area,validate_counts
class SummaryContracts(unittest.TestCase):
    def fixture(self):
        return [dict(arm="A",step=str(k),group=g,n=str(n),correct=str(n//2))
          for k in range(0,1001,100) for g,n in (("01",184),("10",56))]
    def test_endpoint_weights(self):
        self.assertEqual(exact_area([Fraction(1)]+[Fraction(0)]*10),Fraction(1,20))
        self.assertEqual(exact_area([Fraction(0),Fraction(1)]+[Fraction(0)]*9),Fraction(1,10))
    def test_contrast_can_have_either_sign(self):
        a=exact_area([Fraction(1,2)]*11);b=exact_area([Fraction(1,3)]*11)
        self.assertEqual(a-b,Fraction(1,6));self.assertEqual(b-a,Fraction(-1,6))
    def test_duplicate_key_is_rejected_for_duplicate_reason(self):
        r=self.fixture();r.append(dict(r[0]))
        with self.assertRaisesRegex(ValueError,"DUPLICATE_EVALUATION_KEY"):validate_counts(r,{"01":184,"10":56})
    def test_group_swap_and_wrong_denominator(self):
        r=self.fixture();r[0]["n"]="56"
        with self.assertRaisesRegex(ValueError,"GROUP_DENOMINATOR_MISMATCH"):validate_counts(r,{"01":184,"10":56})
    def test_missing_node_is_not_interpolated(self):
        r=self.fixture()[1:]
        with self.assertRaisesRegex(ValueError,"INCOMPLETE_REGISTERED_GRID"):validate_counts(r,{"01":184,"10":56})
if __name__=="__main__":unittest.main()
