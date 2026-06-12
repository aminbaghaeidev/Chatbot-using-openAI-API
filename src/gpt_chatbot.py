from openai import OpenAI, APIStatusError, RateLimitError


def chatbot(user_message: str, api: str) -> str:
    """Receives a message and returns a response using ChatGPT's API.

    :return: response or error
    """

    try:
        client = OpenAI(
            api_key=api
        )

        response = client.responses.create(
            model="gpt-5.4-mini",
            input=user_message,
            store=True
        )
        return response.output_text

    except RateLimitError:
        print("Error your API reached the limit! Try another one.")

    except APIStatusError as e:
        if e.status_code in [401, 403]:
            print(e.body)

    return "Your API key is unavailable. :( Try again later."


if __name__ == '__main__':
    API = "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"
    print(chatbot('Hello!', api=API))
