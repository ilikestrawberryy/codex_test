import os

try:
    import openai
except ImportError:
    raise ImportError('openai package is required to run this script')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY environment variable is not set")

openai.api_key = OPENAI_API_KEY

def generate_code(prompt: str) -> str:
    """Use Codex to generate code from a natural language prompt."""
    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        temperature=0.2,
        max_tokens=64,
    )
    return response.choices[0].text.strip()

def explain_code(code: str) -> str:
    """Use Codex to explain the given code snippet."""
    messages = [
        {"role": "system", "content": "You are a helpful programming assistant."},
        {"role": "user", "content": f"다음 파이썬 코드를 설명해줘:\n{code}"},
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2,
    )
    return response.choices[0].message["content"].strip()

if __name__ == "__main__":
    prompt = "파이썬으로 'Hello Codex' 문자열을 출력하는 코드를 작성해줘"
    generated = generate_code(prompt)
    print("[Generated code]\n", generated, "\n")

    explanation = explain_code(generated)
    print("[Explanation]\n", explanation)
