from telegram import *

from telegram.ext import *

import ForGunePortal

"""
bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                              text="You Clicked " + valueFromCallBack + " and key is " + keyFromCallBack)
"""

GuneportalObject = ForGunePortal

# key_token = '1892732900:AAEYJ2a6rQ3L0mGmBAUpS6BNK4EDMrhXBcU'
key_token = "1672147288:AAF1IvWC2MmCBZ-XpqaOdCuHbN64XwezZO0"
bot = Bot(key_token)

updater = Updater(key_token, use_context=True)
dispatcher: Dispatcher = updater.dispatcher


class ProfileManipulation:
    fromProfileShowingPageToMainLandingPage = False

    def PersonalInformationRetriver(self, update: Update):
        ProfileManipulation.fromProfileShowingPageToMainLandingPage = True

        CustomeKbd = [
            [KeyboardButton("<- Back")]
        ]
        replyKbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)

        import DataBaseConnectivity
        listOfUser = DataBaseConnectivity.PersonalInformaionRetrivater(str(update.effective_user.id))
        if listOfUser is not None:
            text_for_retrival = "\U0001F464 Full Name =" + listOfUser["Full_Name"] + '\n' + \
                                "\U0001F481 User Name =@" + listOfUser["User_Name"] + '\n' + \
                                "\U0001F4F1 Phone Number =" + listOfUser["Phone_Number"] + "\n" + \
                                "\U0001F5FA Current Locaction =" + listOfUser["Current_Location"]
            bot.send_message(update.effective_user.id,
                             text="-------------   your Personal information ----------------\n" + text_for_retrival,
                             reply_markup=replyKbd)
            custominline = [[InlineKeyboardButton(text=" Update Information ", callback_data="17~17~17")]]
            repl = InlineKeyboardMarkup(custominline)
            bot.send_message(update.effective_user.id,
                             text="---------------------   End   ----------------------------", reply_markup=repl)
        else:
            bot.send_message(update.effective_user.id, text="Accoun't Can't Be Fetched")


class FileForConfiguration:
    listOfCountries = """
/c30:Afghanistan
/c21:Albania
/c22:Algeria
/c23:American Samoa
/c26:Andorra
/c25:Angola
/c24:Anguilla
/c27:Antigua and Barbuda
/c28:Argentina
/c6:Armenia
/c29:Aruba
/c19:Australia
/c20:Austria
/c5:Azerbaijan
/c31:Bahamas
/c34:Bahrain
/c32:Bangladesh
/c33:Barbados
/c3:Belarus
/c36:Belgium
/c35:Belize
/c37:Benin
/c38:Bermuda
/c47:Bhutan
/c40:Bolivia
/c235:Bonaire, Sint Eustatius and Saba
/c41:Bosnia and Herzegovina
/c42:Botswana
/c43:Brazil
/c52:British Virgin Islands
/c44:Brunei Darussalam
/c39:Bulgaria
/c45:Burkina Faso
/c46:Burundi
/c103:Côte d`Ivoire
/c91:Cambodia
/c92:Cameroon
/c10:Canada
/c90:Cape Verde
/c149:Cayman Islands
/c213:Central African Republic
/c214:Chad
/c216:Chile
/c97:China
/c98:Colombia
/c99:Comoros
/c100:Congo
/c101:Congo, Democratic Republic
/c150:Cook Islands
/c102:Costa Rica
/c212:Croatia
/c104:Cuba
/c138:Curaçao
/c95:Cyprus
/c215:Czech Republic
/c73:Denmark
/c231:Djibouti
/c74:Dominica
/c75:Dominican Republic
/c54:East Timor
/c221:Ecuador
/c76:Egypt
/c166:El Salvador
/c222:Equatorial Guinea
/c223:Eritrea
/c14:Estonia
/c224:Ethiopia
/c208:Falkland Islands
/c204:Faroe Islands
/c205:Fiji
/c207:Finland
/c209:France
/c210:French Guiana
/c211:French Polynesia
/c56:Gabon
/c59:Gambia
/c7:Georgia
/c65:Germany
/c60:Ghana
/c66:Gibraltar
/c71:Greece
/c70:Greenland
/c69:Grenada
/c61:Guadeloupe
/c72:Guam
/c62:Guatemala
/c236:Guernsey
/c63:Guinea
/c64:Guinea-Bissau
/c58:Guyana
/c57:Haiti
/c67:Honduras
/c68:Hong Kong
/c50:Hungary
/c86:Iceland
/c80:India
/c81:Indonesia
/c84:Iran
/c83:Iraq
/c85:Ireland
/c147:Isle of Man
/c8:Israel
/c88:Italy
/c228:Jamaica
/c229:Japan
/c237:Jersey
/c82:Jordan
/c4:Kazakhstan
/c94:Kenya
/c96:Kiribati
/c105:Kuwait
/c11:Kyrgyzstan
/c106:Laos
/c12:Latvia
/c109:Lebanon
/c107:Lesotho
/c108:Liberia
/c110:Libya
/c111:Liechtenstein
/c13:Lithuania
/c112:Luxembourg
/c116:Macau
/c117:Macedonia
/c115:Madagascar
/c118:Malawi
/c119:Malaysia
/c121:Maldives
/c120:Mali
/c122:Malta
/c125:Marshall Islands
/c124:Martinique
/c114:Mauritania
/c113:Mauritius
/c126:Mexico
/c127:Micronesia
/c15:Moldova
/c129:Monaco
/c130:Mongolia
/c230:Montenegro
/c131:Montserrat
/c123:Morocco
/c128:Mozambique
/c132:Myanmar
/c133:Namibia
/c134:Nauru
/c135:Nepal
/c139:Netherlands
/c143:New Caledonia
/c142:New Zealand
/c140:Nicaragua
/c136:Niger
/c137:Nigeria
/c141:Niue
/c148:Norfolk Island
/c173:North Korea
/c174:Northern Mariana Islands
/c144:Norway
/c146:Oman
/c152:Pakistan
/c153:Palau
/c154:Palestine
/c155:Panama
/c156:Papua New Guinea
/c157:Paraguay
/c158:Peru
/c206:Philippines
/c159:Pitcairn Islands
/c160:Poland
/c161:Portugal
/c162:Puerto Rico
/c93:Qatar
/c163:Réunion
/c165:Romania
/c1:Russia
/c164:Rwanda
/c169:São Tomé and Príncipe
/c172:Saint Helena
/c178:Saint Kitts and Nevis
/c179:Saint Lucia
/c180:Saint Pierre and Miquelon
/c177:Saint Vincent and the Grenadines
/c167:Samoa
/c168:San Marino
/c170:Saudi Arabia
/c176:Senegal
/c181:Serbia
/c175:Seychelles
/c190:Sierra Leone
/c182:Singapore
/c234:Sint Maarten
/c184:Slovakia
/c185:Slovenia
/c186:Solomon Islands
/c187:Somalia
/c227:South Africa
/c226:South Korea
/c232:South Sudan
/c87:Spain
/c220:Sri Lanka
/c188:Sudan
/c189:Suriname
/c219:Svalbard and Jan Mayen
/c171:Swaziland
/c218:Sweden
/c217:Switzerland
/c183:Syria
/c192:Taiwan
/c16:Tajikistan
/c193:Tanzania
/c191:Thailand
/c194:Togo
/c195:Tokelau
/c196:Tonga
/c197:Trinidad and Tobago
/c199:Tunisia
/c200:Turkey
/c17:Turkmenistan
/c151:Turks and Caicos Islands
/c198:Tuvalu
/c53:US Virgin Islands
/c9:USA
/c201:Uganda
/c2:Ukraine
/c145:United Arab Emirates
/c49:United Kingdom
/c203:Uruguay
/c18:Uzbekistan
/c48:Vanuatu
/c233:Vatican
/c51:Venezuela
/c55:Vietnam
/c202:Wallis and Futuna
/c78:Western Sahara
/c89:Yemen
/c77:Zambia
/c79:Zimbabwe
    """


class ForGlobalPortalFlagAndVariables:
    fromFirstPageOfGlobalPortToMainPage = False
    fromMyBooksManipulationToFirstPage = False
    fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter = False
    fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter2 = False
    fromAddingBookToMyBookManipulationPage = False
    fromBookListToFirstLandingPage = False


