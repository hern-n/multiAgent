from groq import Groq
import dotenv

dotenv.load_dotenv()

class GroqAgent:

    def __init__(self):
        self.client = Groq()

    def generate(self, question):
        completion = self.client.chat.completions.create(
            model="moonshotai/kimi-k2-instruct-0905",
            messages=[
            {
                "role": "user",
                "content": question
            }
            ],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=1,
            stream=True,
            stop=None
        )

        for chunk in completion:
            yield chunk.choices[0].delta.content or ""

    def test(self):

        return self.generate("Fibbonazi en python")

if __name__ == "__main__":
    groqAgent = GroqAgent()
    
    for chunk in groqAgent.test():
        print(chunk, end="")
    print("\n")