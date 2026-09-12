from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8000/cubeit/"


def test_cube(page: Page):
    page.goto(BASE_URL)

    enter_number = page.get_by_placeholder("enter number...")
    cube_btn = page.get_by_role("button", name="Cube")
    result = page.locator("div.result-container#resultDisplay")

    enter_number.fill("5")
    cube_btn.click()

    expect(result).to_contain_text("125")


def test_empty(page: Page):
    page.goto(BASE_URL)

    enter_number = page.get_by_placeholder("enter number...")
    cube_btn = page.get_by_role("button", name="Cube")
    result = page.locator("div.result-container#resultDisplay")

    enter_number.fill("")
    cube_btn.click()

    expect(result).to_contain_text("Enter something!")