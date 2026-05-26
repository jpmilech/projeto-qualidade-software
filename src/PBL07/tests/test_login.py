from playwright.sync_api import expect
from src.PBL07.pages.login_page import LoginPage
def test_login(page):

    login = LoginPage(page)

    login.acessar()

    login.realizar_login(
        "joaoEats@gmail.com",
        "joao123"
    )

    expect(page).to_have_url(
    "https://local-eats-unisenac.vercel.app/static/index.html"
    )


# código gerado pelo playwright codegen, antes de ser refatorado

#import re
#from playwright.sync_api import Playwright, sync_playwright, expect


#def run(playwright: Playwright) -> None:
#    browser = playwright.chromium.launch(headless=False)
#    context = browser.new_context()
#    page = context.new_page()
#    page.goto("https://local-eats-unisenac.vercel.app/static/login.html")
#    page.get_by_role("textbox", name="teste@teste.com").click()
#    page.get_by_role("textbox", name="teste@teste.com").fill("joao")
#    page.get_by_role("textbox", name="teste@teste.com").press("CapsLock")
#    page.get_by_role("textbox", name="teste@teste.com").fill("joaoE")
#    page.get_by_role("textbox", name="teste@teste.com").press("CapsLock")
#    page.get_by_role("textbox", name="teste@teste.com").fill("joaoEats@gmail.com")
#    page.get_by_role("textbox", name="Sua senha secreta").click()
#    page.get_by_role("textbox", name="Sua senha secreta").fill("joao123")
#    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    # ---------------------
#    context.close()
#    browser.close()


#with sync_playwright() as playwright:
#    run(playwright) 