class UserAccountHandler:
    manuallySpecifyingNameOFtheUser = False
    manuallyEnteringContactNumber = False
    selectingLocationUsingList = False
    manuallyEnteringLocation = False
    flagForRegisteringNewUser = False

    # ----------- peresonal Information holder varaibles -----------
    FullName = ""
    PhoneNumber = ""
    UserName = ""
    Location = ""

    # ---------------------- end ----------------------------------
    def approvingInformationEntered(self, update: Update):
        UserAccountHandler.flagForRegisteringNewUser = True
        UserAccountHandler.manuallySpecifyingNameOFtheUser = False
        UserAccountHandler.manuallyEnteringContactNumber = False
        UserAccountHandler.selectingLocationUsingList = False
        UserAccountHandler.manuallyEnteringLocation = False

        buttonlist = [[KeyboardButton("Yes")], [KeyboardButton("No")]]
        customKeyBoard = ReplyKeyboardMarkup(buttonlist, resize_keyboard=True)
        personalInfn = "\U0001F464 Full Name :" + str(UserAccountHandler.FullName) + "\n" + " \U0001F464 User Name :" + str(
            UserAccountHandler.UserName) + "\n" + " \U0001F4F1	 Phone Number: " + str(
            UserAccountHandler.PhoneNumber) + "\n" + " \U0001F4F1	 Telegram user Id :" + str(
            update.effective_user.id) + "\n" + "\U0001F5FA	 Current Location :" + str(
            UserAccountHandler.Location) + "\n" + "DO YOU WANT TO CONTINUE WITH THER INFORMATION?"
        try:
            query = update.callback_query
            query.answer()
            update.message.reply_text(text=personalInfn + "\n\U0001F446\U0001F446\U0001F446\U0001F446",
                                      reply_markup=customKeyBoard)
        except:
            bot.send_message(update.effective_user.id, text=personalInfn + "\nU0001F446\U0001F446\U0001F446\U0001F446",
                             reply_markup=customKeyBoard)

    def CreateAnAccountMessage(self, update: Update):
        replykbd = ReplyKeyboardRemove()

        bot.send_message(update.effective_user.id, text="Press The Button To Create An Account", reply_markup=replykbd)
        cutomkbd = [
            [InlineKeyboardButton("Create An Account", callback_data="-10~" + "nothing~" + "55")]
        ]
        repluinline = InlineKeyboardMarkup(cutomkbd)
        bot.send_message(update.effective_user.id, text="\U0001F477\U0001F477\U0001F477\U0001F477",
                         reply_markup=repluinline)

    def UserNameTypeChoosing(self, update: Update):
        query = update.callback_query
        query.answer()
        cutomekbd = [[InlineKeyboardButton("Use Telegram Account Name", callback_data="-11~nothing~55")],
                     [InlineKeyboardButton("Type Manually ", callback_data="-12~nothing~55")]]
        query.edit_message_text("Choose How Do You Want Specify Your Gune Portal Name")
        query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(cutomekbd))

    def SpecifyingNameManullayTyping(self, update: Update, flag):
        UserAccountHandler.manuallySpecifyingNameOFtheUser = True
        if flag == 1:
            query = update.callback_query
            query.answer()
            query.edit_message_text(text="Enter Full Name")

        elif flag == 2:
            query = update.callback_query
            query.answer()
            query.edit_message_text(text="Your Telegram Name isn't meet The policy so ,Enter Full Name Manually")

    def locationsSetterIfManuallyEntred(self, update: Update, cntry):
        UserAccountHandler.Location = cntry
        if UserAccountHandler.UserName is None or UserAccountHandler.UserName == "":
            bot.send_message(update.effective_user.id,
                             text="Before Creating An Account You Need To Have User Name\n After U Set User Name Come Back And create An Account")

            UserAccountHandler().CreateAnAccountMessage(update)
        else:
            UserAccountHandler().approvingInformationEntered(update)

    def locationSpecifyingManually(self, update: Update):
        UserAccountHandler.manuallyEnteringLocation = True
        query = update.callback_query
        query.answer()
        query.edit_message_text(text="Enter Your Current Location?")

    def CountryListProvider(self, update: Update):
        UserAccountHandler.selectingLocationUsingList = True
        query = update.callback_query
        query.answer()
        country = FileForConfiguration.listOfCountries
        query.edit_message_text(text="-- Choose Your Country From These Links -- \n" + country,
                                reply_markup=InlineKeyboardMarkup([[]]))

    def forDefiningLocationUsingInlineButtonsofUser(self, update: Update, currenTextCommand):

        objectFile = FileForConfiguration()
        listOFcont = objectFile.listOfCountries.split("\n")
        usercurrentLocation = ""
        for items in listOFcont:
            countryName = items.split(":")
            if countryName[0] == currenTextCommand:
                for itemss in countryName[1:]:
                    usercurrentLocation += " , " + itemss

        UserAccountHandler.Location = usercurrentLocation
        if UserAccountHandler.UserName is None or UserAccountHandler.UserName == "":
            bot.send_message(update.effective_user.id,
                             text="Before Creating An Account You Need To Have User Name\n After U Set User Name Come Back And create An Account")
            UserAccountHandler().CreateAnAccountMessage(update)
        else:
            UserAccountHandler().approvingInformationEntered(update)

    def LocationOfTheUser(self, update: Update):
        repl = ReplyKeyboardRemove()
        bot.send_message(update.effective_user.id, text="Choose How You Want To Specify YOur Current Location",
                         reply_markup=repl)
        bot.delete_message(update.effective_chat.id, update.effective_message.message_id)

        Customekbd = [
            [InlineKeyboardButton("Get List Of Country's", callback_data="-15~15~5")],
            [InlineKeyboardButton("Enter Your Location Manually", callback_data="-16~16~16")]
        ]

        bot.send_message(update.effective_user.id, text="\U0001F447\U0001F447\U0001F447\U0001F447",
                         reply_markup=InlineKeyboardMarkup(Customekbd))

    def PhoneNumberRetriver(self, update: Update):
        # bot.delete_message(update.effective_chat.id, update.effective_message.message_id)
        CustmizeKeyBoard = [
            [InlineKeyboardButton("use Telegram Account Number", callback_data="-13~13~13")],
            [InlineKeyboardButton("Enter Phone Number Manually", callback_data="-14~14~14")]
        ]
        try:
            query = update.callback_query
            query.answer()

            query.edit_message_text(text="Choose How You Want To Provide You Personal Information")
            query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(CustmizeKeyBoard))
        except:
            bot.delete_message(update.effective_chat.id, update.effective_message.message_id)
            bot.send_message(update.effective_user.id, text="Choose How You Want To Provide You Personal Information",
                             reply_markup=InlineKeyboardMarkup(CustmizeKeyBoard))

    def PhoneNumberFromUserManually(self, update: Update):
        UserAccountHandler.manuallyEnteringContactNumber = True
        UserAccountHandler.UserName = update.effective_user.username

        bot.delete_message(update.effective_chat.id, update.effective_message.message_id)
        repl = ReplyKeyboardRemove()
        bot.send_message(update.effective_user.id, text="Enter You Phone Number should be valid Phone Number",
                         reply_markup=repl)

    def PhoneNumberFromTelgramAutomaticallyRetriver(self, update: Update, flag):
        if flag == 1:
            customKbd = [
                [KeyboardButton("Share Your Contact Information", request_contact=True, request_location=True)]
            ]
            replykbd = ReplyKeyboardMarkup(customKbd, resize_keyboard=True)
            query = update.callback_query
            query.answer()
            query.delete_message()
            update.effective_user.send_message(text="Press The Button Below To Proceed ", reply_markup=replykbd)
        else:
            Information = update.message.contact
            phoneNumber = Information["phone_number"]
            username = update.effective_user.username
            location = update.message.location
            if username is None:
                bot.send_message(update.effective_user.id,
                                 text="There Must Be Telegram user name On Your Account and press Share Button")
            else:
                if phoneNumber is None:
                    bot.send_message(update.effective_user.id,
                                     text="Your Phone Number Can't Be Accessed Automatically so You Need To Enter Manually")
                    UserAccountHandler().PhoneNumberFromUserManually(update)
                else:
                    if location is None:
                        UserAccountHandler.PhoneNumber = phoneNumber
                        UserAccountHandler.UserName = username
                        UserAccountHandler().LocationOfTheUser(update)
                    else:
                        UserAccountHandler.Location = location
                        UserAccountHandler.PhoneNumber = phoneNumber
                        UserAccountHandler.UserName = username
                        if UserAccountHandler.UserName is None or UserAccountHandler.UserName != "":
                            bot.send_message(update.effective_user.id,
                                             text="Before Creating An Account You Need To Have User Name\n After U Set User Name Come Back And create An Account")

                            UserAccountHandler().CreateAnAccountMessage(update)
                        else:
                            UserAccountHandler().approvingInformationEntered(update)


#                     u need to go to next step what ever that is
flagForPortalChoose = -1
flagForNameName = False
flagForNameOFLocation = False
flagForUsingDefaultName = False
flagForLocationSpecification = False
flagForYesNoReviewRegistereing = False
flagForNameOfTheBook = False
flagForCatagoryOfTheBook = False
flagForPublicationYearOfTheBook = False
flagForStatusOfTheBook = False
flagForNumberOfEditionOfTheBook = False
flagForCurrentPrice = False
flagForFileAttaching = True
flagForOtherSpecificationCatgoryOfTheBook = False
flagForTheLanguageOfTheBook = False
forDeletingBookID = ""
userNameFullName = ""
userName = ""
phoneNumber = ""
usertelegramID = ""
usercurrentLocation = ""

nameOfTheBook = ""
catagoryOfTheBook = ""
languageOFTheBook = ""
StatusTheBook = ""
NumberOfEdition = ""
publicationYear = ""
CurrentPrice = ""
BookDocumentFile = ""
forUpdaterBookId = ""
flagForUpdaterTrue = False
ShortNotice = ""
mothForCommentingMonthlyReview = ""
timsStampIdForMonthReview = ""

ActualDocument = ""
DocumentId = ""
NameOfSeminar = ""
NameOfTheDocument = ""
DateAndTimeTheReviewHeld = ""
publisherName = ""
NumberOfpages = ""
RviewedPresenter = ""
ReviewDetailDiscription = ""
timsestampFormonthlyreview = ""

listForFictionalBooks = [
    [InlineKeyboardButton(text="Fanatasy", callback_data="book-selection-Fantasy"),
     InlineKeyboardButton(text="Science Fiction", callback_data="book-selection-Science_Fiction")],
    [InlineKeyboardButton(text="Historical Fiction", callback_data="book-selection-Historical_Fiction"),
     InlineKeyboardButton(text="Realistic Fiction", callback_data="book-selection-Realistic_Fiction")],
    [InlineKeyboardButton(text="Mystrey", callback_data="book-selection-Mystrey"),
     InlineKeyboardButton(text="Fan Fiction", callback_data="book-selection-Fan_Fiction")],
    [InlineKeyboardButton(text="Suspense", callback_data="book-selection-Suspense_OR_Thriller"),
     InlineKeyboardButton(text="Crime", callback_data="book-selection-Crime")],
    [InlineKeyboardButton(text="Horror", callback_data="book-selection-Horror"),
     InlineKeyboardButton(text="Humor", callback_data="book-selection-Humor")],
    [InlineKeyboardButton(text="Classic", callback_data="book-selection-Classic"),
     InlineKeyboardButton(text="Satire", callback_data="book-selection-Satire")],
    [InlineKeyboardButton(text="Comic/Graphic", callback_data="book-selection-Comic/Graphic"),
     InlineKeyboardButton(text="Magical Realism", callback_data="book-selection-Magical_Realism")],
    [InlineKeyboardButton(text="Romance", callback_data="book-selection-Romance"),
     InlineKeyboardButton(text="Drama", callback_data="book-selection-Drama")],
    [InlineKeyboardButton(text="Anthology", callback_data="book-selection-Anthology"),
     InlineKeyboardButton(text="Fable", callback_data="book-selection-Fable")],
    [InlineKeyboardButton(text="Fairy Tale", callback_data="book-selection-Fairy_Tale"),
     InlineKeyboardButton(text="Short Story", callback_data="book-selection-Short_Story")],
    [InlineKeyboardButton(text="Mythology", callback_data="book-selection-Mythology"),
     InlineKeyboardButton(text="Legened", callback_data="book-selection-Legend")],
    [InlineKeyboardButton(text="Other", callback_data="book-selection-Other")]
]

listForNonFictionalBooks = [
    [InlineKeyboardButton(text="Narrative Non-Fiction", callback_data="book-selection-Narrative_Non_Fiction"),
     InlineKeyboardButton(text="Essay", callback_data="book-selection-Essay")],
    [InlineKeyboardButton(text="Speech", callback_data="book-selection-Speech"),
     InlineKeyboardButton(text="Self Help Books", callback_data="book-selection-Self_Help_Books")],
    [InlineKeyboardButton(text="Periodicals", callback_data="book-selection-periodicals"),
     InlineKeyboardButton(text="Biography", callback_data="book-selection-Biography")],
    [InlineKeyboardButton(text="Reference Book", callback_data="book-selection-Reference_Book"),
     InlineKeyboardButton(text="Text Book", callback_data="book-selection-Text_Book")],
    [InlineKeyboardButton(text="Memoir", callback_data="book-selection-Memoir"),
     InlineKeyboardButton(text="Research Papers", callback_data="book-selection-Research_Papers")],
    [InlineKeyboardButton(text="Other", callback_data="book-selection-Other")]
]

conts = FileForConfiguration().listOfCountries


def AccountHandler(update: Update, context: CallbackContext):
    global flagForNameName
    flagForNameName = True
    customekbd = [[KeyboardButton("Or,Use telegram Account Name")]]
    reply_markup = ReplyKeyboardMarkup(customekbd, resize_keyboard=True)
    update.message.reply_text(text="Enter Your Full Name", reply_markup=reply_markup)


def start(update: Update, context: CallbackContext):
    buttons_list = [[KeyboardButton("Amharic"), KeyboardButton("English")]]
    creatKBD = ReplyKeyboardMarkup(buttons_list, resize_keyboard=True)
    update.message.reply_text(text="Choose Language to proceed :", reply_markup=creatKBD)


def languageHandler(update: Update, context: CallbackContext):
    buttons_list = [[KeyboardButton("Create An Account")]]
    creatKBD = ReplyKeyboardMarkup(buttons_list, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text="Press the Button To create An User Account", reply_markup=creatKBD,
                              allow_sending_without_reply=True)


