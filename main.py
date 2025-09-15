from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
import os

OUTPUT_FILE = "gia_vang_pnj.xlsx"

def fetch_pnj_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.pnj.com.vn/site/gia-vang")

        page.wait_for_selector("table")  # chờ bảng hiện ra
        rows = page.query_selector_all("table tr")

        data = []
        for row in rows:
            cols = [c.inner_text().strip() for c in row.query_selector_all("td")]
            if cols:
                data.append(cols)

        browser.close()

        if not data:
            return pd.DataFrame()
        df = pd.DataFrame(data, columns=["loai vang", "mua vao", "ban ra"])
        df["nguon"] = "PNJ"
        df["days"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        return df

def save_to_excel(df, filename=OUTPUT_FILE):
    if os.path.exists(filename):
        old_df = pd.read_excel(filename)
        new_df = pd.concat([old_df, df], ignore_index=True)
    else:
        new_df = df
    new_df.to_excel(filename, index=False)
    print(f"save file in {filename}")

def main():
    df = fetch_pnj_playwright()
    if df.empty:
        print("cannot have data of PNJ")
    else:
        print(df)
        save_to_excel(df)

if __name__ == "__main__":
    main()
