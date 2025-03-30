import json
import os
import re
from typing import List, Tuple

import fire
import httpx
from bs4 import BeautifulSoup


def extract_io_list_from_text(text: str) -> List[Tuple[str, str]]:
    input_pattern = r"####.*?入力例.*?\d.*?\n```IOExample.*?\n([\s\S]*?)```"
    input_results = [re.sub(r"\s*?\r", "", r) for r in re.findall(input_pattern, text)]

    output_pattern = r"####.*?出力例.*?\d.*?\n```IOExample.*?\n([\s\S]*?)```"
    output_results = [
        re.sub(r"\s*?\r", "", r) for r in re.findall(output_pattern, text)
    ]

    # 入力例がない場合は空のリストを返す
    if len(input_results) == 0:
        return []

    if len(input_results) != len(output_results):
        raise Exception("Failed to extract input/output from text")
    return [
        # if output_results is only '\n', result is blank.
        (input_result, output_results[i] if output_results[i] != "\n" else "")
        for i, input_result in enumerate(input_results)
    ]


def extract_problem_from_text(text: str) -> str:
    # 問題文のパターンを修正
    problem_pattern = r"(### ?問題文[\s\S]*?)(?:### |$)"
    problem_result = re.search(problem_pattern, text)

    if problem_result is None:
        raise Exception("Failed to extract problem from text")

    return re.sub(r"\s*?\r", "", problem_result.group(1))


def fetch_question_body(url: str) -> str:
    res = httpx.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.select_one("#__NEXT_DATA__").get_text()
    json_data = json.loads(data)
    body_text = json_data["props"]["pageProps"]["task"]["body"]
    print("Problem body:", body_text)
    return body_text


def get_question(question_number: int) -> None:
    dir_name = f"questions/{str(question_number)}"
    BASE_URL = "https://algo-method.com/tasks"

    body_text = fetch_question_body(f"{BASE_URL}/{question_number}")

    io_list = extract_io_list_from_text(body_text)
    problem_text = extract_problem_from_text(body_text)

    # generate case.json
    os.makedirs(dir_name, exist_ok=True)
    with open(f"{os.path.dirname(__file__)}/../../{dir_name}/case.json", "w") as f:
        json.dump(io_list, f, indent=2)

    # generate main.py
    with open(f"{os.path.dirname(__file__)}/../../{dir_name}/main.py", "w") as f:
        # 入力・出力の例がある場合は記述
        if io_list:
            f.write(
                f'"""\n{BASE_URL}/{str(question_number)}\n\n{problem_text}\n### 入力例\n'
            )
            for i, (input_text, output_text) in enumerate(io_list, 1):
                f.write(f"#### 入力例 {i}\n```IOExample\n{input_text.strip()}\n```\n")
                f.write(f"#### 出力例 {i}\n```IOExample\n{output_text.strip()}\n```\n")
            f.write('"""\n\n')
        else:
            f.write(f'"""\n{BASE_URL}/{str(question_number)}\n\n{problem_text}"""\n\n')

        # 入力が必要な場合はinput()を追加
        if io_list and any(input_text.strip() for input_text, _ in io_list):
            # 入力例の最初の行を見て、スペース区切りの数を確認
            first_input = next(
                input_text.strip() for input_text, _ in io_list if input_text.strip()
            )
            if " " in first_input:
                # スペース区切りの場合
                f.write("N, M = map(int, input().split())\n")
            else:
                # 単一の値の場合
                f.write("N = int(input())\n")
        else:
            f.write('print("Hello Algor-Method!")\n')


if __name__ == "__main__":
    fire.Fire(get_question)
