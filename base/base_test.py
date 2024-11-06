import pytest
from pages.text_box import TextBox
from pages.check_box import CheckBox
from pages.radio_button import RadioButton
from pages.web_tables import WebTables
from pages.buttons import Buttons
from pages.links import Links
from pages.broken_links_images import BrokenLinksImages
from pages.upload_files import UploadFiles
from pages.dynamic_properties import DynamicProperties
from pages.practice_form import PracticeForm
from pages.browser_windows import BrowserWindows
from pages.alerts import Alerts
from pages.frames import Frames
from pages.accordian import Accordian
from pages.auto_complete import AutoComplete


class BaseTest:
    text_box: TextBox
    check_box: CheckBox
    radio_button: RadioButton
    web_tables: WebTables
    buttons: Buttons
    links: Links
    broken_links_images: BrokenLinksImages
    upload_files: UploadFiles
    dynamic_properties: DynamicProperties
    practice_form: PracticeForm
    browser_windows: BrowserWindows
    alerts: Alerts
    frames: Frames
    accordian: Accordian
    auto_complete: AutoComplete

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.text_box = TextBox(driver)
        request.cls.check_box = CheckBox(driver)
        request.cls.radio_button = RadioButton(driver)
        request.cls.web_tables = WebTables(driver)
        request.cls.buttons = Buttons(driver)
        request.cls.links = Links(driver)
        request.cls.broken_links_images = BrokenLinksImages(driver)
        request.cls.upload_files = UploadFiles(driver)
        request.cls.dynamic_properties = DynamicProperties(driver)
        request.cls.practice_form = PracticeForm(driver)
        request.cls.browser_windows = BrowserWindows(driver)
        request.cls.alerts = Alerts(driver)
        request.cls.frames = Frames(driver)
        request.cls.accordian = Accordian(driver)
        request.cls.auto_complete = AutoComplete(driver)
