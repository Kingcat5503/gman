# govman/cli.py
import typer
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch

app = typer.Typer()
MODEL_NAME = "bitnet/bigcode-bitnet"

def get_device():
    return "cuda" if torch.cuda.is_available() else "cpu"

@app.command()
def explain(
    query: str = typer.Argument(..., help="Command or question to explain"),
    model_name: str = typer.Option(MODEL_NAME, help="HuggingFace model name"),
    device: str = typer.Option(get_device(), help="Device: cpu or cuda")
):
    """Explain a command using an AI model."""
    try:
        pipe = pipeline(
            "text-generation",
            model=model_name,
            tokenizer=model_name,
            device=0 if device == "cuda" else -1,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )
        result = pipe(query, max_new_tokens=80)[0]["generated_text"]
        typer.secho(result, fg=typer.colors.WHITE)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)

if __name__ == "__main__":
    app()
