import openai
def generate_email_content(prompt, company_name, location, products):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt.format(company_name=company_name, location=location, products=products),
        max_tokens=150
    )
    return response.choices[0].text.strip()

