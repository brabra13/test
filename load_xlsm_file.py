import marimo

__generated_with = "0.3.4"
app = marimo.App(width="medium")


@app.cell
def __():
    import pyodide
    import micropip
    return micropip, pyodide


@app.cell
def __():
    import pandas as pd
    return pd,


@app.cell
def __():
    from pyodide.http import pyfetch
    import asyncio
    from io import BytesIO
    import base64
    return BytesIO, asyncio, base64, pyfetch


@app.cell
async def __(micropip):
    await micropip.install("openpyxl")
    from openpyxl import load_workbook
    return load_workbook,


@app.cell
def __(platform):
    current_os = platform.system()
    return current_os,


@app.cell
async def __(current_os, micropip):
    await micropip.install('PyGithub')
    if current_os == "Emscripten":
        await micropip.install("ssl")
    return


@app.cell
def __():
    import urllib3
    urllib3.disable_warnings()
    return urllib3,


@app.cell
def __():
    # await micropip.install('PyGithub')
    return


@app.cell
def __():
    from github import Github
    return Github,


@app.cell
def __():
    import platform
    return platform,


@app.cell
def __():
    import io
    from typing import Optional
    return Optional, io


@app.cell
def __():
    # # loading csv file from git 

    # url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"

    # current_os = platform.system()

    # if current_os == "Emscripten":
    #     print("This code is running in a WebAssembly environment.")
    #     df = pd.read_csv(pyodide.http.open_url(url))
    # else:
    #     print("This code is not running in a WebAssembly environment.")
    #     df = pd.read_csv(url)
    return


@app.cell
def __(Github, base64, io, pd):

    login_or_token = "d415979c9c185692e4234824000b07281bc2553f"
    g = Github(base_url="https://scegithub.apps.carrier.com/api/v3", login_or_token=login_or_token)
    repo = g.get_repo("EMEA-MBD/marimo_notebooks")
    sha_file  = "7199e37bc550e22393ba63400eeff7c467393f56"
    blob = repo.get_git_blob(sha_file)

    # contents = repo.get_contents("./", ref="master")
    # for content in contents:
    #     print(f"SHA du fichier : {content.sha} {content.name}")

    binary_data = base64.b64decode(blob.content)
    # with open("test.xlsm", "wb") as f:
    #     f.write(contenu_fichier)
    xlsx_path = io.BytesIO(binary_data)
    excel_file = pd.ExcelFile(xlsx_path)
    pd.read_excel(excel_file) 
    return (
        binary_data,
        blob,
        excel_file,
        g,
        login_or_token,
        repo,
        sha_file,
        xlsx_path,
    )


@app.cell
def __():
    return


@app.cell
def __():
    # # loading XLSM file from git 

    # async def fetch(url: str) -> Optional[bytes]:
    #     try:
    #         response = await pyodide.http.pyfetch(url)
    #         if response.ok:
    #             return await response.blob()
    #     except Exception as e:
    #         print("Error while fetching:", url, ":", e)
    #     return None

    # async def get_dataframe_from_url(url: str) -> Optional[pd.DataFrame]:
    #     loop = asyncio.get_event_loop()
    #     coroutine = await fetch(url)
    #     raw_binary = loop.run_until_complete(coroutine)

    #     if not raw_binary:
    #         return None

    #     df = pd.read_excel(io.BytesIO(raw_binary), engine='openpyxl')
    #     return df


    # df_xlsx = get_dataframe_from_url('https://github.com/brabra13/Pressure-Swing-Adsorption/raw/main/test.xlsx')

    # if df_xlsx is not None:
    #     print("Successfully read Excel file from URL.")
    # else:
    #     print("Failed to read Excel file from URL.")
    return


@app.cell
def __():
    # # loading XLSM file from git 
    # from urllib3.util import Retry
    # async def fetch(url: str) -> Optional[bytes]:
    #     try:
    #         response = await pyodide.http.pyfetch(url)
    #         if response.ok:
    #             return await response.bytes()
    #     except Exception as e:
    #         print("Error while fetching:", url, ":", e)
    #     return None

    # async def get_dataframe_from_url() -> Optional[pd.DataFrame]:
    #     loop = asyncio.get_event_loop()
    #     # You can use a CORS proxy to get around CORS issues
    #     g = Github(base_url="https://corsproxy.io/?https://scegithub.apps.carrier.com/api/v3", 
    #                login_or_token="d415979c9c185692e4234824000b07281bc2553f",
    #                retry=Retry(10))
    #     repo = g.get_repo("EMEA-MBD/marimo_notebooks")
    #     sha_du_fichier  = "c63e4c113b6ce6f1dbaa2c812688340ae33816b8"
    #     blob = repo.get_git_blob(sha_du_fichier)
    #     raw_binary = await fetch(blob.url + '/test_fetch.xlsx')
    #     print(blob.url + '/test_fetch.xlsx')
    #     print(raw_binary)
    #     #raw_binary = loop.run_until_complete(coroutine)

    #     if not raw_binary:
    #         return None

    #     df = pd.read_excel(io.BytesIO(raw_binary), engine='openpyxl')
    #     return df

    # df_xlsx = await get_dataframe_from_url()

    # if df_xlsx is not None:
    #     print("Successfully read Excel file from URL.")
    # else:
    #     print("Failed to read Excel file from URL.")
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
