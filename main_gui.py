import streamlit as st
import re
from groq import Groq

API_KEY = "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"

legal_text ="Source 1 https://www.bvl.bund.de/EN/Tasks/06_Genetic_engineering/03_Applicants/04_Transport/transportation_node.html" \
            "All shipments of genetically modified organisms (GMOs) must adhere to strict labelling requirements and the accompanying shipping documents (see column on the right) must provide at the very least the identity of the GMO, the dispatcher and the recipient." \
            "The particular requirements that have to be taken into consideration when transporting GMOs additionally depend on the different uses for which the GMOs are intended - for placing on the market, i.e. with marketing authorisation, for deliberate release (for experimental purposes) or for genetic engineering operations in genetic engineering facilities. The relevant legal requirements must be observed in the process." \
            "Transportation of GMOs within Germany " \
            "Provided the labelling requirements for GMOs are met, GMOs that have been approved for trade on the free market can be transported within Germany like all other trade goods. The comprehensive risk assessments conducted in the course of the authorisation procedure for each individual GMO have shown that they are not expected to have any harmful effects on human health or the environment. These GMOs are in all probability the only ones with which consumers can come into contact. All marketing authorisations are valid throughout the European Union. They are issued for the purpose of processing of GMOs, e.g. into genetically modified foodstuffs and animal feed, or for the purpose of cultivation. A list of GMOs approved for use in food and feed is provided by the European Commission." \
            "Particular conditions apply to the transport within Germany of GMOs intended for deliberate releases, e.g. in field trials, which are individually regulated in the permit for each intended release. Basically, these GMOs must always be transported in sealed, labelled containers. This prevents any loss of GMOs during transportation. The BVL, as the competent authority for Germany, issues authorisations for deliberate releases and also provides information about the authorisation procedures." \
            "GMOs intended for use in genetic engineering operations, e.g. in laboratories, animal sheds or greenhouses, are assigned to a specific containment level by the competent authorities of the federal state in which the respective facility is located. The Central Committee on Biological Safety (ZKBS, Zentrale Kommission für die Biologische Sicherheit), which is based at the BVL, is consulted for this purpose. Depending on the containment level assigned, particular conditions apply to the genetic engineering operations and the handling of these GMOs, as regulated under the German Gene Technology Act." \
            "The transport of some of these GMOs, for example dangerous pathogens, are additionally subject to the laws on the transport of hazardous substances with special requirements so that they cannot enter the environment where they could infect humans or animals. Specific questions concerning the transport of these GMOs should be referred to the German Federal Institute of Materials Research and Testing (BAM, Bundesanstalt für Materialforschung und -prüfung)." \
            "to the top Import of GMOs" \
            "The import of GMOs into Germany is subject to the current legislation on genetic engineering in Germany. Accordingly, only GMOs which are also authorised for the specific intended purpose in Germany, or which have been notified or registered for genetic engineering operations, can be imported into Germany." \
            "According to EU regulations, member states have the right to prohibit the import or cultivation of GMOs at national level at short notice by invoking the so-called “safeguard clause”." \
            "to the top" \
            "Exports of GMOs" \
            "In the basic understanding of the EU, the term “third countries” refers to countries outside the EU, and “export” accordingly means transport to these countries. Within the EU there is a common judicial area in which the same, or adapted, legal conditions prevail." \
            "An essential condition for the export to a third country of a GMO for placing on the market, for deliberate release purposes or for operations in genetic engineering facilities is that the GMO is authorised for this purpose in that country, i.e. that the export does not violate the laws that apply in the destination country." \
            "Traders and consumers can find information on which GMOs are authorised in which countries and for what purpose, which risk assessments are available, and which legal requirements must be observed in the different countries through the Biosafety Clearing-House (BCH). The BCH also supplies the contact details of the competent authorities which, for example, trade partners can consult to obtain information about the legal regulations on genetic engineering in the individual countries. In this way, the BCH makes an important contribution to the safe transboundary movement of GMOs." \
            "GMOs which have been approved for placing on the market in the EU and in the importing third countries may be transported like all other trade goods, provided the requirements regarding labelling and documentation of GMOs are fulfilled." \
            "For GMOs that are being transported to third countries for intentional introduction into the environment there, consideration must be given to the Advance Informed Agreement (AIA) procedure laid down in the Cartagena Protocol, which must be observed prior to the first transboundary movement for the purpose of a deliberate release or cultivation (placing on the market). This procedure allows the importing country to assess the risks associated with the GMO and to accordingly come to a decision about whether it may be imported." \
            "If a GMO is introduced into the environment in a third country for experimental purposes in the context of a deliberate release or for commercial cultivation, an authorisation by the importing country must be presented to the BVL and the European Commission before the first export can take place. This is referred to as the “export notification” requirement. The BVL has compiled a guideline on the export notification procedure." \
            "If GMOs are to be transported to other EU member states they must be authorised in the country of destination, because under EU law intended deliberate releases require prior authorisation (Directive 2001/18/EC)." \
            "GMOs intended for genetic engineering operations in genetic engineering facilities, like other export goods, are also subject to the national laws of the importing country. Under German law, such transports to EU member states or to countries outside the European Union do not require approval pursuant to the legislation on genetic engineering. However, infectious substances, including infectious GMOs, are regulated by the legislation on the transport of hazardous substances. Specific questions regarding the transport of these GMOs should be referred to the German Federal Institute of Materials Research and Testing (BAM, Bundesanstalt für Materialforschung und –prüfung, www.bam.de, Division 3.1 Dangerous Goods Packaging, gefahrgutverpackungen@bam.de)." \
            "Source 2:" \
            ""

