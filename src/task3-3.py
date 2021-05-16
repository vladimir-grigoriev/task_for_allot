import time
import unittest

from selenium import webdriver

import additional_functions.funcs_for_task_33 as funcs


LINK = "https://www.metric-conversions.org"


class TestMetricConversions(unittest.TestCase):
    """Tests for www.metric-conversions.org."""

    def test_celsius_to_fahrenheit(self) -> None:
        """
        Test for converting Celsius to Fahrenheit temperature.
        """
        values_to_convert = [25, -25, 0, 110, 1, 300, 10000]

        try:
            browser = webdriver.Chrome()
            browser.get(LINK)

            browser.find_element_by_css_selector(
                "a[title='Temperature Conversion']"
            ).click()
            time.sleep(1)

            browser.find_element_by_xpath(
                "/html/body/div[1]/div[3]/ol/li[1]/a"
            ).click()
            time.sleep(1)

            for value in values_to_convert:
                input1 = browser.find_element_by_id("argumentConv")
                input1.clear()
                input1.send_keys(value)
                input1.submit()
                time.sleep(1)

                answer_field = browser.find_element_by_id("answer").text
                result = float(answer_field.split(" ")[1].replace("°F", ""))

                self.assertAlmostEqual(funcs.celsius_to_fahrenheit(value), result, 3)

        finally:
            time.sleep(1)
            browser.quit()

    def test_meters_to_feet(self) -> None:
        """Test for converting meters to feet."""

        values_to_convert = [25, -25, 0, 110, 1, 300, 10000]

        try:
            browser = webdriver.Chrome()
            browser.get(LINK)

            browser.find_element_by_css_selector(
                "a[title='Length Conversion']"
            ).click()
            time.sleep(1)

            browser.find_element_by_xpath(
                "/html/body/div[1]/div[3]/ol/li[1]/a"
            ).click()
            time.sleep(1)

            for value in values_to_convert:
                input1 = browser.find_element_by_id("argumentConv")
                input1.clear()
                input1.send_keys(value)
                input1.submit()
                time.sleep(1)

                browser.find_element_by_class_name("controlOptions").click()
                browser.find_element_by_xpath(
                    "/html/body/div[1]/div[1]/section[2]/div[2]/select/option[2]"
                ).click()
                time.sleep(1)

                answer_field = browser.find_element_by_id("answer").text
                result = float(answer_field.split(" ")[1].replace("ft", ""))

                self.assertAlmostEqual(funcs.meters_to_feet(value), result, 2)

        finally:
            time.sleep(1)
            browser.quit()

    def test_ounces_to_grams(self) -> None:
        """Tests for converting ounces to grams."""

        values_to_convert = [25, -25, 0, 40, 100, 10000]

        try:
            browser = webdriver.Chrome()
            browser.get(LINK)

            browser.find_element_by_css_selector(
                "a[title='Weight Conversion']"
            ).click()
            time.sleep(1)

            browser.find_element_by_xpath(
                "/html/body/div[1]/div[3]/ol/li[5]/a"
            ).click()
            time.sleep(1)

            for value in values_to_convert:
                input1 = browser.find_element_by_id("argumentConv")
                input1.clear()
                input1.send_keys(value)
                input1.submit()
                time.sleep(1)

                answer_field = browser.find_element_by_id("answer").text
                result = float(answer_field.split(" ")[1].replace("g", ""))

                self.assertAlmostEqual(funcs.ounces_to_grams(value), result, 2)

        finally:
            time.sleep(1)
            browser.quit()


if __name__ == "__main__":
    unittest.main()
