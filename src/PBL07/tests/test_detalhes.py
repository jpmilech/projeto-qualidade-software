from playwright.sync_api import expect

from src.PBL07.pages.login_page import LoginPage
from src.PBL07.pages.home_page import HomePage
from src.PBL07.pages.restaurant_page import RestaurantPage


def test_detalhes(page):

    login = LoginPage(page)

    home = HomePage(page)

    restaurant = RestaurantPage(page)

    login.acessar()

    login.realizar_login(
        "joaoEats@gmail.com",
        "joao123"
    )

    home.abrir_restaurante()

    expect(
        restaurant.validar_restaurante()
    ).to_be_visible()

    expect(
        restaurant.validar_cardapio()
    ).to_be_visible()


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
#    page.get_by_role("textbox", name="teste@teste.com").press("Tab")
#    page.get_by_role("textbox", name="Sua senha secreta").fill("joao123")
#    page.locator("#loginForm").get_by_role("button", name="Entrar").click()
#    page.get_by_role("link", name="Restaurante Sabor 0").click()
#    page.get_by_role("img", name="Restaurant Image").click()
#    page.get_by_role("heading", name="Restaurante Sabor").click()
#    page.get_by_text("Um ótimo lugar para").click()
#    page.get_by_role("heading", name="Prato Especial 0").click()
#    page.locator("div").filter(has_text="Prato Especial 2 Delicioso").nth(3).click()

    # ---------------------
#    context.close()
#    browser.close()


#with sync_playwright() as playwright:
#    run(playwright)