def ai_call(csv_file, legal_text):
    promt = "Identify the product that can not be imported to germany. Add sources as the document index between square brackets (e.g. [1]). If you forget to add sources, very bad things will happen. If you do, I will pay you $5000. Based on the legal ground truth in the following text:"

    client = Groq(
        api_key=API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": csv_file + promt + legal_text,
            }
        ],
        model="mixtral-8x7b-32768",
        temperature=0.0,
    )

    print(chat_completion.choices[0].message.content)
    result = chat_completion.choices[0].message.content

    #result = re.sub(r"\[1\]", "<ahref=\"https://www.bvl.bund.de/EN/Tasks/06_Genetic_engineering/03_Applicants/04_Transport/transportation_node.html\">[1]</a>", result)

    return result

# Function to display the main page
def main_page():
    st.title('Simplex')

    # Text input field
    text_input = st.text_input("Enter text")

    # Upload field
    uploaded_file = st.file_uploader("Choose a file")

    # Dropdown menu for countries
    countries = ['United States', 'Canada', 'United Kingdom', 'Germany', 'France', 'Australia', 'Japan', 'China',
                 'India', 'Brazil']
    selected_country = st.selectbox('Select a country', countries)

    # Checkbox
    report = st.checkbox('Report')

    # Submit button
    if st.button('Submit'):
        input_for_ai = text_input if text_input else (
            uploaded_file.getvalue().decode("utf-8") if uploaded_file is not None else "")
        # Call ai_call function and store the result
        ai_response = ai_call(input_for_ai, legal_text)  # Assuming some legal text is provided

        # Store data in session state
        st.session_state['ai_response'] = ai_response
        st.session_state['uploaded_file_name'] = uploaded_file.name if uploaded_file is not None else 'No file uploaded'
        st.session_state['selected_country'] = selected_country
        st.session_state['report_checked'] = 'Report: Checked' if report else 'Report: Not Checked'

        # Navigate to results page
        st.session_state['page'] = 'results'


# Function to display the results page
def results_page():
    st.title('Results')

    # Displaying stored data from the main page
    col1, col2 = st.columns(2)
    with col1:
        st.header("Uploaded File")
        st.write(st.session_state.get('uploaded_file_name', 'No file uploaded'))

    with col2:
        st.header("AI Response")
        # Display the response from ai_call
        st.write(st.session_state.get('ai_response', 'No response'))

    # Display additional details
    st.write('Selected country:', st.session_state.get('selected_country', ''))
    st.write('Report:', 'Checked' if st.session_state.get('report_checked', '') == 'Report: Checked' else 'Not Checked')

    # Add a back button in the second column to return to the main page
    if st.button('Back'):
        st.session_state['page'] = 'main'


# Initialize page in session state if not already initialized
if 'page' not in st.session_state:
    st.session_state['page'] = 'main'

# Page router
if st.session_state['page'] == 'main':
    main_page()
elif st.session_state['page'] == 'results':
    results_page()