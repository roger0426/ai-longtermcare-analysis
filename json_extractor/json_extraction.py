import json
from pathlib import Path

from openai_client import OpenAIClient
from prompt import example_prompt, extraction_prompt
from utils import read_json_template, read_raw_data, save_json_result


def get_template():
    template_dir = Path('templates')
    template_filename = 'template_i.json'
    template_path = template_dir / template_filename
    template = read_json_template(template_path)
    return template


def get_raw_data():
    raw_data_path = Path('raw_data.txt')
    raw_data = read_raw_data(raw_data_path)
    return raw_data


def get_example():
    example = example_prompt.DOCLING_EXAMPLE
    return example


def main():
    llm_client = OpenAIClient()
    template = get_template()
    raw_data = get_raw_data()
    example = get_example()
    system_prompt = extraction_prompt.SYSTEM_PROMPT
    user_prompt = extraction_prompt.USER_PROMPT.format(example=example,
                                                       raw_data=raw_data,
                                                       template=template)
    response = llm_client.request(system_prompt, user_prompt)
    print(response)
    save_json_result(Path('output.json'), json.loads(response))


if __name__ == '__main__':
    main()
