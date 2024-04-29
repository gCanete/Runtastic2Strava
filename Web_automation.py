import undetected_chromedriver as uc
import time


def web_automation(url) -> str or None:
    options = uc.ChromeOptions()
    options.headless = False
    driver = uc.Chrome(options=options)

    with driver:
        # Go to the target website
        driver.get(url)
        previous_url = driver.current_url
        print(f"Current URL: {previous_url}")

        while True:
            current_url = driver.current_url
            if current_url != previous_url and current_url.startswith('http://localhost/?state=&code='):
                print(f"URL changed to: {current_url}")
                start = "&code="
                end = "&scope"
                code = current_url.split(start)[1].split(end)[0]
                print(code)
                break
            time.sleep(2)  # Wait for 2 seconds before checking if the URL has changed

    driver.close()
    return code




