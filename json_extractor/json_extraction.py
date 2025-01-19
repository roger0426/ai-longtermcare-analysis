import json
from pathlib import Path
import asyncio

from json_repair import repair_json
from json_extractor.openai_client import AzureOpenAIClient
from json_extractor.prompt import example_prompt, extraction_prompt
from json_extractor.utils import read_json_template, read_raw_data, save_json_result


def get_templates(template_dir: str = "templates") -> dict[str, dict]:
    current_dir = Path(__file__).parent
    template_dir = (current_dir / template_dir).resolve()

    if not template_dir.exists():
        raise FileNotFoundError(f"Template directory not found: {template_dir}")
    if not template_dir.is_dir():
        raise NotADirectoryError(f"Template path is not a directory: {template_dir}")
        
    return {
        template_path.stem: read_json_template(template_path)
        for template_path in template_dir.iterdir()
        if template_path.suffix == ".json"
    }


def get_raw_data(raw_data_path: str = "raw_data.txt") -> str:
    current_dir = Path(__file__).parent
    raw_data_path = (current_dir / raw_data_path).resolve()
    raw_data = read_raw_data(raw_data_path)
    return raw_data


async def extract_json(
    raw_data: str | Path,
    template_dir: str = "templates",
    example: str = example_prompt.DOCLING_EXAMPLE,
    output_dir: str = "outputs",
) -> dict:
    llm_client = AzureOpenAIClient()
    templates = get_templates(template_dir)
    if isinstance(raw_data, Path):
        raw_data = get_raw_data(raw_data)
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)

    async def process_template(template_name: str, template: dict) -> tuple[str, dict]:
        print(f"Extracting JSON format data from section {template_name}")
        system_prompt = extraction_prompt.SYSTEM_PROMPT
        user_prompt = extraction_prompt.USER_PROMPT.format(
            example=example, raw_data=raw_data, template=template
        )
        response = await llm_client.request(system_prompt, user_prompt)
        repaired_response = repair_json(response, return_objects=True)

        output_path = output_dir / f"{template_name}.json"
        save_json_result(output_path, repaired_response)
        
        return template_name, repaired_response

    # Process all templates in parallel
    tasks = [
        process_template(template_name, template)
        for template_name, template in templates.items()
    ]
    results = await asyncio.gather(*tasks)
    
    # Convert results list to dictionary
    return dict(results)


async def main() -> None:
    raw_data_path = "raw_data.txt"
    await extract_json(raw_data_path)


if __name__ == "__main__":
    asyncio.run(main())
