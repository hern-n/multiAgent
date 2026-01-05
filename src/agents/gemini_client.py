from google import genai
import os
import dotenv


class GeminiAgent:
    def __init__(self):
        dotenv.load_dotenv()
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def generate(self, question):
        response = self.client.models.generate_content_stream(
            model="gemini-2.5-flash", contents=question
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text

    def test(self):
        return self.generate("Fibbonacci en python")

    def __str__(self):
        return "Agent gemini-2.5-flash from Gemini"


geminiAgent = GeminiAgent()

if __name__ == "__main__":

    print(str(geminiAgent))
    print("\n" * 2)

    for chunk in geminiAgent.test():
        print(chunk, end="")
    print("\n")