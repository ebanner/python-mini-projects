from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()


if __name__ == '__main__':
    #
    # Need to have .env file with OPENAI_API_KEY
    #
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    output = completion.choices[0].message.content
    print(output)
