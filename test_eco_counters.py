
import pytest
import asyncio
from playwright.async_api import async_playwright

site = "https://www.avito.ru/avito-care/eco-impact"
eco_counters_xpath = "//div[contains(@class,'desktop-impact-item')]"					   

async def main():
	for i in range(2,7,2):
		async with async_playwright() as p:
			browser = await p.chromium.launch()
			page = await browser.new_page()
			await page.goto(site)
			await page.wait_for_load_state("domcontentloaded")
			xpath_i = eco_counters_xpath+'['+str(i)+']'
			await page.locator(xpath_i).screenshot(path=f'output/eco_counter_{i//2}.png')
			await browser.close()

asyncio.run(main())