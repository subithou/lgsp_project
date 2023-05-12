from django.http import HttpResponse
from django.shortcuts import render, redirect
import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint
from django.contrib import messages
from email_app.models import AuthenticationBackend
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

api_client = PureCloudPlatformClientV2.api_client.ApiClient().get_client_credentials_token('682b4a94-5e61-4219-b399-e52764c8da30','u0FlpCfcvHgcnuywg0c_y3dLxee6cllDEq-YyO_0dkA')


def get_rows(table_id):
    api_instance = PureCloudPlatformClientV2.ArchitectApi(api_client)
    datatable_id = table_id # str | id of datatable
    page_number = 1 # int | Page number (optional) (default to 1)
    page_size = 25 # int | Page size (optional) (default to 25)
    showbrief = True # bool | If true returns just the key value of the row (optional) (default to True)
    sort_order = 'ascending' # str | Sort order (optional) (default to 'ascending')
    try:
    # Returns the rows for the datatable with the given id
        api_response = api_instance.get_flows_datatable_rows(datatable_id, page_number=page_number, page_size=page_size, showbrief=showbrief, sort_order=sort_order)
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling ArchitectApi->get_flows_datatable_rows: %s\n" % e)
        return null


@login_required
def lgsp_email(request, pnr):
  current_user = request.user
  name = current_user.first_name + " "+ current_user.last_name

  try:
     # , conversation_id, message_id, #table id, pnr
    #   print("pnr:", pnr)
  
  
    api_message_instance = PureCloudPlatformClientV2.ConversationsApi(api_client)
#   conversation_id = conversation_id # str | conversationId
#   message_id = message_id # str | messageId
    pnr = pnr.strip()

#   api_response_message = api_message_instance.get_conversations_email_message(conversation_id, message_id)
#   pprint(api_response_message)
    
    datatable_id = 'b6abbb1b-10da-4f44-9794-49253bb07748'
    datatable_row = get_rows(datatable_id)
    same_pnr_list = []
    email_list = []
#   print(datatable_row)
  
    api_instance = PureCloudPlatformClientV2.ArchitectApi(api_client)
  

    for i in datatable_row.entities:
        print(i)
        print(i.get('key'))
        row_id = i.get('key')
        showbrief = False
        api_row_info = api_instance.get_flows_datatable_row(datatable_id, row_id, showbrief=showbrief)
        test_pnr = api_row_info.get('pnr')
        cleaned_pnr = test_pnr.strip()
        print("cleaned pnr:"+cleaned_pnr)
        print("pnr:"+pnr)
        if pnr == cleaned_pnr:
            print(True)
         # same_pnr_list.append([api_row_info['conversation_id'], api_row_info['message_id'], api_row_info['pnr']])
            same_pnr_list.append(api_row_info)
            print(api_row_info)
            print(api_row_info.get('conversation_id'))
            conversation_id = api_row_info.get('key')
            message_id = api_row_info.get('message_id')
            api_response_message = api_message_instance.get_conversations_email_message(conversation_id, message_id)
            email_list.append(api_response_message)
    print(same_pnr_list)
    return render(request, 'email_structure.html',{'api_response_message':email_list,
                                                'datatable_row': datatable_row, 'name':name})
  except:
    messages.error(request, 'Error occured in PNR number')
    return redirect('view_email')


@login_required
def all_pnr_list(request):
    current_user = request.user
    name = current_user.first_name + " "+ current_user.last_name
    # api_message_instance = PureCloudPlatformClientV2.ConversationsApi(api_client)

    conversation_id = '7423a681-8186-44d4-9385-ca2c80acdd9e' # str | conversationId
    message_id = 'deb55674-868c-4513-b18d-af41b9e12625' # str | messageId

    datatable_id = 'b6abbb1b-10da-4f44-9794-49253bb07748'
    datatable_row = get_rows(datatable_id)

    api_instance = PureCloudPlatformClientV2.ArchitectApi(api_client)

    print(datatable_row)
    row_list = []
    for i in datatable_row.entities:
        print(i.get('key'))
        row_id = i.get('key')
        showbrief = False
        api_row_info = api_instance.get_flows_datatable_row(datatable_id, row_id, showbrief=showbrief)
        api_row_info['pnr'] = api_row_info.get('pnr').strip()
        row_list.append(api_row_info)

    print(row_list)    

    return render(request, 'view_email.html', {'row_list': row_list, 'name':name})


@login_required
def add_pnr(request):
    current_user = request.user
    name = current_user.first_name + " "+ current_user.last_name
    
    if request.method == 'POST':
        new_pnr = str(request.POST.get('new_pnr'))
        new_sender_email = str(request.POST.get('new_sender_email'))
        new_message_id = str(request.POST.get('new_message_id'))
        new_conversation_id = str(request.POST.get('new_conversation_id'))

        datatable_id = 'b6abbb1b-10da-4f44-9794-49253bb07748'
        datatable_row = get_rows(datatable_id)
        api_instance = PureCloudPlatformClientV2.ArchitectApi(api_client)

        for i in datatable_row.entities:
            print(i.get('key'))
            row_id = i.get('key')
            showbrief = False
            api_row_info = api_instance.get_flows_datatable_row(datatable_id, row_id, showbrief=showbrief)
            exist_conversation_id = api_row_info.get('key')
            exist_message_id = api_row_info.get('message_id')

            if exist_conversation_id == new_conversation_id and exist_message_id == new_message_id:
                # datatable_id = 'datatable_id_example' # str | id of datatable
                # row_id = 'row_id_example' # str | the key for the row
                body = {
                    'pnr': new_pnr,
                    'message_id': new_message_id,
                    'sender_emailid': new_sender_email,
                    'key': new_conversation_id
                } # object | datatable row (optional)
                try:
                    api_response = api_instance.put_flows_datatable_row(datatable_id, row_id, body=body)
                    messages.error(request, 'Successfully Updated')
                    return redirect('view_email')
                except :
                    # messages.error(request, 'Please provide correct input')
                    return redirect('add_pnr')
            else:
                data_table_row = {
                    'pnr': new_pnr,
                    'message_id': new_message_id,
                    'sender_emailid': new_sender_email,
                    'key': new_conversation_id
                }
                try:
                    # Create a new row entry for the datatable.
                    api_response = api_instance.post_flows_datatable_rows(datatable_id, data_table_row)
                    messages.error(request, 'Successfully Updated')
                    return redirect('view_email')
                except ApiException as e:
                    print("Exception when calling ArchitectApi->post_flows_datatable_rows: %s\n" % e)
        print(new_pnr, new_sender_email, new_message_id, new_conversation_id)


    return render(request, 'add_pnr.html',{'name':name})


def login_page(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        if AuthenticationBackend.authenticate(self=None, request=request, username=username1,
                                              password=password1) is not None:
            user = AuthenticationBackend.authenticate(self=None, request=request, username=username1,
                                                      password=password1)

            login(request, user)
            # Redirect to a success page.
            return redirect('view_email')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login_page.html')

    
    return render(request, 'login_page.html')

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
    