def phoneNumberRetriver(update: Update, context: CallbackContext):
    global phoneNumber, usertelegramID, userName, flagForUsingDefaultName, userNameFullName

    chat_user_client = update.message.from_user.username
    collectionOfPersonalInformation = update.message.contact

    userName = chat_user_client
    usertelegramID = collectionOfPersonalInformation["user_id"]
    phoneNumber = collectionOfPersonalInformation["phone_number"]
    if flagForUsingDefaultName:
        userNameFullName = collectionOfPersonalInformation["first_name"]
        print(userNameFullName)
        flagForUsingDefaultName = False
    flagForNameOFLocation = True

    CustomeKeyBoard = [[KeyboardButton("YES,am ready!"), KeyboardButton("NO.am not!")]]
    relpkbd = ReplyKeyboardMarkup(CustomeKeyBoard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text(text="Are you ready am about to send u bog list countries!\nChoose Ur location pressing "
                                   "link along with ur country", reply_markup=relpkbd)


def forcreatingSharedInformationkeyBoards(update: Update, context: CallbackContext):
    buttons_list = [[KeyboardButton("Share_Contact_Information", request_contact=True, request_location=True)]]
    creatKBD = ReplyKeyboardMarkup(buttons_list, resize_keyboard=True)
    update.message.reply_text(text="Press the Button To create An User Account", reply_markup=creatKBD,
                              allow_sending_without_reply=True)


def approvalFunction(update: Update, context: CallbackContext):
    global userNameFullName, userName, phoneNumber, usertelegramID, usercurrentLocation

    buttonlist = [[KeyboardButton("Yes")], [KeyboardButton("No")]]
    customKeyBoard = ReplyKeyboardMarkup(buttonlist, resize_keyboard=True)
    personalInfn = "Full Name :" + str(userNameFullName) + "\n" + "User Name :" + str(
        userName) + "\n" + "Phone Number" + str(
        phoneNumber) + "\n" + "Telegram user Id:" + str(
        usertelegramID) + "\n" + "Current Location" + str(
        usercurrentLocation) + "\n" + "DO YOU WANT TO CONTINUE WITH THER INFORMATION?"

    update.message.reply_text(text=personalInfn, reply_markup=customKeyBoard)


# -------------------------------
def afterApproval(update: Update, context: CallbackContext):
    listOFbuttons = [#🔍 U+1F468 U+1F30D
        [KeyboardButton(text="\U0001F4DA Gune Portal"), KeyboardButton(text="\U0001F30D Global Portal")],
        [KeyboardButton(text="\U0001F468 Profile"), KeyboardButton(text="🔍 Search For Books")]
    ]
    relpyKbd = ReplyKeyboardMarkup(keyboard=listOFbuttons, resize_keyboard=True)
    update.message.reply_text(text="Choose what To Perform", reply_markup=relpyKbd)


def CountryListProvider(update: Update, context: CallbackContext):
    global flagForLocationSpecification
    bot.sendMessage(update.effective_chat.id, conts)
    reply_markup = ReplyKeyboardMarkup([["Other Country"]], resize_keyboard=True)
    update.message.reply_text(text="\U0001F446	 \U0001F446	\U0001F446	 \U0001F446", reply_markup=reply_markup)
    flagForLocationSpecification = True


def forSpecificCountry(update: Update, context: CallbackContext):
    replKbd = ReplyKeyboardRemove()
    update.message.reply_text(text="Enter Your Location ,If its more than one spzeify using \',\' ?",
                              reply_markup=replKbd)


def BooksFtecherFromDatabase(update: Update, context: CallbackContext):
    ForGlobalPortalFlagAndVariables.fromFirstPageOfGlobalPortToMainPage = False
    CustomeKbs = [[KeyboardButton("<- Back")]
                  ]
    ForGlobalPortalFlagAndVariables.fromBookListToFirstLandingPage = True
    replkbd = ReplyKeyboardMarkup(CustomeKbs, resize_keyboard=True)
    bot.send_message(update.effective_user.id, text="\U0001F447\U0001F447\U0001F447\U0001F447", reply_markup=replkbd)
    import DataBaseConnectivity
    # currentUserId = update.effective_user.id
    # lis = DataBaseConnectivity.BookListProvideForSingleUserTelegId(str(currentUserId))
    lis = DataBaseConnectivity.BookListProviderALLtheBookAvaiable()
    if lis == None:
        bot.sendMessage(update.effective_chat.id, "There Is No Book Recorded")
    else:
        forInlineKeyBd = []
        fg = 0
        for i in lis:
            templist = []

            for oo in lis[i]:
                FullInfnOfTheBooks = (lis[i])[oo]
                nameOFTheBook = FullInfnOfTheBooks["NameOFtheBook"]
                catagory = FullInfnOfTheBooks["Catagory"]
                langaugeOFTheBook = FullInfnOfTheBooks["LanguageOFTheBook"]
                numberOFEdition = FullInfnOfTheBooks["LanguageOFTheBook"]
                CurrentPrice = FullInfnOfTheBooks["CurrentPrice"]
                PublicationYear = FullInfnOfTheBooks["PublicationYear"]
                StatusOfTheBook = FullInfnOfTheBooks["StatusOfTheBook"]
                cms = nameOFTheBook  # + "\n" + "Language=" + langaugeOFTheBook + "\n" + "Catagory=" + catagory
                if fg == 1:
                    templist.append(InlineKeyboardButton(cms, callback_data="2-" + i + "-" + oo))
                    forInlineKeyBd.append(templist)
                    templist = []
                    fg = 0
                else:
                    templist.append(InlineKeyboardButton(text=cms, callback_data="2-" + i + "-" + oo))
                    fg += 1

            if fg == 1:
                forInlineKeyBd.append(templist)

        replKbd = InlineKeyboardMarkup(forInlineKeyBd)
        update.message.reply_text(text="List of books so far registered", reply_markup=replKbd)


def forReturningDiscriptionWithFileRetriver(update: Update, context: CallbackContext, tgidofuser, bookid):
    import DataBaseConnectivity
    allBookInfn = DataBaseConnectivity.BookListProvideForSingleUserTelegIdspecifically(tgidofuser, bookid)
    forPersenting = "\U0001F4D5 Name Of The Book :" + allBookInfn["NameOFtheBook"] + "\n" + \
                    "\U0001F9CB Catagory  :" + allBookInfn["Catagory"] + "\n" + \
                    "\U0001F4B8 Current Price :" + str(allBookInfn["CurrentPrice"]) + "\n" + \
                    "\U0001F30D Langauge of the book :" + allBookInfn["LanguageOFTheBook"] + "\n" + \
                    "\U0001F522 Edition Number :" + str(allBookInfn["NumberEditionNumber"]) + "\n" + \
                    "\U0000231A	 Published at : " + allBookInfn["PublicationYear"] + "\n" + \
                    "\U0001F449 status of the book :" + allBookInfn["StatusOfTheBook"] + "\n"
    x = allBookInfn["BookId"]
    bot.sendMessage(update.effective_user.id, text=forPersenting)
    bot.send_document(update.effective_user.id, x)


def inlineQueryHandler(update: Update, context: CallbackContext):
    global catagoryOfTheBook, typeofcatagory, flagForOtherSpecificationCatgoryOfTheBook
    query = update.callback_query
    query.answer()

    # query.edit_message_text(text=f"Selected option: {query.data}")
    infnForRetrival = query.data
    listofinfns = []
    if infnForRetrival.__contains__('~'):
        listofinfns = infnForRetrival.split("~")
    else:
        listofinfns = infnForRetrival.split("-")
    forPersenting = ""
    userId = listofinfns[0]
    numberOfBookInDb = listofinfns[1]
    nameOFCommandKeys = listofinfns[2]
    if flagForCatagoryOfTheBook:
        if nameOfTheBook != "Other":
            if userId == "book":
                catagoryOfTheBook = typeofcatagory + "," + nameOFCommandKeys
                forLangaugeHandlerofTheBook(update, context)
                flagForOtherSpecificationCatgoryOfTheBook = False
        else:
            update.message.reply_text(text="Please Specify What The Category Of the Books is")
            flagForOtherSpecificationCatgoryOfTheBook = True

    else:
        if userId == '-15':  # get list of countrys
            UserAccountHandler.selectingLocationUsingList = True
            UserAccountHandler().CountryListProvider(update)
        elif userId == '-16':  # get specifying country manaully
            UserAccountHandler.manuallyEnteringLocation = True
            UserAccountHandler().locationSpecifyingManually(update)
        elif userId == "-13":  # helps to get the phone number from the telegram Account
            UserAccountHandler().PhoneNumberFromTelgramAutomaticallyRetriver(update, 1)
        elif userId == "-14":  # helps to get the phone number so that user can enter them manually
            UserAccountHandler().PhoneNumberFromUserManually(update)
        elif userId == "-11":  # for creating using telegeram name
            name = update.effective_user.full_name

            if name != "" or name is not None:  # already name is found procedd
                UserAccountHandler.FullName = name
                UserAccountHandler().PhoneNumberRetriver(update)
            else:  # if the name is suitable to register to telegram
                UserAccountHandler().SpecifyingNameManullayTyping(update, 2)

        elif userId == "-12":  # for specifying name
            UserAccountHandler().SpecifyingNameManullayTyping(update, 1)
        elif userId == "-10":  # for creating an account
            UserAccountHandler().UserNameTypeChoosing(update)
        elif userId == "0":
            tgidofuser = listofinfns[1]
            bookid = listofinfns[2]
            forReturningDiscriptionWithFileRetriver(update, context, tgidofuser, bookid)
        elif userId == "1":
            pass
        #      this  here gtb deeep shit been sitting
        elif userId == "2":
            tgidofuser = listofinfns[1]
            bookid = listofinfns[2]
            forReturningDiscriptionWithFileRetriver(update, context, tgidofuser, bookid)
        elif userId == "3":
            customeKbd = [
                [KeyboardButton("Yes, I Want To Edit")],
                [KeyboardButton("No, I Don't")]
            ]
            query = update.callback_query
            query.answer()

            tgidofuser = listofinfns[1]
            bookid = listofinfns[2]
            forReturningDiscriptionWithFileRetriver(update, context, tgidofuser, bookid)
            global forUpdaterBookId, flagForUpdaterTrue
            flagForUpdaterTrue = True
            global flagForNameOfTheBook
            flagForNameOfTheBook = True
            forUpdaterBookId = bookid
            replyKbd = ReplyKeyboardMarkup(customeKbd, resize_keyboard=True)
            query.message.reply_text(text="Current Stored Information", reply_markup=replyKbd)
        elif userId == "4":
            customeKbd = [
                [KeyboardButton("Sure Do u Want Delete")],
                [KeyboardButton("No, I Don't want Delete")]
            ]
            query = update.callback_query
            query.answer()
            tgidofuser = listofinfns[1]
            bookid = listofinfns[2]
            global forDeletingBookID
            forDeletingBookID = bookid
            replyKbd = ReplyKeyboardMarkup(customeKbd, resize_keyboard=True)
            query.message.reply_text(text="Are You Sure Do You Want To Delete", reply_markup=replyKbd)
        elif userId == '5':
            ForGunePortal.GuneOfficialReviews().PrivillageGrantingFuntion(infnForRetrival, update, bot)
        elif userId == '6':
            ForGunePortal.GuneOfficialReviews().PrivillageRevokingFuntion(infnForRetrival, update, bot)
        elif userId == '8':
            timestapid = "-" + nameOFCommandKeys
            import DataBaseConnectivity
            if DataBaseConnectivity.SeminarReviews().DeleteMonthlyReview(timestapid):
                ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
                ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = True
                CustomKeyBoard = [
                    [KeyboardButton("Add Review"), KeyboardButton("Update Review"),
                     KeyboardButton("Delete Review")],
                    [KeyboardButton("<- Back")]
                ]
                replkbd = ReplyKeyboardMarkup(CustomKeyBoard, resize_keyboard=True)
                bot.send_message(update.effective_user.id, text="Review Deleted Successfully", reply_markup=replkbd)

            else:
                ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
                ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = True
                CustomKeyBoard = [
                    [KeyboardButton("Add Review"), KeyboardButton("Update Review"),
                     KeyboardButton("Delete Review")],
                    [KeyboardButton("<- Back")]
                ]
                replkbd = ReplyKeyboardMarkup(CustomKeyBoard, resize_keyboard=True)
                bot.send_message(update.effective_user.id, text="Review Can not Be Deleted", reply_markup=replkbd)
        elif userId == '9':
            global timsestampFormonthlyreview
            timsestampFormonthlyreview = nameOFCommandKeys

            ForGunePortal.GunePortalFlagAndVaraibles.flagForUpdaterIndicaterToDistiguishFromAdder = True
            ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 1)
        elif userId == '10':
            import DataBaseConnectivity
            listoFSuggestion = DataBaseConnectivity.CommuntitySuggestionHandler().listOfSuggestionOfSpecifiedMonth(
                numberOfBookInDb)
            listt = ForGunePortal.GuneOfficialReviews().inlineKeyProviderForSuggester(listoFSuggestion, 0, 5)

            index = 0
            count = 0
            for i in listt[0:len(listt) - 1]:
                CustomeKeyboard = [
                    [InlineKeyboardButton("Approve", callback_data="11~" + i[1] + "~" + numberOfBookInDb),
                     InlineKeyboardButton("Discard", callback_data="12~" + i[1] + "~" + numberOfBookInDb)]]

                if count + 1 == len(listt[0:len(listt) - 1]):
                    CustomeKeyboard.append([InlineKeyboardButton("More", callback_data="13-" + str(
                        listt[len(listt) - 1]) + "-" + numberOfBookInDb)])
                    repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                    bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                else:
                    repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                    bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                count += 1
        elif userId == '11':
            timstID = numberOfBookInDb
            month = nameOFCommandKeys
            import DataBaseConnectivity
            if DataBaseConnectivity.CommuntitySuggestionHandler().forRegisteringApprovedSuggestions(timstID, month):

                if DataBaseConnectivity.CommuntitySuggestionHandler().forDeletinggSuggestionForDiscardingFunction(
                        timstID, month):
                    update.callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))
                    query = update.callback_query
                    query.answer()
                    query.edit_message_text(text="Approved!")
                else:
                    query = update.callback_query
                    query.answer()
                    query.message.reply_text(text="Message Can't Be Approved")
            else:
                query = update.callback_query
                query.answer()
                query.message.reply_text(text="Message Can't Be Approved")

            # for approving the suggestion
        elif userId == '12':

            # for descarding suggetion
            timstID = numberOfBookInDb
            month = nameOFCommandKeys
            import DataBaseConnectivity
            if DataBaseConnectivity.CommuntitySuggestionHandler().forDeletinggSuggestionForDiscardingFunction(
                    timstID, month):
                update.callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="Discarded!")
            else:
                query = update.callback_query
                query.answer()
                query.message.reply_text(text="Message Can't Be Discarded for some reasons")
        elif userId == '13':
            # for handling more Query

            import DataBaseConnectivity
            listoFSuggestion = DataBaseConnectivity.CommuntitySuggestionHandler().listOfSuggestionOfSpecifiedMonth(
                str(nameOFCommandKeys))
            listt = ForGunePortal.GuneOfficialReviews().inlineKeyProviderForSuggester(listoFSuggestion,
                                                                                      startingIndex=int(
                                                                                          numberOfBookInDb),
                                                                                      endinIndex=int(
                                                                                          numberOfBookInDb) + 5)
            if len(listt) > 1:
                index = 0
                count = 0
                for i in listt[0:len(listt) - 1]:
                    CustomeKeyboard = [
                        [InlineKeyboardButton("Approve", callback_data="11~" + i[1] + "~" + str(nameOFCommandKeys)),
                         InlineKeyboardButton("Discard",
                                              callback_data="12~" + i[1] + "~" + str(nameOFCommandKeys))]]

                    if count + 1 == len(listt[0:len(listt) - 1]):
                        CustomeKeyboard.append([InlineKeyboardButton("More", callback_data="13-" + str(
                            listt[len(listt) - 1]) + "-" + numberOfBookInDb)])
                        repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                        bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                    else:
                        repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                        bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                    count += 1
            else:
                bot.send_message(update.effective_user.id, text="There is No More Suggestion to Fetch")
        elif userId == '14':

            import DataBaseConnectivity
            listOFapprovedsuggestions = DataBaseConnectivity.VoteHandler().listProviderForOPeningVotes(
                numberOfBookInDb)
            if listOFapprovedsuggestions is not None:

                listt = ForGunePortal.GuneOfficialReviews().inlineKeyProviderForSuggester(listOFapprovedsuggestions,
                                                                                          0, 5)

                index = 0
                count = 0
                for i in listt[0:len(listt) - 1]:
                    CustomeKeyboard = [
                        [InlineKeyboardButton("Open Vote", callback_data="15~" + i[1] + "~" + numberOfBookInDb)]
                    ]

                    if count + 1 == len(listt[0:len(listt) - 1]):
                        CustomeKeyboard.append([InlineKeyboardButton("More", callback_data="16~" + str(
                            listt[len(listt) - 1]) + "~" + numberOfBookInDb)])
                        repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                        bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                    else:
                        repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                        bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                    count += 1
            else:
                pass
        elif userId == "15":
            month = nameOFCommandKeys
            timestampid = numberOfBookInDb
            import DataBaseConnectivity
            checkIFitsCommitted = DataBaseConnectivity.VoteHandler().OpenVotePoll(timestamp=timestampid,
                                                                                  month=month)
            if checkIFitsCommitted:
                update.callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="Poll Opened!")
            else:
                bot.send_message(update.effective_user.id, text="Vote Can't Be Opened!")
        elif userId == "16":
            import DataBaseConnectivity
            listoFSuggestion = DataBaseConnectivity.VoteHandler().listProviderForOPeningVotes(
                str(nameOFCommandKeys))
            listt = ForGunePortal.GuneOfficialReviews().inlineKeyProviderForSuggester(listoFSuggestion,
                                                                                      startingIndex=int(
                                                                                          numberOfBookInDb),
                                                                                      endinIndex=int(
                                                                                          numberOfBookInDb) + 5)
            if len(listt) > 1:
                index = 0
                count = 0
                for i in listt[0:len(listt) - 1]:
                    CustomeKeyboard = [
                        [InlineKeyboardButton("Open Vote",
                                              callback_data="15~" + i[1] + "~" + str(numberOfBookInDb))]
                    ]

                    if count + 1 == len(listt[0:len(listt) - 1]):
                        CustomeKeyboard.append([InlineKeyboardButton("More", callback_data="16-" + str(
                            listt[len(listt) - 1]) + "-" + numberOfBookInDb)])
                        repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                        bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                    else:
                        repKbd = InlineKeyboardMarkup(CustomeKeyboard)
                        bot.send_message(update.effective_user.id, text=i[index], reply_markup=repKbd)
                    count += 1
            else:
                bot.send_message(update.effective_user.id, text="There is No More Suggestion to Fetch")
        elif userId == "17":
            pass
        elif userId == "18":
            import DataBaseConnectivity
            result = DataBaseConnectivity.VoteHandler().ClosingVote(numberOfBookInDb)
            if result:
                update.callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="Vote Closed!")
            else:
                bot.send_message(update.effective_user.id, text="Vote Can't Be Closed")
        elif userId == "19":
            bot.send_message(update.effective_user.id, text="Enter Your Comment Down here \U0001F447 ")
            ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringCommentOnMothllyReview = True
            global mothForCommentingMonthlyReview, timsStampIdForMonthReview
            mothForCommentingMonthlyReview = numberOfBookInDb
            timsStampIdForMonthReview = nameOFCommandKeys
        elif userId == "20":
            import DataBaseConnectivity
            result = DataBaseConnectivity.VoteHandler().voteforHandlingUpVotes(str(numberOfBookInDb),
                                                                               str(update.effective_user.id))

            if result is not None:

                if result == False:
                    bot.send_message(update.effective_user.id, text="You Already Vote \U0001F44D")
                else:

                    CustomeInlineKeyBorad = [
                        [InlineKeyboardButton("\U0001F44D " + str(result),
                                              callback_data="20~" + str(numberOfBookInDb) + "~" + str(
                                                  update.effective_user.id)),
                         InlineKeyboardButton("\U0001F44E " + str(
                             str(DataBaseConnectivity.VoteHandler().voteResultRetriver(str(numberOfBookInDb), 2))),
                                              callback_data="21~" + str(numberOfBookInDb) + "~" + str(
                                                  update.effective_user.id))],
                    ]
                    update.callback_query.edit_message_reply_markup(
                        reply_markup=InlineKeyboardMarkup(CustomeInlineKeyBorad))
            else:
                bot.send_message(update.effective_user.id, text="You can't Vote")
        elif userId == "21":
            import DataBaseConnectivity
            result = DataBaseConnectivity.VoteHandler().VoteForHandlingDownVotes(str(numberOfBookInDb),
                                                                                 str(update.effective_user.id))
            if result is not None:

                if result == False:
                    bot.send_message(update.effective_user.id, text="You Already Vote \U0001F44E")
                else:

                    CustomeInlineKeyBorad = [
                        [InlineKeyboardButton("\U0001F44D " + str(
                            DataBaseConnectivity.VoteHandler().voteResultRetriver(str(numberOfBookInDb), 1)),
                                              callback_data="20~" + str(numberOfBookInDb) + "~" + str(
                                                  update.effective_user.id)),
                         InlineKeyboardButton("\U0001F44E " + str(result),
                                              callback_data="21~" + str(numberOfBookInDb) + "~" + str(
                                                  update.effective_user.id))],
                    ]
                    update.callback_query.edit_message_reply_markup(
                        reply_markup=InlineKeyboardMarkup(CustomeInlineKeyBorad))
            else:
                bot.send_message(update.effective_user.id, text="You can't Vote")
        elif userId == "22":
            # for location of document sharing handliner in guner portal --- > guneshare --- >share Document for both private or public
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.typeOFTheBook = nameOFCommandKeys
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingTypeOfTheBook = False
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 6)
        elif userId == "23":
            # for location of document sharing handliner in guner portal --- > guneshare --- >share Document for both private or public
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.typeOFTheBook = nameOFCommandKeys
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingTypeOfTheBook = False
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 6)
        elif userId == "24":
            month = numberOfBookInDb
            mainlookUp = nameOFCommandKeys
            typelookUp = listofinfns[3]
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.infnsForDocument = month + "-" + mainlookUp + "-" + typelookUp
            ForGunePortal.GuneShare().InlineListProviderOfDocuments(update, bot, 4)
        elif userId == '25':
            timestapID = numberOfBookInDb
            mainlookUp = (nameOFCommandKeys.split('-'))[1]
            month = (nameOFCommandKeys.split('-'))[0]
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.monthHolder = month
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.timeStampIdHolder = timestapID
            ForGunePortal.GuneShare().DeleteDocuemtInformation(update, bot, month, timestapID, mainlookUp)
        elif userId == "26":
            month = nameOFCommandKeys
            timestampId = numberOfBookInDb
            import DataBaseConnectivity
            result = DataBaseConnectivity.GuneShareForSharingDocument().PrivateToPublicViceVersaConverter(
                timestampId, str(update.effective_user.id), month, 1)
            if result:
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="Successfully Added To Public",
                                        reply_markup=InlineKeyboardMarkup([[]]))

            else:
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="UnSuccessful To Add Public",
                                        reply_markup=InlineKeyboardMarkup([[]]))
        elif userId == "27":
            month = nameOFCommandKeys
            timestampId = numberOfBookInDb
            import DataBaseConnectivity
            result = DataBaseConnectivity.GuneShareForSharingDocument().PrivateToPublicViceVersaConverter(
                timestampId, str(update.effective_user.id), month, 2)
            if result:
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="Successfully Added To Private",
                                        reply_markup=InlineKeyboardMarkup([[]]))

            else:
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="UnSuccessful To Add Private",
                                        reply_markup=InlineKeyboardMarkup([[]]))
        elif userId == '28':

            timestampIdOfDocument = listofinfns[2]
            teleramIdOfReciever = listofinfns[3]
            RequesterId = str(update.effective_user.id)

            dataFoRegsitering = {
                "BookID": timestampIdOfDocument,
                "RequestedBy": RequesterId
            }
            ForGunePortal.GuneShare().RequestToGetPhysicalDocuments(update, bot, dataFoRegsitering,
                                                                    teleramIdOfReciever)
        elif userId == "29":
            bot.send_message(update.effective_user.id, text="You Already make Request To The Owner")
        elif userId == "30":

            import DataBaseConnectivity
            result = DataBaseConnectivity.GuneShareForSharingDocument().VoteRetriverForRequester(
                str(listofinfns[3]))
            bot.send_message(update.effective_user.id, text=result)
        elif userId == "31":
            import DataBaseConnectivity

            bookId = listofinfns[1]
            senderId = listofinfns[2]
            reciverId = listofinfns[3]
            BookInformation = DataBaseConnectivity.GuneShareForSharingDocument().BookInformationRetriver(
                str(senderId), bookId)
            personalInformation = DataBaseConnectivity.GuneShareForSharingDocument().PersonalInformationRetriver(
                senderId)

            textForRetriving = "This The Address Of The Book Owner You Requested For\n" + \
                               BookInformation + "\n" + \
                               " -------------------------------- " + "\n" + \
                               personalInformation
            bot.send_message(reciverId, textForRetriving)
            bot.send_message(update.effective_user.id, text="Your Personal information In Sent")
        elif userId == "32":
            dataToBeStored = {"BookID": listofinfns[1], "RequestedBy": listofinfns[2]}
            import DataBaseConnectivity
            result = DataBaseConnectivity.GuneShareForSharingDocument().writterIfTheBookWasPhysicallYshared(
                str(update.effective_user.id), dataToBeStored)
            if result:
                query = update.callback_query
                query.answer()
                query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))
        elif userId == "33":
            reciverId = listofinfns[3]
            senderId = listofinfns[2]
            bookId = listofinfns[1]
            import DataBaseConnectivity
            result = DataBaseConnectivity.GuneShareForSharingDocument().BookInformationRetriver(senderId, bookId)
            if result is not None:
                text = "-- Book Information You Requested --" + "\n" + \
                       result + "\n" + \
                       "\u26A0 The Book You Requested is not Current In Handel I will let You Know When Its"
                bot.send_message(reciverId, text=text)
                bot.send_message(update.effective_user.id, text="You Have Sent Short Notice For Requester")
            else:
                bot.send_message(update.effective_user.id, text="Short Can't Be Send For Some Reasons")
        elif userId == "34":
            bookId = listofinfns[1]
            userId = listofinfns[2]
            requesterId = listofinfns[3]
            import DataBaseConnectivity
            result = DataBaseConnectivity.GuneShareForSharingDocument().BorrowedDocumentInformationDeleterWhenBookIsRetrived(
                userId, bookId)
            if result:
                CustomeInlineKbd = [
                    [
                        InlineKeyboardButton("\U0001F92C",
                                             callback_data="35~" + "1~" + userId + "~" + requesterId + "~" + bookId),
                        InlineKeyboardButton("\U00002639",
                                             callback_data="35~" + "2~" + userId + "~" + requesterId + "~" + bookId),
                        InlineKeyboardButton("\U0001F642",
                                             callback_data="35~" + "3~" + userId + "~" + requesterId + "~" + bookId),
                        InlineKeyboardButton("\U0001F601",
                                             callback_data="35~" + "4~" + userId + "~" + requesterId + "~" + bookId)]
                ]
                bot.send_message(update.effective_user.id,
                                 text="Please Give Rating To The Book You Selected As Returned Its Neccessary")
                query = update.callback_query
                query.answer()
                query.edit_message_reply_markup(InlineKeyboardMarkup(CustomeInlineKbd))
            else:
                bot.send_message(update.effective_user.id, text="Can't Deleted The Book Returned")
        elif userId == "35":
            dataToBeStored = {"BookId": listofinfns[4], "Rate": listofinfns[1]}
            rateReciverId = listofinfns[3]
            rateGiver = listofinfns[2]
            import DataBaseConnectivity
            if DataBaseConnectivity.GuneShareForSharingDocument().voteRegistrer(dataToBeStored, rateReciverId,
                                                                                rateGiver):
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="The Book History Is Cleared Successfully",
                                        reply_markup=InlineKeyboardMarkup([[]]))
            else:
                query = update.callback_query
                query.answer()
                query.edit_message_text(text="The Book History Is Can't Be Cleared ",
                                        reply_markup=InlineKeyboardMarkup([[]]))
        elif userId == "36":
            import DataBaseConnectivity
            result = DataBaseConnectivity.GuneCommunityHandler().seminarReviewHeldOntheMonthRetriver(listofinfns[1])
            if result is not None:
                for infns in result:
                    text = infns[0]
                    seminarId = infns[1]
                    documnetId = infns[2]
                    bot.send_document(update.effective_user.id, documnetId)
                    CustomeInlineKbd = [[InlineKeyboardButton(" > Comments <", callback_data="37~" + listofinfns[
                        1] + "~" + seminarId)]]
                    replyInline = InlineKeyboardMarkup(CustomeInlineKbd)
                    bot.send_message(update.effective_user.id, text=text, reply_markup=replyInline)
            else:
                bot.send_message(update.effective_user.id,
                                 text="There is No Review Held On This Month OR Its May be Remove Come Back Some Oh=ther Time")
        elif userId == "37":
            import DataBaseConnectivity

            result = DataBaseConnectivity.GuneCommunityHandler().commentsRetriverForSpecifiedSeminarInSpecifiedMonth(
                listofinfns[1], listofinfns[2])
            result2 = DataBaseConnectivity.GuneCommunityHandler().sepecifiedIdSeminarDataRetriver(listofinfns[1],
                                                                                                  listofinfns[2])
            textRetrival = ""
            if result is not None and result2 is not None:
                textRetrival = result2

                textRetrival += "\n-------- All Comments Given ----------- \n"
                for mainResult in result:
                    userIdForUserName = mainResult[0]
                    comment = mainResult[1]
                    fetchedUserName = DataBaseConnectivity.GuneCommunityHandler().personalInformationUserNameRetriver(
                        str(userIdForUserName))
                    if fetchedUserName is not None:
                        textRetrival += "User Name = @" + fetchedUserName + "\n" + \
                                    "Comment =" + comment + "\n" + \
                                    "  -----------------------  \n"
                    else:
                        textRetrival += "No Comments Were Given To This Review \n"



                query = update.callback_query
                query.answer()
                query.edit_message_text(text=textRetrival)

            else:
                query = update.callback_query
                query.answer()
                query.edit_message_reply_markup(InlineKeyboardMarkup(
                    [[InlineKeyboardButton("No Comments Given", callback_data="17~" + "no" + "data")]]))
        else:
            import DataBaseConnectivity
            allBookInfn = DataBaseConnectivity.BookListProvideForSingleUserTelegIdspecifically(userId,
                                                                                               numberOfBookInDb)
            allPersonalInfn = DataBaseConnectivity.PersonalInformaionRetrivater(userId)

            forPersenting = "Name Of The Book :" + allBookInfn["NameOFtheBook"] + "\n" + \
                            "Catagory  :" + allBookInfn["Catagory"] + "\n" + \
                            "Current Price :" + str(allBookInfn["CurrentPrice"]) + "\n" + \
                            "Langauge of the book :" + allBookInfn["LanguageOFTheBook"] + "\n" + \
                            "Edition Number :" + str(allBookInfn["NumberEditionNumber"]) + "\n" + \
                            "Published at : " + allBookInfn["PublicationYear"] + "\n" + \
                            "status of the book :" + allBookInfn["StatusOfTheBook"] + "\n" + \
                            "-------------- Resources from ------------ " + "\n" + \
                            "Name : " + allPersonalInfn["Full_Name"] + "\n" + \
                            "user Name of the account :" + allPersonalInfn["User_Name"] + "\n"
            kbd = [[InlineKeyboardButton("Get The Book", callback_data="1-" + infnForRetrival + "-gtb")]]
            repkbd = InlineKeyboardMarkup(kbd)
            query.edit_message_text(text=forPersenting, reply_markup=repkbd)


