from playwright.sync_api import sync_playwright
import pandas as pd
from datetime import datetime
import os
import tkinter as tk
from tkinter import ttk, messagebox

OUTPUT_FILE = "gia_vang_pnj.xlsx"

def fetch_pnj_playwright():
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://www.pnj.com.vn/site/gia-vang")

            page.wait_for_selector("table")
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
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi lấy dữ liệu: {e}")
            return pd.DataFrame()

def save_to_excel(df, filename=OUTPUT_FILE):
    try:
        if os.path.exists(filename):
            old_df = pd.read_excel(filename)
            new_df = pd.concat([old_df, df], ignore_index=True)
        else:
            new_df = df

        full_path = os.path.abspath(filename)
        
        new_df.to_excel(filename, index=False)
        messagebox.showinfo("complete", f"Save file in: \n{full_path}")
    except Exception as e:
        messagebox.showerror("error", f"loi luu tep: {e}")

def run_scraper():

    df = fetch_pnj_playwright()
    if df.empty:
        messagebox.showinfo("Thông báo", "kh lay duoc data ")
    else:
        save_to_excel(df)

def create_gui():

    root = tk.Tk()
    root.title("Công cụ lấy giá vàng PNJ")
    root.geometry("400x200")

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(expand=True, fill="both")

    label = ttk.Label(main_frame, text="Nhấn nút để lấy giá vàng PNJ và xuất ra tệp Excel.", wraplength=350, font=("Helvetica", 10))
    label.pack(pady=20)

    # Use a bigger, more prominent button
    scrape_button = ttk.Button(main_frame, text="xuất Excel", command=run_scraper)
    scrape_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()