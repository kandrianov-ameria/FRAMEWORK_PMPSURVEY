#The starting Country select pop-up locators.

class HomePageSelectors:

    homepage_url = "https://syneospmp.ameriadev.de/"

    # The starting country popup selectors.

    country_popup_css = "div[class='fancybox-slide fancybox-slide--current fancybox-slide--html']"
    country_popup_img_css = "img[alt='choose-country'][src='img/chose-country.svg']"
    country_popup_title_xpath = "//div[contains(text(), 'Please select your country/language:')]"
    country_popup_select_css = "select[id='country-select']"
    country_popup_proceedbtn_css = "button[class='btn question__btn btn-chose-country']"
    country_popup_close_css = "button[class='fancybox-button fancybox-close-small']"
    fake_button = "button[class='box-button']"

    # Home page selectors:

    home_page_takepart_btn_css = "a[class='take-part__cta tr-button_start']"