def PersonalBookInformationManipualtion(update: Update, context: CallbackContext):
    ForGlobalPortalFlagAndVariables.fromFirstPageOfGlobalPortToMainPage = False
    ForGlobalPortalFlagAndVariables.fromMyBooksManipulationToFirstPage = True
    listofButtons = [[KeyboardButton("\U0001F4C4  List of My Booksl")],
                     [KeyboardButton("\U0001F195 Add new Book"), KeyboardButton("\U0001F4AC Update Book infn")],
                     [KeyboardButton("🛑 Delete book")],
                     [KeyboardButton('<- Back')]]
    repmarkkbd = ReplyKeyboardMarkup(listofButtons, resize_keyboard=True)
    update.message.reply_text(text="Choose What u Going to do ?", reply_markup=repmarkkbd)


#
def customizedBookAdder(update: Update, context: CallbackContext):
    ForGlobalPortalFlagAndVariables.fromAddingBookToMyBookManipulationPage = True
    ForGlobalPortalFlagAndVariables.fromMyBooksManipulationToFirstPage = False
    replKbd = ReplyKeyboardRemove()
    update.message.reply_text(text="Enter The Name OF The Boook?", reply_markup=replKbd)


def forGlobalPort(update: Update, context: CallbackContext):
    ForGlobalPortalFlagAndVariables.fromFirstPageOfGlobalPortToMainPage = True
    ForGlobalPortalFlagAndVariables.fromMyBooksManipulationToFirstPage = False
    ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter = False
    ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter2 = False
    ForGlobalPortalFlagAndVariables.fromAddingBookToMyBookManipulationPage = False
    ForGlobalPortalFlagAndVariables.fromBookListToFirstLandingPage = False

    listOFbuttons = [[KeyboardButton("\U0001F4D5 Books List"), KeyboardButton("\U0001F4DA  Global Portal")], [KeyboardButton("<- Back")]]
    repkbd = ReplyKeyboardMarkup(listOFbuttons, resize_keyboard=True)
    update.message.reply_text(text="Choose How U want Proceed", reply_markup=repkbd)


