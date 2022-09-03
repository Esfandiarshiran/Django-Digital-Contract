import base64
from datetime import date
from os import path

from docusign_esign import EnvelopesApi, RecipientViewRequest, Document, Signer, EnvelopeDefinition, SignHere, Tabs, \
    Recipients, Text, CarbonCopy, DateSigned

from .consts import authentication_method
from .docusign import create_api_client



class Eg001EmbeddedSigningController:
    @classmethod
    def worker(cls, args):
        """
        1. Create the envelope request object
        2. Send the envelope
        3. Create the Recipient View request object
        4. Obtain the recipient_view_url for the embedded signing
        """
        envelope_args = args["envelope_args"]
        # 1. Create the envelope request object
        envelope_definition = cls.make_envelope(envelope_args)

        # 2. call Envelopes::create API method
        # Exceptions will be caught by the calling function
        api_client = create_api_client(base_path=args["base_path"], access_token=args["access_token"])

        envelope_api = EnvelopesApi(api_client)
        results = envelope_api.create_envelope(account_id=args["account_id"], envelope_definition=envelope_definition)

        envelope_id = results.envelope_id

        # 3. Create the Recipient View request object
        recipient_view_request = RecipientViewRequest(
            authentication_method=authentication_method,
            client_user_id=envelope_args["signer_client_id"],
            recipient_id="1",
            return_url=envelope_args["ds_return_url"],
            user_name=envelope_args["signer_name"],
            email=envelope_args["signer_email"]
        )

        # 4. Obtain the recipient_view_url for the embedded signing
        # Exceptions will be caught by the calling function
        results = envelope_api.create_recipient_view(
            account_id=args["account_id"],
            envelope_id=envelope_id,
            recipient_view_request=recipient_view_request
        )

        return {"envelope_id": envelope_id, "redirect_url": results.url}

    @classmethod
    def make_envelope(cls, args):
        """
        Creates envelope
        args -- parameters for the envelope:
        signer_email, signer_name, signer_client_id
        returns an envelope definition
        """

        # document 1 (pdf) has tag /sn1/
        #
        # The envelope has one recipient.
        # recipient 1 - signer
        # create the envelope definition
        doc1_b64 = base64.b64encode(bytes(cls.create_document(args), "utf-8")).decode("ascii")
        # Create the document models
        document = Document(  # create the DocuSign document object
            document_base64=doc1_b64,
            name="Acknowledgement",  # can be different from actual file name
            file_extension="html",  # many different document types are accepted
            document_id="1"  # a label used to reference the doc
        )

        # Create the signer recipient model
        signer1 = Signer(
            # The signer
            email=args["signer_email"],
            name=args["signer_name"],
            recipient_id="1",
            routing_order="1",
            # Setting the client_user_id marks the signer as embedded
            client_user_id=args["signer_client_id"]
        )

        signer2 = Signer(
            # The signer
            email=args["receiver_email"],
            name=args["receiver_name"],
            recipient_id="2",
            routing_order="2",
        )

        today = date.today()
        curr_date = today.strftime("%d/%m/%y")
        sign_date = DateSigned(
            document_id='1',
            page_number='1',
            recipient_id='1',
            tab_label='Date',
            font='helvetica',
            bold='true',
            value=curr_date,
            tab_id='date',
            font_size='size16',
            y_position='110',
            x_position='350',
        )
        # text_name = Text(
        #     document_id='1',
        #     page_number='1',
        #     recipient_id='1',
        #     tab_label='Name',
        #     font='helvetica',
        #     bold='true',
        #     value=args['signer_name'],
        #     tab_id="name",
        #     font_size="size16",
        #     # y_position='43',
        #     # x_position="363",
        # )
        # text_email = Text(
        #     document_id='1',
        #     page_number='1',
        #     recipient_id='1',
        #     tab_label='Email',
        #     font='helvetica',
        #     bold='true',
        #     value=args['signer_email'],
        #     tab_id="email",
        #     font_size="size16",
        #     y_position='410',
        #     x_position="359",
        # )
        # cc1 = CarbonCopy(
        #     email=args["cc_email"],
        #     name=args["cc_name"],
        #     recipient_id="2",
        #     routing_order="2"
        # )
        sign_here1 = SignHere(
            anchor_string="/sn1/",
            anchor_units="pixels",
            anchor_y_offset="20",
            anchor_x_offset="30",
        )
        sign_here2 = SignHere(
            anchor_string="/**signature_1**/",
            anchor_units="pixels",
            anchor_y_offset="30",
            anchor_x_offset="30",
        )

        # Add the tabs model (including the sign_here tab) to the signer
        # The Tabs object wants arrays of the different field/tab types
        signer1.tabs = Tabs(sign_here_tabs=[sign_here1], text_tabs=[ sign_date])
        signer2.tabs = Tabs(sign_here_tabs=[sign_here2])

        # Next, create the top level envelope definition and populate it.
        envelope_definition = EnvelopeDefinition(
            email_subject="Please sign this document.",
            documents=[document],
            # The Recipients object wants arrays for each recipient type
            recipients=Recipients(signers=[signer1, signer2]),
            status="sent"  # requests that the envelope be created and sent.
        )
        return envelope_definition

    @classmethod
    def create_document(cls, args):
        """ Creates document 1 -- an html document"""

        return f"""
        <!DOCTYPE html>
        <html>
            <head>
              <meta charset="UTF-8">
            </head>
            <body style="font-family:sans-serif;margin-left:2em;">
            <h1 style="font-family: "Trebuchet MS", Helvetica, sans-serif;
                color: darkblue;margin-bottom: 0;">Welcome</h1>
            <h2 style="font-family: "Trebuchet MS", Helvetica, sans-serif;
              margin-top: 0px;margin-bottom: 3.5em;font-size: 1em;
              color: darkblue;">Order Processing Date :</h2>
            <h4>Ordered by : {args["signer_name"]}</h4>
            <p style="margin-top:0em; margin-bottom:0em;">Email: {args["signer_email"]}</p>
            <p style="margin-top:0em; margin-bottom:0em;"> Sent To: {args["receiver_name"]} & Email : {args["receiver_email"]}</p>
            <p style="margin-top:3em;">
                    {args['contract_text']}
            </p>
            <!-- Note the anchor tag for the signature field is in white. -->
           <h3 style="margin-top:3em;">Agreed: <span style="color:white;">/sn1/</span></h3>
           <h3 style="margin-top:3em;">Agreed: <span style="color:white;">/**signature_1**/</span></h3>
            </body>
        </html>
      """
