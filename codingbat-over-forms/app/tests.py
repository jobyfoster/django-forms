from django.test import SimpleTestCase


# Create your tests here.
class TestFontTimesView(SimpleTestCase):
    def test_hi_3(self):
        response = self.client.get("/font-times/?phrase=Hi&copies=3")
        self.assertContains(response, "HiHiHi")

    def test_there_4(self):
        response = self.client.get("/font-times/?phrase=There&copies=4")
        self.assertContains(response, "TheTheThe")

    def test_hi_3(self):
        response = self.client.get("/font-times/?phrase=d&copies=2")
        self.assertContains(response, "dd")


class TestCenteredAverageView(SimpleTestCase):
    def test_1_2_3_4_100(self):
        response = self.client.get(
            "/centered-average/?num_one=1&num_two=2&num_three=3&num_four=4&num_five=100"
        )
        self.assertContains(response, "3")

    def test_5_5_100_200_7(self):
        response = self.client.get(
            "/centered-average/?num_one=5&num_two=5&num_three=100&num_four=200&num_five=7"
        )
        self.assertContains(response, "37")

    def test_5_3_4_6_2(self):
        response = self.client.get(
            "/centered-average/?num_one=5&num_two=3&num_three=4&num_four=6&num_five=2"
        )
        self.assertContains(response, "4")


class TestXYZThereView(SimpleTestCase):
    def test_phrase_with_xyz(self):
        response = self.client.get("/xyz-there/?phrase=abcxyz")
        self.assertContains(response, "True")

    def test_phrase_with_dot_xyz(self):
        response = self.client.get("/xyz-there/?phrase=abc.xyz")
        self.assertContains(response, "False")

    def test_phrase_with_dot_xyz_and_xyz(self):
        response = self.client.get("/xyz-there/?phrase='abc.xyzxyz")
        self.assertContains(response, "True")


class TestNoTeenSumView(SimpleTestCase):
    def test_all_non_teen_values(self):
        response = self.client.get("/no-teen-sum/", {"a": 5, "b": 3, "c": 8})
        self.assertContains(response, "16")

    def test_some_teen_values(self):
        response = self.client.get("/no-teen-sum/", {"a": 13, "b": 15, "c": 2})
        self.assertContains(response, "17")

    def test_all_teen_values(self):
        response = self.client.get("/no-teen-sum/", {"a": 14, "b": 18, "c": 19})
        self.assertContains(response, "0")

    def test_with_negative_values(self):
        response = self.client.get("/no-teen-sum/", {"a": -1, "b": -5, "c": -10})
        self.assertContains(response, "-16")