def forGunePortal(update: Update, context: CallbackContext):
    ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = True

    listOfButtons = [
        [KeyboardButton(text="Gune Official Reviews"), KeyboardButton(text="Gune Share")],
        [KeyboardButton(text="Gune Community Reviews")],
        [KeyboardButton(text="<- Back")]
    ]
    replyKbd = ReplyKeyboardMarkup(listOfButtons, resize_keyboard=True)
    update.message.reply_text(text="\U0001F449\U0001F449\U0001F449", reply_markup=replyKbd)


def personalUploadedBooksInlineButtonRetriver(update: Update, context: CallbackContext, flagdetector):
    ForGlobalPortalFlagAndVariables.fromMyBooksManipulationToFirstPage = False
    ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter = True
    customekbd = [
        [KeyboardButton("<- Back")]
    ]
    replykbd = ReplyKeyboardMarkup(customekbd, resize_keyboard=True)
    bot.send_message(update.effective_user.id,
                     text="If There If Any Book Published By You Will Be Listed Here ",
                     reply_markup=replykbd)
    import DataBaseConnectivity
    listofBooks = DataBaseConnectivity.BookListProvideForSingleUserTelegId(str(update.effective_user.id))
    if listofBooks is not None:
        listOfBookId = listofBooks.keys()

        flag = 0
        CustomKbd = []
        templist = []
        for id in listOfBookId:
            name = str((listofBooks[id])["NameOFtheBook"])
            idd = str((listofBooks[id])["BookId"])

            if flag == 1:

                templist.append(
                    InlineKeyboardButton(text=name,
                                         callback_data=flagdetector + str(update.effective_user.id) + "-" + id))
                CustomKbd.append(templist)
                templist = []
                flag = 0
            else:
                templist.append(
                    InlineKeyboardButton(text=name,
                                         callback_data=flagdetector + str(update.effective_user.id) + "-" + id))
                flag += 1
        CustomKbd.append(templist)
        replKbd = InlineKeyboardMarkup(CustomKbd)
        update.message.reply_text(text="List of books so far registered", reply_markup=replKbd)
    else:
        bot.send_message(update.effective_user.id, text="There is No Book Published So Far")


def personalUploadedActualBooksRetriver(update: Update, context: CallbackContext, booKid):
    import DataBaseConnectivity
    DataBaseConnectivity.BookListProvideForSingleUserTelegIdspecifically(bookNumber=booKid,
                                                                         tguserid=str(update.effective_user.id))


def forSearchingBooks(update: Update, context: CallbackContext):
    listOFbuttons = [
        [KeyboardButton(text="From Gune Seminar Store"), KeyboardButton(text="From Global Store")],
        [KeyboardButton(text="<-Back")]
    ]
    replkbd = ReplyKeyboardMarkup(listOFbuttons, resize_keyboard=True)
    update.message.reply_text(text="\U0001F449\U0001F449\U0001F449", reply_markup=replkbd)


def forLangaugeHandlerofTheBook(update: Update, context: CallbackContext):
    global flagForTheLanguageOfTheBook, languageOFTheBook, flagForNumberOfEditionOfTheBook
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Please Specify In Which Language The Books Is Written?",
                            reply_markup=InlineKeyboardMarkup([[]]))
    flagForTheLanguageOfTheBook = True


def documnetHandler(update: Update, context: CallbackContext):
    global BookDocumentFile, flagForNameOfTheBook, nameOfTheBook, catagoryOfTheBook, languageOFTheBook, StatusTheBook, NumberOfEdition, publicationYear, CurrentPrice, BookDocumentFile
    global ActualDocument, DocumentId
    documnet = update.message.document

    BookDocumentFile = documnet.to_json()
    x = documnet.file_id

    import DataBaseConnectivity
    global forUpdaterBookId, flagForUpdaterTrue, flagForNameName
    if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingActualFile:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.fileContent = BookDocumentFile
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.filecontentId = x
        ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 11)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringActualSuggestionDocumnet:
        ForGunePortal.GunePortalFlagAndVaraibles.actualDocument = BookDocumentFile
        ForGunePortal.GunePortalFlagAndVaraibles.documentId = x
        ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringActualSuggestionDocumnet = False
        ForGunePortal.GuneOfficialReviews().SuggestionAdderForNextMonthReviewSeminar(update, bot, 5)
    elif flagForUpdaterTrue:
        customekbds = [[KeyboardButton("<- Back")]]
        replk = ReplyKeyboardMarkup(customekbds, resize_keyboard=True)

        result = DataBaseConnectivity.writeToBooksInformation2(childId=forUpdaterBookId,
                                                               userTelegramId=str(update.effective_user.id),
                                                               BookName=str(nameOfTheBook),
                                                               langaugeOfTheBook=languageOFTheBook,
                                                               catagory=catagoryOfTheBook,
                                                               editionNumber=NumberOfEdition,
                                                               publicationYear=publicationYear,
                                                               currentPriceOnMarket=CurrentPrice,
                                                               status=StatusTheBook, actualBookInfn=BookDocumentFile,
                                                               bookid=x)
        if result:
            bot.send_message(update.effective_user.id, text="Book Successfully Updated!", reply_markup=replk)
        else:
            bot.send_message(update.effective_user.id,
                             text="Book Can't Be Stored Make Sure You Enter Valid Information And Try Again",
                             reply_markup=replk)

    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForAttachingReviewDocument:
        # for accepting actula document
        ForGunePortal.GunePortalFlagAndVaraibles.flagForAttachingReviewDocument = False
        ActualDocument = BookDocumentFile
        DocumentId = x
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 2)
    else:
        ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter2 = True
        customekbds = [[KeyboardButton("<- Back")]]
        replk = ReplyKeyboardMarkup(customekbds, resize_keyboard=True)

        result = DataBaseConnectivity.writeToBooksInformation(userTelegramId=str(update.effective_user.id),
                                                              BookName=str(nameOfTheBook),
                                                              langaugeOfTheBook=languageOFTheBook,
                                                              catagory=catagoryOfTheBook, editionNumber=NumberOfEdition,
                                                              publicationYear=publicationYear,
                                                              currentPriceOnMarket=CurrentPrice,
                                                              status=StatusTheBook, actualBookInfn=BookDocumentFile,
                                                              bookid=x)

        if result:
            bot.send_message(update.effective_user.id, text="Book Successfully Registered!", reply_markup=replk)
        else:
            bot.send_message(update.effective_user.id,
                             text="Book Can't Be Stored Make Sure You Enter Valid Information And Try Again",
                             reply_markup=replk)


