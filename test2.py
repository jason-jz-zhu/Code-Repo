"""
simple_test = unit + smoke
rigorous_test = regression + end-to-end
simple_test_cost = low, for early feedback
rigorous_test_cost = high, for production-readiness
not all tests are run for every release due to cost-risk tradeoff
"""

import math

class ReleaseTestCadence():
    """ tests """
    def __init__(self, cadence, releases, simple_cost, rigorous_cost):
        self.cadence = cadence
        self.releases = releases
        self.simple_cost = simple_cost
        self.rigorous_cost = rigorous_cost

    def simple_tests_needed(self):
        """
        compute the min number of simple tests need for this release cadence
        returns the min number of simple tests need for this release cadence
        """
        if self.releases < 6:
            return 0
        elif self.releases > 12:
            return (self.releases // 3) * 2
        return self.releases // 2
    
    def rigorous_tests_needed(self):
        """
        compute the min number of rigorous tests need for this release cadence
        returns the min number of rigorous tests need for this release cadence
        """
        if self.releases < 6:
            return self.releases
        elif self.releases > 12:
            return (self.releases // 3)
        return math.ceil(self.releases / 2)
    
    """
    for the release cadence determine the total cost to run the min required cost
    if there are surplus budget, the budget will be realigned to simgle and rigorous tests
    """
    # def compute_test_needs(self, budget):
    #     simple_needed = self.simple_tests_needed()
    #     print("simple_needed: " + str(simple_needed))
    #     rigorous_needed = self.rigorous_tests_needed()
    #     print("rigorous_needed: " + str(rigorous_needed))
    #     cost = simple_needed * self.simple_cost + rigorous_needed * self.rigorous_cost
    #     surplus = budget - cost
    #     print(surplus)
    #     if surplus >= self.rigorous_cost:
    #         # ----------
    #         more = surplus // (self.rigorous_cost - self.simple_cost)
    #         print("more: "+ str(more))
    #         more = more if more <= simple_needed else simple_needed
    #         # ----------
    #         simple_needed -= more
    #         rigorous_needed += more
    #         cost = simple_needed * self.simple_cost + rigorous_needed * self.rigorous_cost
    #     result = "Meets" if surplus >= 0 else "Fails"
    #     print(f"{self.cadence:10} : Simple= {simple_needed:3.0f}, Rigorous= {rigorous_needed:3.0f}, " +\
    #           f"Cost ${cost:9.2f}, Surplus {surplus:9.2f}, {result:5}")
    #     return surplus
    def compute_test_needs(self, budget):
        simple_needed   = self.simple_tests_needed()
        rigorous_needed = self.rigorous_tests_needed()
        cost = simple_needed * self.simple_cost + rigorous_needed * self.rigorous_cost
        surplus = budget - cost
        
        print(simple_needed)
        print(rigorous_needed)
        print(cost)
        print(surplus)

        upgrade_cost = self.rigorous_cost - self.simple_cost
        if (surplus >= self.rigorous_cost):
            more = surplus // upgrade_cost
            more = min(more, simple_needed)
            simple_needed   -= more
            assert simple_needed >= 0
            rigorous_needed += more
            cost = simple_needed * self.simple_cost + rigorous_needed * self.rigorous_cost
            surplus = budget - cost
        result = 'Meets' if surplus >= 0 else 'Fails'
        print(f"{self.cadence:10} : Simple= {simple_needed:3.0f}, Rigorous= {rigorous_needed:3.0f}, " +\
            f"Cost ${cost:9.2f}, Surplus {surplus:9.2f}, {result:5}")
        return surplus


# import unittest

# class TestReleaseTestCadence(unittest.TestCase):
#     def setUp(self):
#         self.rtc = ReleaseTestCadence()

#     def test_rtc(self):
#         self.assertEqual(self.bs.rtc("BIWEEKLY", 24, 2000.0, 6000.0), "true")
        


# if __name__ == "__main__":
#     unittest.main()

bi_weekly = ReleaseTestCadence("BIWEEKLY", 24, 2000.0, 6000.0)
monthly = ReleaseTestCadence("MONTHLY", 11, 2500.0, 80000.0)
bi_monthly = ReleaseTestCadence("BIMONTHLY", 6, 0.0, 12000.0)
quarterly = ReleaseTestCadence("QUARTERLY", 4, 0.0, 22000.0)

bi_weekly.compute_test_needs(240000.00)
monthly.compute_test_needs(240000.00)
bi_monthly.compute_test_needs(240000.00)
quarterly.compute_test_needs(240000.00)
