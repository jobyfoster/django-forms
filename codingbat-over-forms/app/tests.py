from django.test import SimpleTestCase


# Create your tests here.
class TestFontTimesView(SimpleTestCase):
    def test_chocolate_2(self):
        response = self.client.get("/warmup-2/font-times/?phrase=Chocolate&copies=2")
        self.assertContains(response, "ChoCho")

    def test_chocolate_3(self):
        response = self.client.get("/warmup-2/font-times/?phrase=Chocolate&copies=3")
        self.assertContains(response, "ChoChoCho")

    def test_abc_3(self):
        response = self.client.get("/warmup-2/font-times/?phrase=Abc&copies=3")
        self.assertContains(response, "AbcAbcAbc")


class TestCenteredAverageView(SimpleTestCase):
    def test_1_2_3_4_100(self):
        response = self.client.get(
            "/list-2/centered-average/?num_one=1&num_two=2&num_three=3&num_four=4&num_five=100"
        )
        self.assertContains(response, 3)

    def test_1_1_5_5_10_8_7(self):
        response = self.client.get(
            "/list-2/centered-average/?num_one=1&num_two=1&num_three=5&num_four=5&num_five=10&num_six=8&num_seven=7"
        )
        self.assertContains(response, 5)

    def test_neg10_neg4_neg2_neg4_neg2_0(self):
        response = self.client.get(
            "/list-2/centered-average/?num_one=-10&num_two=-4&num_three=-2&num_four=-4&num_five=-2&num_six=0&num_seven="
        )
        self.assertContains(response, -3)


class TestXYZThereView(SimpleTestCase):
    def test_phrase_with_xyz(self):
        response = self.client.get("/string-2/xyz-there/?phrase=abcxyz")
        self.assertContains(response, True)

    def test_phrase_with_dot_xyz(self):
        response = self.client.get("/string-2/xyz-there/?phrase=abc.xyz")
        self.assertContains(response, False)

    def test_phrase_with_dot_xyz_and_xyz(self):
        response = self.client.get("/string-2/xyz-there/?phrase='xyz.abc")
        self.assertContains(response, True)


class TestNoTeenSumView(SimpleTestCase):
    def test_1_2_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=1&b=2&c=3")
        self.assertContains(response, 6)

    def test_2_13_1(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=13&c=1")
        self.assertContains(response, 3)

    def test_2_1_14(self):
        response = self.client.get("/logic-2/no-teen-sum/?a=2&b=1&c=14")
        self.assertContains(response, 3)