def EditingBookInformation(update: Update, context: CallbackContext):
    personalUploadedBooksInlineButtonRetriver(update, context, "3-")


def BookDeleter(update: Update, context: CallbackContext):
    personalUploadedBooksInlineButtonRetriver(update, context, "4-")


def forDefiningTheNameOfTheBook(update: Update, context: CallbackContext, currenTextCommand):
    global flagForCatagoryOfTheBook, nameOfTheBook, flagForNameOfTheBook
    nameOfTheBook = currenTextCommand.strip()

    customeListKbd = [[KeyboardButton(text="Fiction"), KeyboardButton(text="Non-Fiction")]]
    replKbd = ReplyKeyboardMarkup(customeListKbd, resize_keyboard=True)

    bot.sendMessage(update.effective_user.id, text="Choose one Category's of the book ", reply_markup=replKbd)

    flagForCatagoryOfTheBook = True
    flagForNameOfTheBook = False


def forDefiningTheStatusOfTheBook(update: Update, context: CallbackContext, currenTextCommand):
    global StatusTheBook, flagForFileAttaching, flagForStatusOfTheBook
    flagForStatusOfTheBook = False
    StatusTheBook = currenTextCommand.strip()
    bot.sendMessage(update.effective_user.id, text="Now Attach The Document by pressing 📎 ")
    flagForFileAttaching = True


def forDefiningTheEditionNumberOFtheBook(update: Update, context: CallbackContext, currenTextCommand):
    global NumberOfEdition, flagForCurrentPrice, flagForNumberOfEditionOfTheBook
    NumberOfEdition = currenTextCommand.strip()
    flagForCurrentPrice = True
    flagForNumberOfEditionOfTheBook = False
    bot.sendMessage(update.effective_user.id, text="Enter The Current Price Of The Book?")


def forDefiningThePriceOfTheBook(update: Update, context: CallbackContext, currenTextCommand):
    global flagForCurrentPrice, flagForStatusOfTheBook
    flagForCurrentPrice = False
    flagForStatusOfTheBook = True
    global CurrentPrice
    CurrentPrice = currenTextCommand.strip()
    bot.sendMessage(update.effective_user.id, text="Enter The Status Of The Book?")


def forOtherSpecificationOfTheCatagoryOFTheBook(update: Update, context: CallbackContext, currenTextCommand):
    global catagoryOfTheBook, flagForOtherSpecificationCatgoryOfTheBook
    flagForOtherSpecificationCatgoryOfTheBook = False
    catagoryOfTheBook = currenTextCommand.strip()
    forLangaugeHandlerofTheBook(update, context)


def forDefiningThePublicationYearOfTheBook(update: Update, context: CallbackContext, currenTextCommand):
    global publicationYear, flagForPublicationYearOfTheBook, flagForNumberOfEditionOfTheBook
    publicationYear = currenTextCommand.strip()
    flagForPublicationYearOfTheBook = False
    bot.sendMessage(update.effective_user.id, text="Enter The Number Of Edition Of The Book?")
    flagForNumberOfEditionOfTheBook = True


def forDefiningTheLanguageOfTheBook(update: Update, context: CallbackContext, currenTextCommand):
    global languageOFTheBook, flagForPublicationYearOfTheBook, flagForTheLanguageOfTheBook
    languageOFTheBook = currenTextCommand.strip()
    bot.sendMessage(update.effective_user.id, text="Enter Publication Year Of The Book")
    flagForPublicationYearOfTheBook = True
    flagForTheLanguageOfTheBook = False


def forDefiningLocationSpecificationInManual(update: Update, context: CallbackContext, currenTextCommand):
    global flagForLocationSpecification, flagForNameOFLocation, usercurrentLocation
    flagForLocationSpecification = False
    flagForNameOFLocation = False
    usercurrentLocation = currenTextCommand.strip()
    approvalFunction(update, context)


def forDefiningPersonalNameWhileCreatingAnAccount(update: Update, context: CallbackContext, currenTextCommand):
    global flagForNameName, flagForNameOFLocation, userNameFullName
    flagForNameName = False
    flagForNameOFLocation = True
    userNameFullName = currenTextCommand.strip()
    forcreatingSharedInformationkeyBoards(update, context)


def forDefiningLocationUsingInlineButtonsofUser(update: Update, context: CallbackContext, currenTextCommand):
    global flagForNameOFLocation, flagForLocationSpecification, usercurrentLocation
    objectFile = FileForConfiguration()
    listOFcont = objectFile.listOfCountries.split("\n")

    for items in listOFcont:
        countryName = items.split(":")
        if countryName[0] == currenTextCommand:
            for itemss in countryName[1:]:
                usercurrentLocation += " , " + itemss

            flagForNameOFLocation = False
            flagForLocationSpecification = False
            approvalFunction(update, context)


def AllConditionsForRegisteringAllBookInformation(update: Update, context: CallbackContext, currenTextCommand):
    global RviewedPresenter, flagForYesNoReviewRegistereing, ActualDocument, NumberOfpages, ReviewDetailDiscription, publisherName, NameOfSeminar, NameOfTheDocument, DateAndTimeTheReviewHeld
    if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingActualFile:
        bot.send_message(update.effective_user.id, text="Please Attach onLY Document Not Text")
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingCurrentPrice:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingCurrentPrice = False
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.currentPriceOnMarket = currenTextCommand
        ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 9)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingNumberOfEdition:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingNumberOfEdition = False
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.numberOfEdition = currenTextCommand
        ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 8)

    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingLanguageOfTheBook:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingLanguageOfTheBook = False
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.languageOfTheDocumentWritten = currenTextCommand
        ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 7)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingAuthorOfTheDocument:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingAuthorOfTheDocument = False
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.nameOftheAuthorOfTheDocument = currenTextCommand.strip()
        ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 3)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingDocumentName:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingDocumentName = False
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.nameOftheDocument = currenTextCommand.strip()
        ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 2)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringActualSuggestionDocumnet:
        bot.send_message(update.effective_user.id, text="You Need To Attach The Actual File")
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringDiscriptionOnSuggestion:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringDiscriptionOnSuggestion = False
        ForGunePortal.GunePortalFlagAndVaraibles.discriptionofsuggestion = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().SuggestionAdderForNextMonthReviewSeminar(update, bot, 4)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringNameOfTheAuthor:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringNameOfTheAuthor = False
        ForGunePortal.GunePortalFlagAndVaraibles.nameofauthourofthebook = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().SuggestionAdderForNextMonthReviewSeminar(update, bot, 3)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringSuggestionBookName:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringSuggestionBookName = False
        ForGunePortal.GunePortalFlagAndVaraibles.nameofSuggestedNameOfTheBook = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().SuggestionAdderForNextMonthReviewSeminar(update, bot, 2)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringCommentOnMothllyReview:
        ForGunePortal.GunePortalFlagAndVaraibles().flagForEnteringCommentOnMothllyReview = False
        global mothForCommentingMonthlyReview, timsStampIdForMonthReview
        ForGunePortal.GuneOfficialReviews().CommentOnReviewsHandler(currenTextCommand, update, bot,
                                                                    mothForCommentingMonthlyReview,
                                                                    timsStampIdForMonthReview)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForWritingANoticeForCommunityAsBroadcastMessage:
        global ShortNotice
        ShortNotice = currenTextCommand.strip()
        ForGunePortal.GunePortalFlagAndVaraibles.flagForWritingANoticeForCommunityAsBroadcastMessage = False
        update.message.reply_text(text="This The the Notice You Want To Send\n" + currenTextCommand)
        CustomeKyboard = [
            ["Yes,send to all", "No Don't send"]
        ]
        replKbd = ReplyKeyboardMarkup(CustomeKyboard, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="How You Want To Proceed ?", reply_markup=replKbd)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForReviewPresenter:
        global RviewedPresenter, ActualDocument, NumberOfpages, ReviewDetailDiscription, publisherName, NameOfSeminar, NameOfTheDocument, DateAndTimeTheReviewHeld
        ForGunePortal.GunePortalFlagAndVaraibles.flagForReviewPresenter = False
        RviewedPresenter = currenTextCommand.strip()
        str = "NameOfSeminar:" + NameOfSeminar + "\n" + \
              "NameOfTheDocument:" + NameOfTheDocument + "\n" + \
              "DateAndTimeTheReviewHeld:" + DateAndTimeTheReviewHeld + "\n" + \
              "publisherName:" + publisherName + "\n" + \
              "NumberOfpages:" + NumberOfpages + "\n" + \
              "RviewedPresenter:" + RviewedPresenter + "\n" + \
              "ReviewDetailDiscription:" + ReviewDetailDiscription

        CustomeKeyBoard = [
            [KeyboardButton("Yes"), KeyboardButton("No")]
        ]
        flagForYesNoReviewRegistereing = True
        RelyKbd = ReplyKeyboardMarkup(CustomeKeyBoard, resize_keyboard=True)
        update.message.reply_text(text=str + "\n" + "Are You Sure Do You Want To Continue?", reply_markup=RelyKbd)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForDiscriptionOnThreReview:
        # For Accepting detail review discriotion
        # global ReviewDetailDiscription
        ForGunePortal.GunePortalFlagAndVaraibles.flagForDiscriptionOnThreReview = False
        ReviewDetailDiscription = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 8)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForNumberOfPages:
        # global NumberOfpages
        ForGunePortal.GunePortalFlagAndVaraibles.flagForNumberOfPages = False
        NumberOfpages = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 7)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForDocumentPublsisher:
        # for acceptin puvblisher name
        # global publisherName
        ForGunePortal.GunePortalFlagAndVaraibles.flagForDocumentPublsisher = False
        publisherName = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 6)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForDateReviewHold:
        # for accepting date of review held
        # global DateAndTimeTheReviewHeld
        ForGunePortal.GunePortalFlagAndVaraibles.flagForDateReviewHold = False
        DateAndTimeTheReviewHeld = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 5)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForGuneReviewBookTittle:
        # for accepting name the document when published by publisher
        # global NameOfTheDocument
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGuneReviewBookTittle = False
        NameOfTheDocument = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 4)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForSeminarTittle:
        # for accepting name of semianr or review tittle
        # global NameOfSeminar
        ForGunePortal.GunePortalFlagAndVaraibles.flagForSeminarTittle = False
        NameOfSeminar = currenTextCommand.strip()
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 3)
    # elif flagForNameName:
    #     forDefiningPersonalNameWhileCreatingAnAccount(update, context, currenTextCommand)
    elif UserAccountHandler.manuallyEnteringContactNumber:
        UserAccountHandler.manuallyEnteringContactNumber = False
        UserAccountHandler.PhoneNumber = currenTextCommand.strip()
        UserAccountHandler().LocationOfTheUser(update)

    elif UserAccountHandler.manuallySpecifyingNameOFtheUser:
        UserAccountHandler.manuallySpecifyingNameOFtheUser = False
        UserAccountHandler.FullName = currenTextCommand.strip()
        UserAccountHandler().PhoneNumberRetriver(update)
    elif UserAccountHandler.selectingLocationUsingList:
        UserAccountHandler().forDefiningLocationUsingInlineButtonsofUser(update, currenTextCommand)
    elif UserAccountHandler.manuallyEnteringLocation:
        UserAccountHandler().locationsSetterIfManuallyEntred(update, currenTextCommand)
    elif flagForOtherSpecificationCatgoryOfTheBook:
        forOtherSpecificationOfTheCatagoryOFTheBook(update, context, currenTextCommand)
    elif flagForNameOfTheBook:
        forDefiningTheNameOfTheBook(update, context, currenTextCommand)
    elif flagForTheLanguageOfTheBook:
        forDefiningTheLanguageOfTheBook(update, context, currenTextCommand)
    elif flagForPublicationYearOfTheBook:
        forDefiningThePublicationYearOfTheBook(update, context, currenTextCommand)
    elif flagForNumberOfEditionOfTheBook:
        forDefiningTheEditionNumberOFtheBook(update, context, currenTextCommand)
    elif flagForCurrentPrice:
        forDefiningThePriceOfTheBook(update, context, currenTextCommand)
    elif flagForStatusOfTheBook:
        forDefiningTheStatusOfTheBook(update, context, currenTextCommand)


