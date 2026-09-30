import os
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self, model_name="gemini-pro"):
        self.api_key = os.getenv("GEMINI_API_KEY")

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        # Parties விவரங்களை பிரித்தல்
        party_list = [p.strip() for p in parties.split(",") if p.strip()]
        provider = party_list[0] if len(party_list) > 0 else "Jane Doe (Service Provider)"
        client = party_list[1] if len(party_list) > 1 else "TechNova Inc. (Client)"

        # Terms & Conditions விவரங்களை பிரித்தல்
        term_items = [t.strip() for t in terms.split(";") if t.strip()]
        services_text = term_items[0] if len(term_items) > 0 else "The Service Provider agrees to deliver the designated project milestones."
        payment_text = term_items[1] if len(term_items) > 1 else "Payment shall be cleared within 7 days of invoice."
        ip_text = term_items[2] if len(term_items) > 2 else "All intellectual property rights belong solely to the Client."

        # ஸ்கிரீன்ஷாட்டில் உள்ள அச்சு அசலான வடிவம்
        doc = f"""## {document_type}

I AM EDITING THIS DOCUMENT

Agreement made this {dates}

Between:

{provider}, residing at [Service Provider Address, City, State, Zip Code]

And:

{client}, a corporation organized and existing under the laws of [State of Incorporation], with its principal place of business at [Client Address, City, State, Zip Code].

WITNESSETH:

WHEREAS, the Client desires to engage the Service Provider to perform certain services as described herein; and

WHEREAS, the Service Provider is willing to perform such services for the Client on the terms and conditions set forth in this Agreement;

NOW, THEREFORE, in consideration of the mutual covenants and promises contained herein, the parties agree as follows:

1. Services:
{services_text}

2. Term and Termination:
This Agreement shall commence on the Effective Date and shall terminate upon the completion of the Services as defined in Section 1, or upon mutual written agreement.

3. Payment:
{payment_text}

4. Intellectual Property Rights:
{ip_text}

5. Confidentiality:
The Service Provider agrees to preserve the confidentiality of all proprietary Client information.

6. Independent Contractor Status:
The Service Provider is an independent contractor and not an employee of the Client.

7. Governing Law:
This Agreement shall be governed by and construed in accordance with the laws of the State.

8. Entire Agreement:
This Agreement constitutes the entire understanding between the parties with respect to the subject matter hereof.

9. Severability:
If any provision of this Agreement is held to be invalid or unenforceable, the remaining provisions shall remain in full force and effect.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the Effective Date.


________________________________________
{provider}

[Authorized Representative Signature]

[Authorized Representative Title]

________________________________________
{client}
"""
        return doc