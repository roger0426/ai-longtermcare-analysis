import json
from pathlib import Path

from json_repair import repair_json
from openai_client import OpenAIClient
from prompt import example_prompt, extraction_prompt
from utils import read_json_template, read_raw_data, save_json_result


def get_templates(template_dir: str = "templates") -> dict[str, dict]:
    template_dir = Path(template_dir)
    return {
        template_path.stem: read_json_template(template_path)
        for template_path in template_dir.iterdir()
        if template_path.suffix == ".json"
    }


def get_raw_data(raw_data_path: str = "raw_data.txt") -> str:
    raw_data_path = Path(raw_data_path)
    raw_data = read_raw_data(raw_data_path)
    return raw_data


def extract_json(
    raw_data_path: str,
    template_dir: str = "templates",
    example: str = example_prompt.DOCLING_EXAMPLE,
    output_dir: str = "outputs",
) -> None:
    llm_client = OpenAIClient()
    templates = get_templates(template_dir)
    raw_data = get_raw_data(raw_data_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    for template_name, template in templates.items():
        print(f"Extracting JSON format data from section {template_name}")
        system_prompt = extraction_prompt.SYSTEM_PROMPT
        user_prompt = extraction_prompt.USER_PROMPT.format(
            example=example, raw_data=raw_data, template=template
        )
        response = llm_client.request(system_prompt, user_prompt)
        repaired_response = repair_json(response, return_objects=True)

        output_path = output_dir / f"{template_name}.json"
        save_json_result(output_path, repaired_response)


def main() -> None:
    raw_data_path = "raw_data.txt"
    extract_json(raw_data_path)


if __name__ == "__main__":
    main()