def ForChoosingLocationInlinKeyBoard(update: Update, context: CallbackContext):
    global typeofcatagory
    typeofcatagory = "Fiction"
    repl = ReplyKeyboardRemove()
    update.message.reply_text("Choose One The Following ", reply_markup=repl)
    listrepl = InlineKeyboardMarkup(listForFictionalBooks)
    update.message.reply_text(text="\U0001F447\U0001F447\U0001F447", reply_markup=listrepl)


def ForChooseingNonFicition(update: Update, context: CallbackContext):
    global typeofcatagory
    typeofcatagory = "Non-Fiction"
    repl = ReplyKeyboardRemove()
    update.message.reply_text("Choose One The Following ", reply_markup=repl)
    listrepl = InlineKeyboardMarkup(listForNonFictionalBooks)
    update.message.reply_text(text="\U0001F447\U0001F447\U0001F447", reply_markup=listrepl)


def ForButtonUsingDefaultNameInCreatingUserAccount(update: Update, context: CallbackContext):
    global flagForNameName, flagForNameOFLocation, flagForUsingDefaultName
    flagForNameName = False
    flagForNameOFLocation = True
    flagForUsingDefaultName = True
    forcreatingSharedInformationkeyBoards(update, context)


def registeringNewCustomer(update: Update, context: CallbackContext, flag):
    if flag:
        ForGunePortal.GunePortalMain().userRegistering(str(update.effective_user.id))
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GunePortalMain().listProviderIfAlreadyCommunityMember()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
    else:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GunePortalMain().listProviderIfAlreadyCommunityMember()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)


