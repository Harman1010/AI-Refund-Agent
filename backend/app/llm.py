import os

from dotenv import load_dotenv

load_dotenv()

provider = os.getenv("LLM_PROVIDER", "groq")


def generate_reply(reason, approved, order_id):

    status = "Approved" if approved else "Denied"

    prompt = f"""
You are an ecommerce customer support chatbot.

Order ID: {order_id}

Refund Status: {status}

Reason: {reason}

Write a short conversational response.

Keep it under 4 sentences.

Do not use letter formatting.
Do not say Dear Customer.
Do not add signatures.
"""

    try:

        if provider == "gemini":

            from google import genai

            client = genai.Client(
                api_key=os.getenv("GEMINI_API_KEY")
            )

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            return response.text

        if provider == "groq":

            from groq import Groq

            client = Groq(
                api_key=os.getenv("GROQ_API_KEY")
            )

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional ecommerce customer support chatbot."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.choices[0].message.content

    except Exception as e:

        print("LLM ERROR:", e)

        if approved:
            return f"""
Your refund request for order {order_id} has been approved.

Reason: {reason}

The refund will be processed shortly.
"""

        return f"""
Your refund request for order {order_id} has been denied.

Reason: {reason}

Please contact support if you believe this decision is incorrect.
"""