def functionHandlesBackwardtraversal(update: Update, context: CallbackContext):
    if ForGlobalPortalFlagAndVariables.fromBookListToFirstLandingPage:
        ForGlobalPortalFlagAndVariables.fromBookListToFirstLandingPage = False
        forGlobalPort(update, context)
    elif ForGlobalPortalFlagAndVariables.fromAddingBookToMyBookManipulationPage:
        ForGlobalPortalFlagAndVariables.fromAddingBookToMyBookManipulationPage = False
        PersonalBookInformationManipualtion(update, context)

    elif ProfileManipulation.fromProfileShowingPageToMainLandingPage:
        bot.delete_message(update.effective_chat.id, update.effective_message.message_id)
        ProfileManipulation.fromProfileShowingPageToMainLandingPage = False
        afterApproval(update, context)
    elif ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter:
        #  this from viewing list of books uploaded by any user in global port to book manipulation page
        ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter = False
        PersonalBookInformationManipualtion(update, context)
    elif ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter2:
        ForGlobalPortalFlagAndVariables.fromViewListOfBooksUploadedByYourSelfToYouBooksManipualtionCenter2 =False
        PersonalBookInformationManipualtion(update, context)
    elif ForGlobalPortalFlagAndVariables.fromMyBooksManipulationToFirstPage:
        # this help to go from personal books manipulation To First Lnding pAGE Thst is book list and my books page
        ForGlobalPortalFlagAndVariables.fromMyBooksManipulationToFirstPage = False

        forGlobalPort(update, context)

    elif ForGlobalPortalFlagAndVariables.fromFirstPageOfGlobalPortToMainPage:
        #  this helps to traers form book list an my books to main landing page that is  gune portal nad global portal
        ForGlobalPortalFlagAndVariables.fromFirstPageOfGlobalPortToMainPage = False
        afterApproval(update, context)

    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForFromNormalViewAdminViewToNormalViewUsers:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForFromNormalViewAdminViewToNormalViewUsers = False
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGuneMainPageToGunePortalMainPage = True
        ForGunePortal.GuneOfficialReviews().FunctionCheckkingThatAuserIsAnAdmin(str(update.effective_user.id), update)

    elif ForGunePortal.GuneCommunityFlagAndVariables.fromGuneCommunityToGuneMainPortalPage:
        ForGunePortal.GuneCommunityFlagAndVariables.fromGuneCommunityToGuneMainPortalPage = False
        forGunePortal(update, context)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromDocumetnsSharedPhysicallYpanelToDocumentManipulationPage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromDocumetnsSharedPhysicallYpanelToDocumentManipulationPage = False
        ForGunePortal.GuneShare().listMenuProviderForSharedDocumentsMangingPAGE(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGetRequestToSharedDocuementPage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGetRequestToSharedDocuementPage = False
        ForGunePortal.GuneShare().listProvideForSharedDocumentsPage(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromPhysicallDocToGetDocumentPage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromPhysicallDocToGetDocumentPage = False
        ForGunePortal.GuneShare().listProviderForGetDocumentsInSharedDocumentPage(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromSoftCopyShowingToGetDocumentsPage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromSoftCopyShowingToGetDocumentsPage = False
        ForGunePortal.GuneShare().listProviderForGetDocumentsInSharedDocumentPage(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGetDocumentsToSharedDocumentsPage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGetDocumentsToSharedDocumentsPage = False
        ForGunePortal.GuneShare().listProvideForSharedDocumentsPage(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromSharedDocumentsToGunesharePage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromSharedDocumentsToGunesharePage = False
        ForGunePortal.GuneShare().GuneShareMainPageListProvider(update, bot)

    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromManagingDocuemtToGuneSharePage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromManagingDocuemtToGuneSharePage = False
        ForGunePortal.GuneShare().GuneShareMainPageListProvider(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromDocumentInformationRetriverToShariningDocumentPage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromDocumentInformationRetriverToShariningDocumentPage = False
        ForGunePortal.GuneShare().listProviderForShareDocumentPage(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromShareDocumentLandingPageToGuneSharePage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromShareDocumentLandingPageToGuneSharePage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGuneMainPageToGunePortalMainPage = True
        ForGunePortal.GuneShare().GuneShareMainPageListProvider(update, bot)
    elif ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGuneMainPageToGunePortalMainPage:
        ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagFromGuneMainPageToGunePortalMainPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GunePortalMain().listProviderIfAlreadyCommunityMember()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)


    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFromSuggestionAddertoNormalUserPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromSuggestionAddertoNormalUserPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForEnteringSuggestionBookName = False
        replkbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnNormalUser()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForNormalUserReviewViewingPageToNormalUsrPanel:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForNormalUserReviewViewingPageToNormalUsrPanel = False
        replkbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnNormalUser()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)

    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFromSendAlertToAdmingLandingPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromSendAlertToAdmingLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromVoteCotrollingMaintoAdminMainPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromPeoplesSuggestionToAdminLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnAdmin()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFromResultOfVotePageToVoteControlingPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromResultOfVotePageToVoteControlingPage = False
        ForGunePortal.GuneOfficialReviews().voteControllingPanelMenuProvider(update, bot)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFromOpennVotePageToVoteControlingPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromOpennVotePageToVoteControlingPage = False
        ForGunePortal.GuneOfficialReviews().voteControllingPanelMenuProvider(update, bot)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFromVoteCotrollingMaintoAdminMainPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromVoteCotrollingMaintoAdminMainPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromPeoplesSuggestionToAdminLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnAdmin()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFromPeoplesSuggestionToAdminLandingPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromPeoplesSuggestionToAdminLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnAdmin()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFortraversingFromuploaingfinshedtorecviewManipualtionPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagFortraversingFromuploaingfinshedtorecviewManipualtionPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = True
        ForGunePortal.GuneOfficialReviews().MonthlyreviewMenuListProvider(update)

    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu:
        # this for for gune portal to common main menu
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        afterApproval(update, context)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView:
        # for register and back button to common main menu
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        afterApproval(update, context)
    elif ForGunePortal.GunePortalFlagAndVaraibles().flagForGunePortalAdminControlPanel:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnAdmin()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage:
        # from admin landling page   to commun gune portal view
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        registeringNewCustomer(update, context, False)
    elif ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage:
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnAdmin()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)


def TextCommandsHandler(update: Update, context: CallbackContext):
    global flagForNameName, flagForTheLanguageOfTheBook, typeofcatagory, flagForNameOfTheBook, nameOfTheBook, flagForNameOFLocation, userName, usertelegramID, usercurrentLocation, userNameFullName, flagForUsingDefaultName, flagForLocationSpecification, flagForOtherSpecificationCatgoryOfTheBook
    global flagForCurrentPrice, flagForPublicationYearOfTheBook, flagForNumberOfEditionOfTheBook, flagForStatusOfTheBook
    global flagForPortalChoose, flagForYesNoReviewRegistereing
    global RviewedPresenter, flagForYesNoReviewRegistereing, ActualDocument, NumberOfpages, ReviewDetailDiscription, publisherName, NameOfSeminar, NameOfTheDocument, DateAndTimeTheReviewHeld

    currenTextCommand = update.message.text
    if currenTextCommand == "Normal View":
        ForGunePortal.GunePortalFlagAndVaraibles.flagForFromNormalViewAdminViewToNormalViewUsers = True
        replkbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnNormalUser()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)

    elif currenTextCommand == "Physical Document":
        ForGunePortal.GuneShare().forRetrivingAllPhysicalDocuments(update, bot)
    elif currenTextCommand == "Soft Copies":
        ForGunePortal.GuneShare().ForRetrivingAllSoftCopiesDocuments(update, bot)
    elif currenTextCommand == "Get Documents":
        ForGunePortal.GuneShare().listProviderForGetDocumentsInSharedDocumentPage(update, bot)
    elif currenTextCommand == "Get Requests":
        ForGunePortal.GuneShare().RequestsRecieveHanling(update, bot)
    elif currenTextCommand == "Shared Documents":
        ForGunePortal.GuneShare().listProvideForSharedDocumentsPage(update, bot)
    elif currenTextCommand == "Books Shared Physically":

        ForGunePortal.GuneShare().alreadyBorrowedBooksControlingPage(update, bot)
    elif currenTextCommand == "View":
        ForGunePortal.GuneShare().ViewAllTheDocuments(update, bot)
    elif currenTextCommand == "Delete":
        ForGunePortal.GuneShare().InlineListProviderOfDocuments(update, bot, 1)
    elif currenTextCommand == "Manage Document":
        ForGunePortal.GuneShare().listMenuProviderForSharedDocumentsMangingPAGE(update, bot)
    elif currenTextCommand == "SoftCopy":
        if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument = False
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForChoosenISSoftCopyAccessebility = True
            ForGunePortal.GuneShare().InlineListProviderOfDocuments(update, bot, 3)
        else:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForSharingSoftCopy = True
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.statusOfTheDocument = currenTextCommand
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 10)
    elif currenTextCommand == "Physically":
        if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument = False
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagIfChoosenIsIsPhysicallAccessebility = True
            ForGunePortal.GuneShare().InlineListProviderOfDocuments(update, bot, 3)

        else:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForPhysicallySahring = True
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.statusOfTheDocument = currenTextCommand
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 11)
    elif currenTextCommand == "Discard":
        ForGunePortal.GuneShare().listProviderForShareDocumentPage(update, bot)
    elif currenTextCommand == "Private":
        if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument = False
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.typeAccessbelityChoosen = "Private"
            ForGunePortal.GuneShare().InlineListProviderOfDocuments(update, bot, 2)
        else:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForPrivateDocumentRegistering = True
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 1)

    elif currenTextCommand == "Public":
        if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument = False
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.typeAccessbelityChoosen = "Public"
            ForGunePortal.GuneShare().InlineListProviderOfDocuments(update, bot, 2)
        else:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForPublicDocumentRegistering = True
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 1)
    elif currenTextCommand == "Share Document":
        ForGunePortal.GuneShare().listProviderForShareDocumentPage(update, bot)
    elif currenTextCommand == "Vote On Suggestion":
        ForGunePortal.GuneOfficialReviews().VoteOnActiveSuggestions(update, bot)
    elif currenTextCommand == "No, Don't save it":
        replkbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnNormalUser()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)
    elif currenTextCommand == "Yes,save it":
        ForGunePortal.GuneOfficialReviews().SuggestionAdderForNextMonthReviewSeminar(update, bot, 6)
    elif currenTextCommand == "Add Suggesstion":
        ForGunePortal.GuneOfficialReviews().SuggestionAdderForNextMonthReviewSeminar(update, bot, 1)
    elif currenTextCommand == "View This Month Review":
        ForGunePortal.GuneOfficialReviews().CurrentMonthReviewingPageForNormalUser(update, bot)

    elif currenTextCommand == "No Don't send":
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromPeoplesSuggestionToAdminLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
        replyKbd = ForGunePortal.GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnAdmin()
        update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
    elif currenTextCommand == "Yes,send to all":
        ForGunePortal.GuneOfficialReviews().BrodacastNoticeToAllGuneCommunity(ShortNotice, update, bot)
    elif currenTextCommand == "Send Alert":
        ForGunePortal.GuneOfficialReviews().sendAlert(update, bot)
    elif currenTextCommand == "Result On Votes":
        ForGunePortal.GuneOfficialReviews().VoteResultViewingPage(update, bot)
    elif currenTextCommand == "Open Votes":
        ForGunePortal.GuneOfficialReviews().VoteOpeningPage(update, bot)
    elif currenTextCommand == "Vote Controlling Panel":
        ForGunePortal.GuneOfficialReviews().voteControllingPanelMenuProvider(update, bot)
    elif currenTextCommand == "Peoples Suggestions":
        ForGunePortal.GuneOfficialReviews().PeoplesSuggestionManipulator(bot, update)
    elif currenTextCommand == "Delete Review":
        update.message.reply_text(text="Choose Which Review You Want To Delete", reply_markup=ReplyKeyboardRemove())
        ForGunePortal.GuneOfficialReviews().DeleteMonthlyReview(update)
    elif currenTextCommand == "Add Review":
        ForGunePortal.GuneOfficialReviews().NewReviewAdder1(update, bot, 1)
    elif currenTextCommand == "Update Review":
        ForGunePortal.GuneOfficialReviews().reviewupdatingPage(update)
    elif currenTextCommand == "Add This Month Reviews":
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
        ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = True
        ForGunePortal.GuneOfficialReviews().MonthlyreviewMenuListProvider(update)
    elif currenTextCommand == "Grant Privillage":
        ForGunePortal.GuneOfficialReviews().GrantingPrivillage(update)
    elif currenTextCommand == "Revoke Privillage":
        ForGunePortal.GuneOfficialReviews().RevokePrieviallge(update)
    elif currenTextCommand == "Admin Control Panel":
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = True
        ForGunePortal.GuneOfficialReviews().adminControlPanel(update)
    elif currenTextCommand == "Register":
        registeringNewCustomer(update, context, True)
    elif currenTextCommand == "Gune Official Reviews":
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = True
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GuneOfficialReviews().FunctionCheckkingThatAuserIsAnAdmin(str(update.effective_user.id), update)
    elif currenTextCommand == "Gune Share":
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
        ForGunePortal.GuneShare().GuneShareMainPageListProvider(update, bot)

    elif currenTextCommand == "Gune Community Reviews":
        ForGunePortal.GuneCommunity().MonthInlineRetriver(update, bot)
        ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False

    elif currenTextCommand == "<- Back":
        functionHandlesBackwardtraversal(update, context)
    elif currenTextCommand == "Amharic":
        UserAccountHandler().CreateAnAccountMessage(update)
        # languageHandler(update, context)
    elif currenTextCommand == "Yes, I Want To Edit":
        customizedBookAdder(update, context)  # this function used by two
    elif currenTextCommand == "No, I Don't":
        PersonalBookInformationManipualtion(update, context)
    elif currenTextCommand == "Sure Do u Want Delete":
        import DataBaseConnectivity
        global forDeletingBookID
        DataBaseConnectivity.SpecificBookDeleter(update.effective_user.id, forDeletingBookID)
    elif currenTextCommand == "No, I Don't want Delete":
        pass
    elif currenTextCommand == "Other Country":
        forSpecificCountry(update, context)
    elif currenTextCommand == "Suggestions For This Month":
        pass
    elif currenTextCommand == "\U0001F4DA Gune Portal":
        if ForGunePortal.GunePortalMain().AccountCecker(str(update.effective_user.id)):
            ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = True
            ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
            replyKbd = ForGunePortal.GunePortalMain().listProviderIfAlreadyCommunityMember()
            update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
        else:
            ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = True
            ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False

            replyKbd = ForGunePortal.GunePortalMain().listProviderIfNotCommunityMember()
            update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)

        # forGunePortal(update, context)
    elif currenTextCommand == "\U0001F30D Global Portal":
        forGlobalPort(update, context)
    elif currenTextCommand == "Fiction":
        if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingTypeOfTheBook:
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 4)
        else:
            ForChoosingLocationInlinKeyBoard(update, context)
    elif currenTextCommand == "Non-Fiction":
        if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.forReceivingTypeOfTheBook:
            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 5)
        else:
            ForChooseingNonFicition(update, context)
    elif currenTextCommand == 'English':
        UserAccountHandler().CreateAnAccountMessage(update)
        # languageHandler(update, context)
    elif currenTextCommand == "YES,am ready!":
        CountryListProvider(update, context)
    elif currenTextCommand == "Yes":
        if ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForPrivateDocumentRegistering or ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForPublicDocumentRegistering:
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForPrivateDocumentRegistering  = False
            ForGunePortal.GunePortalForGuneShareFlagsAndVariables.flagForPublicDocumentRegistering = False

            ForGunePortal.GuneShare().DocumentInformationRetriver(update, bot, 12)
        elif ForGunePortal.GunePortalFlagAndVaraibles.flagForUpdaterIndicaterToDistiguishFromAdder:
            ForGunePortal.GunePortalFlagAndVaraibles.flagForUpdaterIndicaterToDistiguishFromAdder = False
            flagForYesNoReviewRegistereing = False
            ForGunePortal.GunePortalFlagAndVaraibles.flagFortraversingFromuploaingfinshedtorecviewManipualtionPage = False
            ForGunePortal.GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
            ForGunePortal.GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = True
            ForGunePortal.GuneOfficialReviews().MonthlyreviewMenuListProvider(update)
            import datetime
            dcitForRegistering = {
                "ActualDocument": ActualDocument,
                "DocumentId": DocumentId,
                "NameOfSeminar": NameOfSeminar,
                "NameOfTheDocument": NameOfTheDocument,
                "DateAndTimeTheReviewHeld": DateAndTimeTheReviewHeld,
                "publisherName": publisherName,
                "NumberOfpages": NumberOfpages,
                "RviewedPresenter": RviewedPresenter,
                "ReviewDetailDiscription": ReviewDetailDiscription,
                "CurrentDate": str(datetime.datetime.now().month) + "," + datetime.datetime.now().strftime("%d")
            }

            import DataBaseConnectivity
            global timsestampFormonthlyreview

            if DataBaseConnectivity.SeminarReviews().UpdateMonthlyReview(dcitForRegistering,
                                                                         "-" + timsestampFormonthlyreview):
                update.message.reply_text(text="You Have Successfully Updates Information")
            else:
                update.message.reply_text(text="Can't Be Updated")

        elif flagForYesNoReviewRegistereing:
            flagForYesNoReviewRegistereing = False
            import datetime
            dcitForRegistering = {
                "ActualDocument": ActualDocument,
                "DocumentId": DocumentId,
                "NameOfSeminar": NameOfSeminar,
                "NameOfTheDocument": NameOfTheDocument,
                "DateAndTimeTheReviewHeld": DateAndTimeTheReviewHeld,
                "publisherName": publisherName,
                "NumberOfpages": NumberOfpages,
                "RviewedPresenter": RviewedPresenter,
                "ReviewDetailDiscription": ReviewDetailDiscription,
                "CurrentDate": str(datetime.datetime.now().month) + "," + datetime.datetime.now().strftime("%d")
            }

            import DataBaseConnectivity
            val = DataBaseConnectivity.SeminarReviews().uploadthismonthReview(dcitForRegistering)
            if val:
                r = [[KeyboardButton("<- Back")]]
                ForGunePortal.GunePortalFlagAndVaraibles.flagFortraversingFromuploaingfinshedtorecviewManipualtionPage = True
                rep = ReplyKeyboardMarkup(r, resize_keyboard=True)
                update.message.reply_text("Successfully Uploaded", reply_markup=rep)
            else:
                r = [[KeyboardButton("<- Back")]]
                rep = ReplyKeyboardMarkup(r, resize_keyboard=True)
                update.message.reply_text("Not Successfully Uploaded its because the review is already uploaded",
                                          reply_markup=rep)

        elif UserAccountHandler.flagForRegisteringNewUser:
            UserAccountHandler.flagForRegisteringNewUser = False
            import DataBaseConnectivity
            result = DataBaseConnectivity.writeToUserPersonalInformation(useTgId=str(update.effective_user.id),
                                                                         FullName=UserAccountHandler.FullName,
                                                                         userName=UserAccountHandler.UserName,
                                                                         PhoneNumber=UserAccountHandler.PhoneNumber,
                                                                         locationOfUser=UserAccountHandler.Location)
            if result:
                afterApproval(update, context)
            else:
                bot.send_message(update.effective_user.id, text="Make Sure You Enter Valid Information")
            usercurrentLocation = userName = userNameFullName = usertelegramID = ""

    elif currenTextCommand == "\U0001F4D5 Books List":
        BooksFtecherFromDatabase(update, context)
    elif currenTextCommand == "\U0001F4C4  List of My Booksl":
        personalUploadedBooksInlineButtonRetriver(update, context, "0-")
    elif currenTextCommand == "\U0001F195 Add new Book":
        ForGlobalPortalFlagAndVariables.fromMyBooksManipulationToFirstPage = False
        customizedBookAdder(update, context)
        flagForNameOfTheBook = True

    elif currenTextCommand == "\U0001F4AC Update Book infn":
        EditingBookInformation(update, context)
    elif currenTextCommand == "🛑 Delete book":
        BookDeleter(update, context)
    elif currenTextCommand == "\U0001F4DA  Global Portal":
        PersonalBookInformationManipualtion(update, context)
    elif currenTextCommand == "\U0001F468 Profile":
        ProfileManipulation().PersonalInformationRetriver(update)

    elif currenTextCommand == "🔍 Search For Books":
        forSearchingBooks(update, context)
    elif currenTextCommand == "No":
        UserAccountHandler().CreateAnAccountMessage(update)
    elif currenTextCommand == "Create An Account":
        AccountHandler(update, context)
    else:

        AllConditionsForRegisteringAllBookInformation(update, context, currenTextCommand)


#          u need to store it in database
dispatcher.add_handler(CommandHandler("x", forGlobalPort))
dispatcher.add_handler((CommandHandler("xo", afterApproval)))
dispatcher.add_handler((CommandHandler("start", start)))
dispatcher.add_handler(MessageHandler(Filters.text, TextCommandsHandler))
dispatcher.add_handler(
    MessageHandler(Filters.contact, UserAccountHandler().PhoneNumberFromTelgramAutomaticallyRetriver))
dispatcher.add_handler(MessageHandler(Filters.document, documnetHandler))

updater.dispatcher.add_handler(CallbackQueryHandler(inlineQueryHandler))

updater.start_polling()
updater.idle()
"""
            TODO
                extract text
                 rawtext--> the extracted text
                upload file to storage ->
                    onsuccess -> 
                        get path -> 
                            create official review object like officialReview(ActualDocumentpath , reviewer path ... )
                                -> push the created object like DatabaseReference.child('officialReviews').push(officialReview)
                                    -> on succes show message 'review submitted successfully'
                To view official review
                    first get all the official reviews from DatabaseReference.child('officialReviews');
                        -> iterate through all
                            -> for each official review
                                ->get the path of the doc and other attributes
                                    -> get the doc from storage by the path of the obj
                                        -> display the text from doc by reading file
                                            -> display th review                          
        """
