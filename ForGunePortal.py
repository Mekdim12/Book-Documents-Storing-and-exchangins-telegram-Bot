import DataBaseConnectivity
from telegram import *


class GuneOfficialReviews:
    def VoteOnActiveSuggestions(self, update: Update, bot):
        import DataBaseConnectivity
        opendVotes = DataBaseConnectivity.VoteHandler().VoteResultRetriver()
        if opendVotes is not None:
            CustomeKeyborad = [
                [KeyboardButton("<- Back")]
            ]
            replKbd = ReplyKeyboardMarkup(CustomeKeyborad, resize_keyboard=True)
            bot.send_message(update.effective_user.id, text="Place Your Vote By Tapping ur botSign",
                             reply_markup=replKbd)
            GunePortalFlagAndVaraibles.flagFromVotingPageToNormalUserView = True

            for key in opendVotes:
                currentSuggestion = opendVotes[key]
                NameOfTheBook = currentSuggestion["NameOfTheBook"]
                NameOfTheAuthor = currentSuggestion["NameOfTheAuthor"]
                ActualDocument = currentSuggestion["ActualDocument"]
                DocumnetId = currentSuggestion["DocumnetId"]
                Discription = currentSuggestion["Discription"]
                usenameofsuggester = currentSuggestion["usenameofsuggester"]

                bot.send_document(update.effective_user.id, DocumnetId)
                textForRetriving = "\n\U0001F4DA	 Name OF The Book : " + NameOfTheBook + "\n" + \
                                   "\U0001F4D5 Book Author : " + NameOfTheAuthor + "\n" + \
                                   "\U0001F481 Suggestion : " + usenameofsuggester + "\n" + \
                                   "\U0001F449 Discription :" + Discription
                import DataBaseConnectivity

                CustomeInlineKeyBorad = [
                    [InlineKeyboardButton(
                        "\U0001F44D " + str(DataBaseConnectivity.VoteHandler().voteResultRetriver(str(key), 1)),
                        callback_data="20~" + str(key) + "~" + str(update.effective_user.id)),
                        InlineKeyboardButton(
                            "\U0001F44E " + str(DataBaseConnectivity.VoteHandler().voteResultRetriver(str(key), 2)),
                            callback_data="21~" + str(key) + "~" + str(update.effective_user.id))],
                ]
                replyInlineKbd = InlineKeyboardMarkup(CustomeInlineKeyBorad)
                bot.send_message(update.effective_user.id, text=textForRetriving, reply_markup=replyInlineKbd)

        else:
            bot.send_message(update.effective_user.id, text="There is Opened Vote To Show")

    def SuggestionAdderForNextMonthReviewSeminar(self, update: Update, bot, flag):
        if flag == 1:
            CustomeList = [[KeyboardButton("<- Back")]]
            replKbd = ReplyKeyboardMarkup(CustomeList, resize_keyboard=True)
            bot.send_message(update.effective_user.id, text="Enter The Book Name You Want To Suggest?",
                             reply_markup=replKbd)
            GunePortalFlagAndVaraibles.flagFromSuggestionAddertoNormalUserPage = True
            GunePortalFlagAndVaraibles.flagForEnteringSuggestionBookName = True
        elif flag == 2:
            bot.send_message(update.effective_user.id, text="Enter The Book's Author?")
            GunePortalFlagAndVaraibles.flagForEnteringNameOfTheAuthor = True
        elif flag == 3:
            bot.send_message(update.effective_user.id, text="Enter The Brief Description About Book?")
            GunePortalFlagAndVaraibles.flagForEnteringDiscriptionOnSuggestion = True
        elif flag == 4:
            GunePortalFlagAndVaraibles.flagForEnteringActualSuggestionDocumnet = True
            bot.send_message(update.effective_user.id, text="Attach The Document U are Suggesting?")
        elif flag == 5:
            import DataBaseConnectivity
            CustomKbd = [
                [KeyboardButton("Yes,save it"), KeyboardButton("No, Don't save it")]
            ]
            replKbd = ReplyKeyboardMarkup(CustomKbd, resize_keyboard=True)

            textforRetriving = \
                "\U0001F449 Discription :" + GunePortalFlagAndVaraibles.discriptionofsuggestion + "\n" + \
                "\U0001F447 DownVote :" + '0' + "\n" + \
                "\U0001F464 NameOfTheAuthor :" + GunePortalFlagAndVaraibles.nameofauthourofthebook + "\n" + \
                "\U0001F4D5 NameOfTheBook :" + GunePortalFlagAndVaraibles.nameofSuggestedNameOfTheBook + "\n" + \
                "\U0001F44E UpVote :" + '0' + "\n" + \
                "\U0001F464 usenameofsuggester :" + DataBaseConnectivity.PersonalAccountHandler().UserNameRetriver(
                    str(update.effective_user.id)) + "\n" + \
                "Are You Sure Do You Want To Continue?"

            bot.send_message(update.effective_user.id, text=textforRetriving, reply_markup=replKbd)
        elif flag == 6:
            import DataBaseConnectivity
            dataToBeStored = {
                "ActualDocument": GunePortalFlagAndVaraibles.actualDocument,
                "Discription": GunePortalFlagAndVaraibles.discriptionofsuggestion,
                "DocumnetId": GunePortalFlagAndVaraibles.documentId,
                "DownVote": {"100": "0"},
                "NameOfTheAuthor": GunePortalFlagAndVaraibles.nameofauthourofthebook,
                "NameOfTheBook": GunePortalFlagAndVaraibles.nameofSuggestedNameOfTheBook,
                "UpVote": {"100": "0"},
                "usenameofsuggester": DataBaseConnectivity.PersonalAccountHandler().UserNameRetriver(
                    str(update.effective_user.id))
            }
            indicator = DataBaseConnectivity.CommuntitySuggestionHandler().suggestionadder(dataToBeStored)
            if indicator:
                bot.send_message(update.effective_user.id, text="Successfully Suggestion Added")

                GunePortalFlagAndVaraibles.flagForEnteringSuggestionBookName = False
                replkbd = GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnNormalUser()
                update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)
            else:
                bot.send_message(update.effective_user.id, text=" Suggestion can't be Add")
                GunePortalFlagAndVaraibles.flagForEnteringSuggestionBookName = False
                replkbd = GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnNormalUser()
                update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)

    def CommentOnReviewsHandler(self, Comment, update: Update, bot, month, idOfReview):
        import DataBaseConnectivity
        flag = DataBaseConnectivity.SeminarReviews().MonthlyReviewCommentAdder(comment=Comment, month=month,
                                                                               userID=str(update.effective_user.id),
                                                                               timestampid=idOfReview)
        if flag:
            bot.send_message(update.effective_user.id,
                             text="1 Comment Added \n If U Want To Add Mpre Comment Press Add Comment \U0001F446	")
        else:
            bot.send_message(update.effective_user.id, text="You Can't Comment On Current Review")

    def CurrentMonthReviewingPageForNormalUser(self, update: Update, bot):
        CustomeKeyBoard = [
            [KeyboardButton("<- Back")]
        ]
        replkbd = ReplyKeyboardMarkup(CustomeKeyBoard, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="\U0001F447 \U0001F447 \U0001F447 \U0001F447",
                         reply_markup=replkbd)
        GunePortalFlagAndVaraibles.flagForNormalUserReviewViewingPageToNormalUsrPanel = True

        import DataBaseConnectivity
        reviewsData = DataBaseConnectivity.SeminarReviews().montlyReviewRetriver()
        if reviewsData is not None:
            for idTimeStamp in reviewsData:
                ContentsOFInformation = reviewsData[idTimeStamp]
                actulDocument = ContentsOFInformation["ActualDocument"]
                documnentId = ContentsOFInformation["DocumentId"]
                CurrentDate = ContentsOFInformation["CurrentDate"]
                DateAndTimeTheReviewHeld = ContentsOFInformation["DateAndTimeTheReviewHeld"]
                NameOfSeminar = ContentsOFInformation["NameOfSeminar"]
                NameOfTheDocument = ContentsOFInformation["NameOfTheDocument"]
                NumberOfpages = ContentsOFInformation["NumberOfpages"]
                ReviewDetailDiscription = ContentsOFInformation["ReviewDetailDiscription"]
                RviewedPresenter = ContentsOFInformation["RviewedPresenter"]
                publisherName = ContentsOFInformation["publisherName"]

                bot.send_document(update.effective_user.id, documnentId)

                textForRetretriving = "\U0001F4D5 Name Of The Seminar :" + NameOfSeminar + "\n" + \
                                      "\U0001F4D5 Name Of The Document :" + NameOfTheDocument + "\n" + \
                                      "\U0001F4D5Number Of Pages :" + NumberOfpages + "\n" + \
                                      "\U0001F464 Publisher Name :" + publisherName + "\n" + \
                                      "\U0001F464 Presented By:" + RviewedPresenter + "\n" + \
                                      "\U0000231B	Date The Seminar is held :" + DateAndTimeTheReviewHeld + "\n" + \
                                      "\U0001F449	Description :" + ReviewDetailDiscription + "\n"
                monthh = CurrentDate.split(",")
                CustomeInlienKbd = [
                    [InlineKeyboardButton("Add Comment", callback_data="19~" + str(monthh[0]) + "~" + idTimeStamp)]]
                replInlineKbd = InlineKeyboardMarkup(CustomeInlienKbd)
                bot.send_message(update.effective_user.id, text=textForRetretriving, reply_markup=replInlineKbd)


        else:
            bot.send_message(update.effective_user.id,
                             text="There is no Review For This Month Published will keep u posted!")

    def BrodacastNoticeToAllGuneCommunity(self, notice, update: Update, bot):
        import DataBaseConnectivity
        accounts = DataBaseConnectivity.PersonalAccountHandler().AccountChecker()
        if accounts is not None:
            for userid in accounts.values():
                bot.send_message(str(userid), text=notice)
            GunePortalFlagAndVaraibles.flagFromVoteCotrollingMaintoAdminMainPage = False
            GunePortalFlagAndVaraibles.flagFromPeoplesSuggestionToAdminLandingPage = False
            GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = True
            GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = False
            GunePortalFlagAndVaraibles.flagForGunePortalAdminControlPanel = False
            GunePortalFlagAndVaraibles.flagForGunePortalmainMenu = False
            GunePortalFlagAndVaraibles.flagForGunePortalRegitseringView = False
            replyKbd = GuneOfficialReviews().listProviderIfTheCurrentPrivillageisAnAdmin()
            update.message.reply_text(text="Choose How u want to proceed", reply_markup=replyKbd)
        else:
            bot.send_message(update.effective_user.id, text="There is No Gune Community Member Registred So Far")

    def sendAlert(self, update: Update, bot):
        CustomeKeybs = [
            [KeyboardButton("<- Back")]
        ]
        resplykbd = ReplyKeyboardMarkup(CustomeKeybs, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Please Enter Full Discription About The Notice",
                         reply_markup=resplykbd)
        GunePortalFlagAndVaraibles.flagFromSendAlertToAdmingLandingPage = True
        GunePortalFlagAndVaraibles.flagForWritingANoticeForCommunityAsBroadcastMessage = True

    def VoteResultViewingPage(self, update: Update, bot):
        import DataBaseConnectivity
        opendVotes = DataBaseConnectivity.VoteHandler().VoteResultRetriver()

        if opendVotes is not None:
            CustomeKbd = [[KeyboardButton("<- Back")]]
            replKbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
            bot.send_message(update.effective_user.id,
                             text="U can See the result below \U0001F447 \U0001F447	\U0001F447 \U0001F447",
                             reply_markup=replKbd)
            GunePortalFlagAndVaraibles.flagFromResultOfVotePageToVoteControlingPage = True
            for key in opendVotes:
                currentSuggestion = opendVotes[key]
                NameOfTheBook = currentSuggestion["NameOfTheBook"]
                NameOfTheAuthor = currentSuggestion["NameOfTheAuthor"]
                ActualDocument = currentSuggestion["ActualDocument"]
                DocumnetId = currentSuggestion["DocumnetId"]
                UpVote = currentSuggestion["UpVote"]
                DownVote = currentSuggestion["DownVote"]
                Discription = currentSuggestion["Discription"]
                usenameofsuggester = currentSuggestion["usenameofsuggester"]

                # here u need to show the file first before u going to show other information

                bot.send_document(update.effective_user.id, DocumnetId)
                textForRetriving = "\U0001F464 Name OF The Book : " + NameOfTheBook + "\n" + \
                                   "\U0001F4D5 Book Author : " + NameOfTheAuthor + "\n" + \
                                   "\U0001F449 Suggestion : " + usenameofsuggester + "\n" + \
                                   "\U0001F449 Discription :" + Discription

                if DownVote == {'100': "0"}:
                    DownVote = 0
                else:
                    DownVote = len(list(DownVote.keys()))

                if UpVote == {'100': "0"}:
                    UpVote = 0
                else:
                    UpVote = len(list(UpVote.keys()))



                CustomeInlineKeyBorad = [
                    [InlineKeyboardButton("\U0001F44D " + str(UpVote), callback_data="17-" + "where-" + "17"),
                     InlineKeyboardButton("\U0001F44E " + str(DownVote), callback_data="17-" + "where-" + "17")],
                    [InlineKeyboardButton("Close vote", callback_data="18~" + str(key) + "~18")]
                ]
                replyInlineKbd = InlineKeyboardMarkup(CustomeInlineKeyBorad)
                bot.send_message(update.effective_user.id, text=textForRetriving, reply_markup=replyInlineKbd)

        else:
            bot.send_message(update.effective_user.id, text="There is Opened Vote To Show")

    def VoteOpeningPage(self, update: Update, bot):
        CustomeKbd = [
            [KeyboardButton("<- Back")]
        ]
        replykbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Chosse from which month u want to open vote",
                         reply_markup=replykbd)
        GunePortalFlagAndVaraibles.flagFromOpennVotePageToVoteControlingPage = True
        listOFmonthsRegistred = DataBaseConnectivity.CommuntitySuggestionHandler().listofApprovedSuggestionProvider()
        if listOFmonthsRegistred is not None:
            Customkbd = []
            templist = []
            counter = 0
            for month in listOFmonthsRegistred:
                if counter == 1:
                    templist.append(InlineKeyboardButton(text=month, callback_data="14-" + month + "-14"))
                    Customkbd.append(templist)
                    templist = []
                    counter = 0
                else:
                    templist.append(InlineKeyboardButton(text=month, callback_data="14-" + month + "-14"))
                    counter += 1

            if counter == 1:
                Customkbd.append(templist)
            replInlinekbd = InlineKeyboardMarkup(Customkbd)

            bot.send_message(update.effective_user.id, text="\U0001F449\U0001F449\U0001F449",
                             reply_markup=replInlinekbd)
        else:
            bot.send_message(update.effective_user.id, text="There Is No Any Suggestion Given So far")

    def voteControllingPanelMenuProvider(self, update: Update, bot):
        CustomeKbd = [
            [KeyboardButton("Open Votes"), KeyboardButton("Result On Votes")],
            [KeyboardButton("<- Back")]
        ]
        replKbf = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose What U are going to next?", reply_markup=replKbf)
        GunePortalFlagAndVaraibles.flagFromVoteCotrollingMaintoAdminMainPage = True

    def PeoplesSuggestionManipulator(self, bot, update: Update):
        GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
        GunePortalFlagAndVaraibles.flagFromPeoplesSuggestionToAdminLandingPage = True

        CustomeKbd = [[KeyboardButton("<- Back")]]
        replKbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose Which month Suggestion u Want To get",
                         reply_markup=replKbd)

        listOFmonthsRegistred = DataBaseConnectivity.CommuntitySuggestionHandler().listOfSuggestionMonthProvider()

        if listOFmonthsRegistred is not None:
            Customkbd = []
            templist = []
            counter = 0
            for month in listOFmonthsRegistred:
                if counter == 1:
                    templist.append(InlineKeyboardButton(text=month, callback_data="10-" + month + "-10"))
                    Customkbd.append(templist)
                    templist = []
                    counter = 0
                else:
                    templist.append(InlineKeyboardButton(text=month, callback_data="10-" + month + "-10"))
                    counter += 1

            if counter == 1:
                Customkbd.append(templist)
            replInlinekbd = InlineKeyboardMarkup(Customkbd)

            bot.send_message(update.effective_user.id, text="\U0001F449\U0001F449\U0001F449",
                             reply_markup=replInlinekbd)
        else:
            bot.send_message(update.effective_user.id, text="There Is No Any Suggestion Given So far")

    def reviewupdatingPage(self, update: Update):

        data = DataBaseConnectivity.SeminarReviews().montlyReviewRetriver()

        if data is not None:
            MainList = []
            templist = []
            counter = 0
            for timestamp in data.keys():
                datas = data[timestamp]
                str = (data[timestamp])["NameOfTheDocument"]

                if counter == 1:
                    templist.append(InlineKeyboardButton(str, callback_data="9-" + timestamp + "-" + (data[timestamp])[
                        "NameOfTheDocument"]))
                    MainList.append(templist)
                    templist = []
                    counter = 0
                else:
                    templist.append(InlineKeyboardButton(str, callback_data="9-" + timestamp + "-" + (data[timestamp])[
                        "NameOfTheDocument"]))
                    counter += 1
            if counter == 1:
                MainList.append(templist)

            replkbd = InlineKeyboardMarkup(MainList)
            update.message.reply_text(text="Choose Posted Reviews", reply_markup=replkbd)
        else:
            update.message.reply_text(text="There is No Review To Be Updated")

    def NewReviewAdder1(self, update: Update, bot, fg):
        if fg == 1:
            bot.send_message(update.effective_user.id,
                             text="Attachment The Document u want it to Upload using Attachement sign",
                             reply_markup=ReplyKeyboardRemove())

            GunePortalFlagAndVaraibles.flagForAttachingReviewDocument = True
        elif fg == 2:
            bot.sendMessage(update.effective_user.id, "Enter The Seminar Tittle of This Month :")
            GunePortalFlagAndVaraibles.flagForSeminarTittle = True
        elif fg == 3:
            bot.sendMessage(update.effective_user.id, "Enter The Document/book Tittle of This Month :")
            GunePortalFlagAndVaraibles.flagForGuneReviewBookTittle = True
        elif fg == 4:
            bot.sendMessage(update.effective_user.id, "Enter Date The Review Held on")
            GunePortalFlagAndVaraibles.flagForDateReviewHold = True
        elif fg == 5:
            bot.sendMessage(update.effective_user.id, "Enter Publisher Full Name ")
            GunePortalFlagAndVaraibles.flagForDocumentPublsisher = True
        elif fg == 6:
            bot.sendMessage(update.effective_user.id, "Enter Number Of Pages ")
            GunePortalFlagAndVaraibles.flagForNumberOfPages = True
        elif fg == 7:
            bot.sendMessage(update.effective_user.id, "Enter Detail Discription And Peoples Comments Here")
            GunePortalFlagAndVaraibles.flagForDiscriptionOnThreReview = True
        elif fg == 8:
            bot.sendMessage(update.effective_user.id, "Enter who presented On The Seminar")
            GunePortalFlagAndVaraibles.flagForReviewPresenter = True

    def FunctionCheckkingThatAuserIsAnAdmin(self, telegramID, update: Update):
        if DataBaseConnectivity.RegisterNewUserAsAdmin().PrivillageChecker(telegramID):
            replkbd = self.listProviderIfTheCurrentPrivillageisAnAdmin()
            update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)
        else:
            replkbd = self.listProviderIfTheCurrentPrivillageisAnNormalUser()
            update.message.reply_text(text="Choose How u want to proceed", reply_markup=replkbd)

    def listProviderIfTheCurrentPrivillageisAnAdmin(self):
        CustomeKeyBoard = [
            [KeyboardButton("Admin Control Panel"), KeyboardButton("Add This Month Reviews")],
            [KeyboardButton("Peoples Suggestions"), KeyboardButton("Vote Controlling Panel")],
            [KeyboardButton("Normal View"), KeyboardButton("Send Alert")],
            [KeyboardButton("<- Back")]
        ]
        repKbd = ReplyKeyboardMarkup(CustomeKeyBoard, resize_keyboard=True, selective=True)
        return repKbd

    def listProviderIfTheCurrentPrivillageisAnNormalUser(self):
        CustomeKeyBoard = [
            [KeyboardButton("View This Month Review"), KeyboardButton("Add Suggesstion")],
            [KeyboardButton("Vote On Suggestion")],
            [KeyboardButton("<- Back")]
        ]
        repKbd = ReplyKeyboardMarkup(CustomeKeyBoard, resize_keyboard=True, selective=True)
        return repKbd

    def adminControlPanel(self, update: Update):
        Customekeyboard = [
            [KeyboardButton("Grant Privillage"), KeyboardButton("Revoke Privillage")],
            [KeyboardButton("<- Back")]
        ]
        replkbd = ReplyKeyboardMarkup(Customekeyboard, resize_keyboard=True)
        update.message.reply_text(text="choose what u are going to do?", reply_markup=replkbd)

    def PrivillageGrantingFuntion(self, Data, update: Update, bot):
        TgId = (Data.split('-'))[1]
        if DataBaseConnectivity.RegisterNewUserAsAdmin.RegisterNewUserAsAdmin(TgId):
            bot.send_message(update.effective_user.id, text="Successfully Account Granted From Admin Privllage")
        else:
            bot.send_message(update.effective_user.id, text="Account Can't Be registered As An Admin")

    def PrivillageRevokingFuntion(self, Data, update: Update, bot):
        TgId = (Data.split('-'))[1]
        if DataBaseConnectivity.RegisterNewUserAsAdmin().DeleteAdminPrivillage(TgId):
            bot.send_message(update.effective_user.id, text="Successfully Account Revoked From Admin Privllage")
        else:
            bot.send_message(update.effective_user.id, text="Account Can't Be Revoked!")

    def GrantingPrivillage(self, update: Update):
        values = DataBaseConnectivity.UserAccountsListProvider()
        var = DataBaseConnectivity.RegisterNewUserAsAdmin().ViewAdminAccountList()
        listOFFGuneCommunityMembers = DataBaseConnectivity.PersonalAccountHandler().AccoutListProvider()
        if values is not None and listOFFGuneCommunityMembers is not None:

            for i in listOFFGuneCommunityMembers.values():
                if var is not None:
                    if i not in var.values():
                        currentInfn = values[i]
                        Name = currentInfn["Full_Name"]
                        userName = currentInfn["User_Name"]
                        userName = "@" + userName
                        CustomeInlineKbd = [[InlineKeyboardButton(text="Grant Access", callback_data="5-" + i + "-5")]]
                        replKbd = InlineKeyboardMarkup(CustomeInlineKbd)
                        update.message.reply_text(text="Name =" + Name + "\n" + "User Name=" + userName,
                                                  reply_markup=replKbd)
                else:
                    currentInfn = values[i]
                    Name = currentInfn["Full_Name"]
                    userName = currentInfn["User_Name"]
                    userName = "@" + userName
                    CustomeInlineKbd = [[InlineKeyboardButton(text="Grant Access", callback_data="5-" + i + "-5")]]
                    replKbd = InlineKeyboardMarkup(CustomeInlineKbd)
                    update.message.reply_text(text="Name =" + Name + "\n" + "User Name=" + userName,
                                              reply_markup=replKbd)
        else:
            update.message.reply_text(text="There is No Member Of Gune Commmunity Registred So far")

    def RevokePrieviallge(self, update: Update):
        listOFadmins = DataBaseConnectivity.RegisterNewUserAsAdmin().ViewAdminAccountList()
        values = DataBaseConnectivity.UserAccountsListProvider()
        if listOFadmins is not None:
            for i in listOFadmins.values():
                currentUsrIndfn = values[i]
                Name = currentUsrIndfn["Full_Name"]
                userName = currentUsrIndfn["User_Name"]
                userName = "@" + userName
                CustomeInlineKbd = [[InlineKeyboardButton(text="Revoke Access", callback_data="6-" + i + "-6")]]
                replKbd = InlineKeyboardMarkup(CustomeInlineKbd)
                update.message.reply_text(text="Name =" + Name + "\n" + "User Name=" + userName, reply_markup=replKbd)
        else:
            update.message.reply_text(text="There is No Account Registerec As An Admin")

    def MonthlyreviewMenuListProvider(self, update: Update):
        CustomKeyBoard = [
            [KeyboardButton("Add Review"), KeyboardButton("Update Review"), KeyboardButton("Delete Review")],
            [KeyboardButton("<- Back")]
        ]
        replkbd = ReplyKeyboardMarkup(CustomKeyBoard, resize_keyboard=True)
        try:
            update.message.reply_text(text="Choose What U Want To Perform", reply_markup=replkbd)
        except:
            print("a, throwing an error am in admon review controol panel ")

    def DeleteMonthlyReview(self, update: Update):
        data = DataBaseConnectivity.SeminarReviews().montlyReviewRetriver()
        if data is not None:
            MainList = []
            templist = []
            counter = 0
            for timestamp in data.keys():
                datas = data[timestamp]
                str = (data[timestamp])["NameOfTheDocument"]

                if counter == 1:
                    templist.append(InlineKeyboardButton(str, callback_data="8-" + timestamp + "-" + (data[timestamp])[
                        "NameOfTheDocument"]))
                    MainList.append(templist)
                    templist = []
                    counter = 0
                else:
                    templist.append(InlineKeyboardButton(str, callback_data="8-" + timestamp + "-" + (data[timestamp])[
                        "NameOfTheDocument"]))
                    counter += 1
            if counter == 1:
                MainList.append(templist)

            replkbd = InlineKeyboardMarkup(MainList)
            update.message.reply_text(text="Choose Posted Reviews", reply_markup=replkbd)
        else:
            update.message.reply_text(text="There is No Review To Be Updated")
            GunePortalFlagAndVaraibles.flagFortraversingFromuploaingfinshedtorecviewManipualtionPage = False
            GunePortalFlagAndVaraibles.flagForGunePortalAdminLandingPage = False
            GunePortalFlagAndVaraibles.flagFromMonthlyReviewToAdminLandlingPage = True
            GuneOfficialReviews().MonthlyreviewMenuListProvider(update)

    def inlineKeyProviderForSuggester(self, listofsuggestion, startingIndex, endinIndex):
        if len(listofsuggestion) > 5:
            listofsuggestion = listofsuggestion[startingIndex:endinIndex]
            information = ""
            listforsingleinfn = []
            forReturningListHolder = []
            for infns in listofsuggestion:

                for deatil in infns[0:len(infns) - 1]:
                    information += "\n" + deatil
                listforsingleinfn.append(information)
                listforsingleinfn.append(infns[len(infns) - 1])

                forReturningListHolder.append(listforsingleinfn)
                listforsingleinfn = []
                information = ""
            forReturningListHolder.append(str(endinIndex))
            return forReturningListHolder
        else:
            listofsuggestion = listofsuggestion[startingIndex:]
            information = ""
            listforsingleinfn = []
            forReturningListHolder = []
            counter = 0
            for infns in listofsuggestion:

                for deatil in infns[0:len(infns) - 1]:
                    information += "\n" + str(deatil)
                listforsingleinfn.append(information)
                listforsingleinfn.append(infns[len(infns) - 1])
                forReturningListHolder.append(listforsingleinfn)
                listforsingleinfn = []
                information = ""
                counter += 1
                endinIndex = int(startingIndex) + counter
            forReturningListHolder.append(str(endinIndex))
            return forReturningListHolder


class GuneCommunity:
    def MonthInlineRetriver(self, update: Update, bot):
        CustomeKbd = [
            [KeyboardButton("<- Back")]
        ]
        GuneCommunityFlagAndVariables.fromGuneCommunityToGuneMainPortalPage = True
        replkbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose The Month From List Down Blelow If There is Any",
                         reply_markup=replkbd)
        import DataBaseConnectivity
        data = DataBaseConnectivity.GuneCommunityHandler().monthRetriverForReviewIsHeld()
        if data is not None:
            temp = []
            main = []
            counter = 0
            for month in data:
                if counter == 1:
                    temp.append(InlineKeyboardButton(str(month), callback_data="36~" + str(month) + "~" + str(
                        update.effective_user.id)))
                    main.append(temp)
                    temp = []
                    counter = 0
                else:
                    temp.append(InlineKeyboardButton(str(month), callback_data="36~" + str(month) + "~" + str(
                        update.effective_user.id)))
                    counter += 1
            if counter == 1:
                main.append(temp)

            replyInline = InlineKeyboardMarkup(main)
            bot.send_message(update.effective_user.id,
                             text=" \U0001F447\U0001F447\U0001F447\U0001F447\U0001F447\U0001F447",
                             reply_markup=replyInline)
        else:
            bot.send_message(update.effective_user.id,
                             text="There is No Reivews Held So Far Come Back Some Another Time")


class GuneCommunityFlagAndVariables:
    fromGuneCommunityToGuneMainPortalPage = False


class GuneShare:
    def alreadyBorrowedBooksControlingPage(self, update: Update, bot):
        CustomeKbs = [
            [KeyboardButton("<- Back")]
        ]
        replkbd = ReplyKeyboardMarkup(CustomeKbs, resize_keyboard=True)
        bot.send_message(update.effective_user.id,
                         text="If There is Any Physical Book You Shared Will Be Fetched Here \U0001F447\U0001F447\U0001F447",
                         reply_markup=replkbd)
        GunePortalForGuneShareFlagsAndVariables.flagFromDocumetnsSharedPhysicallYpanelToDocumentManipulationPage = True
        import DataBaseConnectivity
        result = DataBaseConnectivity.GuneShareForSharingDocument().borrowedDocumentsRetriver(
            str(update.effective_user.id))
        if result is not None:
            for datas in result:
                BookInformation = datas[0]
                bookId = datas[1]
                requesterId = datas[2]

                replyInline = InlineKeyboardMarkup([[InlineKeyboardButton("Returned",
                                                                          callback_data="34~" + bookId + "~" + str(
                                                                              update.effective_user.id) + "~" + requesterId)]])
                bot.send_message(update.effective_user.id, text="-- Book Information --" + "\n" + BookInformation,
                                 reply_markup=replyInline)

        else:
            bot.send_message(update.effective_user.id, text="There is No Book You Physically Shared")

    def RequestsRecieveHanling(self, update: Update, bot):
        CustomeKbd = [
            [KeyboardButton("<- Back")]
        ]
        replyKbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        GunePortalForGuneShareFlagsAndVariables.flagFromGetRequestToSharedDocuementPage = True

        bot.send_message(update.effective_user.id,
                         text="All Request Will Be Listed Down Here If There is Any \U0001F447\U0001F447\U0001F447\U0001F447",
                         reply_markup=replyKbd)

        import DataBaseConnectivity
        result = DataBaseConnectivity.GuneShareForSharingDocument().RequestRetriver(str(update.effective_user.id))
        if result is not None:

            bookId = result[1]
            requesterId = result[2]
            CustomInline = [
                [InlineKeyboardButton("View Persons Ratings",
                                      callback_data="30~" + str(bookId) + "~" + str(
                                          update.effective_user.id) + "~" + requesterId)],
                [InlineKeyboardButton("Share Information",
                                      callback_data="31~" + str(bookId) + "~" + str(
                                          update.effective_user.id) + "~" + requesterId),
                 InlineKeyboardButton("Borrowed", callback_data="32~" + bookId + "~" + requesterId + "~" + str(
                     update.effective_user.id))],
                [InlineKeyboardButton("Not Currently Available",
                                      callback_data="33~" + str(bookId) + "~" + str(
                                          update.effective_user.id) + "~" + requesterId)]
            ]
            inlineReplykbd = InlineKeyboardMarkup(CustomInline)
            bot.send_message(update.effective_user.id, text=result[0], reply_markup=inlineReplykbd)

        else:
            bot.send_message(update.effective_user.id, text=" There is No Any New Requests Check Some Other Time")

    def RequestToGetPhysicalDocuments(self, update: Update, bot, dataToBeStored, RequestedTo):
        import DataBaseConnectivity
        resultOfCommietement = DataBaseConnectivity.GuneShareForSharingDocument().pysicalDocumentsRequestWriterForUser(
            dataToBeStored, RequestedTo)

        if resultOfCommietement:
            CustomKbd = [
                [InlineKeyboardButton("Requested", callback_data="29~" + "luvU" + "~" + "tsiye")]
            ]
            replyKbd = InlineKeyboardMarkup(CustomKbd)
            query = update.callback_query
            query.answer()
            query.edit_message_reply_markup(reply_markup=replyKbd)
        else:
            bot.send_message(update.effective_user.id, text="The Request Is Already Sent")

    def forRetrivingAllPhysicalDocuments(self, update: Update, bot):
        CustomK = [[KeyboardButton("<- Back")]]
        repl = ReplyKeyboardMarkup(CustomK, resize_keyboard=True)
        bot.send_message(update.effective_user.id,
                         text="All Books Are Going To lsited Down Here \U0001F447 \U0001F447 \U0001F447 \U0001F447",
                         reply_markup=repl)
        GunePortalForGuneShareFlagsAndVariables.flagFromPhysicallDocToGetDocumentPage = True
        import DataBaseConnectivity
        listOfInfns = DataBaseConnectivity.GuneShareForSharingDocument().RetrivingAllPublicPhysicallDocuments(
            str(update.effective_user.id))
        if listOfInfns is not None:
            if listOfInfns != []:
                for mainList in listOfInfns:
                    mainInformation = mainList[3]
                    text = self.textForRetriving(mainInformation)

                    CustomeInline = [
                        [InlineKeyboardButton("Request",
                                              callback_data="28~" + mainList[0] + "~" + mainList[1] + "~" + mainList[
                                                  2])]
                    ]
                    replyInlinKbd = InlineKeyboardMarkup(CustomeInline)
                    bot.send_message(update.effective_user.id, text=text, reply_markup=replyInlinKbd)
            else:
                bot.send_message(update.effective_user.id,
                                 text="There is No Physicall Book Published So far Come some Another Time")
        else:
            bot.send_message(update.effective_user.id,
                             text="There is No Physicall Book Published So far Come some Another Time")

    def ForRetrivingAllSoftCopiesDocuments(self, update: Update, bot):
        CustomK = [[KeyboardButton("<- Back")]]
        repl = ReplyKeyboardMarkup(CustomK, resize_keyboard=True)
        bot.send_message(update.effective_user.id,
                         text="All Books Are Going To lsited Down Here \U0001F447 \U0001F447 \U0001F447 \U0001F447",
                         reply_markup=repl)
        GunePortalForGuneShareFlagsAndVariables.flagFromSoftCopyShowingToGetDocumentsPage = True
        import DataBaseConnectivity
        allDatas = DataBaseConnectivity.GuneShareForSharingDocument().RetrivingAllPublicSoftCopies()
        if allDatas is not None:
            if allDatas != []:
                for Informations in allDatas:
                    textInfn = self.textForRetriving(Informations)
                    documentId = Informations["DocumentId"]
                    bot.send_document(update.effective_user.id, documentId)
                    bot.send_message(update.effective_user.id, text=textInfn)
            else:
                bot.send_message(update.effective_user.id, text="SoftCopies Can't Be Fetched For Some reason")
        else:
            bot.send_message(update.effective_user.id,
                             text="There  Is no SoftCopy Published So far check some other time")

    def listProviderForGetDocumentsInSharedDocumentPage(self, update: Update, bot):
        CustomeKbd = [
            [KeyboardButton("Physical Document"), KeyboardButton("Soft Copies")],
            [KeyboardButton("<- Back")]
        ]
        GunePortalForGuneShareFlagsAndVariables.flagFromGetDocumentsToSharedDocumentsPage = True
        replykbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose How You Want To Proceed", reply_markup=replykbd)

    def listProvideForSharedDocumentsPage(self, update: Update, bot):
        CustomeKbd = [
            [KeyboardButton("Get Requests"), KeyboardButton("Get Documents")],
            [KeyboardButton("<- Back")]
        ]
        GunePortalForGuneShareFlagsAndVariables.flagFromSharedDocumentsToGunesharePage = True
        replykbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose How You Want To Proceed ", reply_markup=replykbd)

    def textForRetriving(self, datas):
        AuthorsName = datas["AuthorsName"]
        BookName = datas["BookName"]
        CurrentPrice = datas["CurrentPrice"]
        Langauge = datas["Langauge"]
        NumberOfEdition = datas["NumberOfEdition"]
        StatusOfTheBook = datas["StatusOfTheBook"]
        TypeOfTheBook = datas["TypeOfTheBook"]

        text = "\U0001F464 Authors Name : " + AuthorsName + '\n' + \
               "\U0001F4D5 Book Name : " + BookName + '\n' + \
               "\U0001F4B0 CurrentPrice : " + CurrentPrice + '\n' + \
               "\U0001F449 Language :" + Langauge + '\n' + \
               "\U0001F522 Number Of Edition :" + NumberOfEdition + '\n' + \
               "\U0001F449 Status Of The Book :" + StatusOfTheBook + '\n' + \
               "\U00002139	Type Of Documents :" + TypeOfTheBook + '\n'

        return text

    def ViewAllTheDocuments(self, update: Update, bot):
        import DataBaseConnectivity
        lists = DataBaseConnectivity.GuneShareForSharingDocument().ViewDocumentsForHisBooksOnlyButAll(
            str(update.effective_user.id))
        if lists is not None:
            privateSoftCopies = lists[0]
            privatePhysicalDocuments = lists[1]
            publicSoftCopies = lists[3]
            publicPhysicalDocuments = lists[2]
            CustomeKeybd = [[KeyboardButton("<- Back")]]
            repl = ReplyKeyboardMarkup(CustomeKeybd, resize_keyboard=True)
            if privateSoftCopies != []:
                bot.send_message(update.effective_user.id,
                                 text="List Of Privately Registered SoftCopies \U0001F447 \U0001F447 \U0001F447 \U0001F447",
                                 reply_markup=repl)
                for datas in privateSoftCopies:
                    DocumentId = datas["DocumentId"]
                    infn = self.textForRetriving(datas)
                    bot.send_document(update.effective_user.id, DocumentId)
                    import DataBaseConnectivity
                    ids = DataBaseConnectivity.GuneShareForSharingDocument().BookTimestampId(datas,
                                                                                             str(update.effective_user.id),
                                                                                             "Private")
                    CustomeInline = [
                        [InlineKeyboardButton("Make It Public", callback_data="26~" + ids[0] + "~" + ids[1])]]
                    InlineKbd = InlineKeyboardMarkup(CustomeInline)
                    bot.send_message(update.effective_user.id, text=infn, reply_markup=InlineKbd)

            if privatePhysicalDocuments != []:
                bot.send_message(update.effective_user.id,
                                 text="List Of Privately Registered Physical Documents \U0001F447 \U0001F447 \U0001F447 \U0001F447",
                                 reply_markup=repl)
                for datas in privatePhysicalDocuments:
                    infn = self.textForRetriving(datas)
                    import DataBaseConnectivity
                    ids = DataBaseConnectivity.GuneShareForSharingDocument().BookTimestampId(datas,
                                                                                             str(update.effective_user.id),
                                                                                             "Private")
                    print(ids)
                    CustomeInline = [
                        [InlineKeyboardButton("Make It Public", callback_data="26~" + ids[0] + "~" + ids[1])]]
                    InlineKbd = InlineKeyboardMarkup(CustomeInline)
                    bot.send_message(update.effective_user.id, text=infn, reply_markup=InlineKbd)
            if publicSoftCopies != []:
                bot.send_message(update.effective_user.id,
                                 text="List Of Public Registered Soft Copies \U0001F447 \U0001F447 \U0001F447 \U0001F447",
                                 reply_markup=repl)
                for datas in publicSoftCopies:
                    DocumentId = datas["DocumentId"]
                    infn = self.textForRetriving(datas)
                    bot.send_document(update.effective_user.id, DocumentId)
                    import DataBaseConnectivity
                    ids = DataBaseConnectivity.GuneShareForSharingDocument().BookTimestampId(datas,
                                                                                             str(update.effective_user.id),
                                                                                             "Public")
                    CustomeInline = [
                        [InlineKeyboardButton("Make It Private", callback_data="27~" + ids[0] + "~" + ids[1])]]
                    InlineKbd = InlineKeyboardMarkup(CustomeInline)
                    bot.send_message(update.effective_user.id, text=infn, reply_markup=InlineKbd)
            if publicPhysicalDocuments != []:

                bot.send_message(update.effective_user.id,
                                 text="List Of Public Registered Physical Books \U0001F447 \U0001F447 \U0001F447 \U0001F447",
                                 reply_markup=repl)
                for datas in publicPhysicalDocuments:
                    infn = self.textForRetriving(datas)
                    import DataBaseConnectivity
                    ids = DataBaseConnectivity.GuneShareForSharingDocument().BookTimestampId(datas,
                                                                                             str(update.effective_user.id),
                                                                                             "Public")

                    CustomeInline = [
                        [InlineKeyboardButton("Make It Private", callback_data="27~" + ids[0] + "~" + ids[1])]]
                    InlineKbd = InlineKeyboardMarkup(CustomeInline)
                    bot.send_message(update.effective_user.id, text=infn, reply_markup=InlineKbd)
        else:
            bot.send_message(update.effective_user.id, text="There is No Document Registred So Far")

    def DeleteDocuemtInformation(self, update: Update, bot, month, TimeStampId, mainLookUp):
        import DataBaseConnectivity
        result = DataBaseConnectivity.GuneShareForSharingDocument().DocumentDeleting(str(update.effective_user.id),
                                                                                     mainLookUp, month, TimeStampId)
        if result:
            query = update.callback_query
            query.answer()
            query.edit_message_text("Document Deleted!", reply_markup=InlineKeyboardMarkup([[]]))
        else:
            query = update.callback_query
            query.answer()
            query.edit_message_text("Document Can't Be Deleted !", reply_markup=InlineKeyboardMarkup([[]]))

    def ilineInTwoRowMakerWithListInput(self, data, lookUp, typelookUp):
        MainList = []
        templist = []
        counter = 0
        for timestamp in data:
            if counter == 1:
                templist.append(
                    InlineKeyboardButton(timestamp, callback_data="24~" + timestamp + "~" + lookUp + "~" + typelookUp))
                MainList.append(templist)
                templist = []
                counter = 0
            else:
                templist.append(
                    InlineKeyboardButton(timestamp, callback_data="24-" + timestamp + "-" + lookUp + "-" + typelookUp))
                counter += 1
        if counter == 1:
            MainList.append(templist)

        replkbd = InlineKeyboardMarkup(MainList)
        return replkbd

    def InlineListProviderOfDocuments(self, update: Update, bot, flag):
        if flag == 1:
            telegramid = str(update.effective_user.id)
            CustomeKbd = [
                [KeyboardButton("Public"), KeyboardButton("Private")],
                [KeyboardButton("<- Back")]
            ]
            replKbd = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
            bot.send_message(update.effective_user.id, text="Choose How u Want To Proceed", reply_markup=replKbd)
            GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument = True
        elif flag == 2:
            CustomeKbd = [
                [KeyboardButton("Physically"), KeyboardButton("SoftCopy")],
                [KeyboardButton("<- Back")]
            ]
            repl = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)

            bot.send_message(update.effective_user.id, text="Choose How u Want To Proceed", reply_markup=repl)
            GunePortalForGuneShareFlagsAndVariables.flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument = True
        elif flag == 3:
            lookUp = GunePortalForGuneShareFlagsAndVariables.typeAccessbelityChoosen
            typeOfDocumentlookup = ""
            if GunePortalForGuneShareFlagsAndVariables.flagIfChoosenIsIsPhysicallAccessebility:
                typeOfDocumentlookup = "Physically"
            elif GunePortalForGuneShareFlagsAndVariables.flagForChoosenISSoftCopyAccessebility:
                typeOfDocumentlookup = "SoftCopy"
            replyMarkup = ReplyKeyboardMarkup([[KeyboardButton("<- Back")]], resize_keyboard=True)
            bot.send_message(update.effective_user.id, text="Choose A month in Which you  want to manipulate",
                             reply_markup=replyMarkup)
            import DataBaseConnectivity

            listOfMonth = DataBaseConnectivity.GuneShareForSharingDocument().DocumetMonthRetriver(
                str(update.effective_user.id), lookUp)
            if listOfMonth is not None:
                replymarkup = self.ilineInTwoRowMakerWithListInput(listOfMonth, lookUp, typeOfDocumentlookup)
                bot.send_message(update.effective_user.id, text="\U0001F447 \U0001F447	\U0001F447 \U0001F447",
                                 reply_markup=replymarkup)
            else:
                bot.send_message(update.effective_user.id, text="There is No Document Registred So Far")
        elif flag == 4:
            listofinfns = GunePortalForGuneShareFlagsAndVariables.infnsForDocument.split("-")
            month = listofinfns[0]
            mainlookUp = listofinfns[1]
            typelookUp = listofinfns[2]
            import DataBaseConnectivity
            valueRet = DataBaseConnectivity.GuneShareForSharingDocument().DocumentFullInformationRetriver(
                str(update.effective_user.id), mainlookUp, typelookUp, month)

            if valueRet is not None:
                for timestapID in valueRet:
                    Information = valueRet[timestapID]
                    AuthorsName = Information["AuthorsName"]
                    BookName = Information["BookName"]
                    CurrentPrice = Information["CurrentPrice"]
                    Langauge = Information["Langauge"]
                    NumberOfEdition = Information["NumberOfEdition"]
                    TypeOfTheBook = Information["TypeOfTheBook"]
                    textToBeRetrived = "Authors Name : " + AuthorsName + "\n" + \
                                       "Book Name : " + BookName + "\n" + \
                                       "Current Price : " + CurrentPrice + "\n" + \
                                       "Lanaguge : " + Langauge + "\n" + \
                                       "Number Of Edition : " + NumberOfEdition + "\n" + \
                                       "Type Of The Book : " + TypeOfTheBook + "\n"
                    if Information["StatusOfTheBook"] == "SoftCopy":
                        DocumentId = Information["DocumentId"]
                        bot.send_document(update.effective_user.id, DocumentId)

                    CustomeKbd = [
                        [InlineKeyboardButton("Delete",
                                              callback_data="25~" + timestapID + "~" + GunePortalForGuneShareFlagsAndVariables.infnsForDocument)]
                    ]
                    replInlineKbd = InlineKeyboardMarkup(CustomeKbd)
                    bot.send_message(update.effective_user.id, text=textToBeRetrived, reply_markup=replInlineKbd)
            else:
                bot.send_message(update.effective_user.id, text="There is No Document Associated With this Month")

    def listMenuProviderForSharedDocumentsMangingPAGE(self, update: Update, bot):
        GunePortalForGuneShareFlagsAndVariables.flagFromManagingDocuemtToGuneSharePage = True
        CustomKbd = [
            [KeyboardButton("Delete"), KeyboardButton("View")],
            [KeyboardButton("Books Shared Physically")],
            [KeyboardButton("<- Back")]
        ]
        replyKbs = ReplyKeyboardMarkup(CustomKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose How You Want To Proceed?", reply_markup=replyKbs)

    def DocumentInformationRetriver(self, update: Update, bot, flag):
        if flag == 1:
            CustomeKeyboard = [
                [KeyboardButton("<- Back")]
            ]
            replyKbd = ReplyKeyboardMarkup(CustomeKeyboard, resize_keyboard=True, one_time_keyboard=True)
            bot.send_message(update.effective_user.id, text="Enter The Name Of The Document ", reply_markup=replyKbd)
            GunePortalForGuneShareFlagsAndVariables.forReceivingDocumentName = True
            GunePortalForGuneShareFlagsAndVariables.flagFromDocumentInformationRetriverToShariningDocumentPage = True
        elif flag == 2:
            bot.send_message(update.effective_user.id, text="Enter The Author Name Of The Book?")
            GunePortalForGuneShareFlagsAndVariables.forReceivingAuthorOfTheDocument = True
        elif flag == 3:
            GunePortalForGuneShareFlagsAndVariables.forReceivingTypeOfTheBook = True
            CustomeList = [
                [KeyboardButton("Fiction"), KeyboardButton("Non-Fiction")],
                [KeyboardButton("<- Back")]
            ]

            replyKeyBoard = ReplyKeyboardMarkup(CustomeList, resize_keyboard=True)
            bot.send_message(update.effective_user.id, text="Specify Type OF Book", reply_markup=replyKeyBoard)
        elif flag == 4:
            CustomeKeyboard = [
                [KeyboardButton("<- Back")]
            ]
            replyKbd = ReplyKeyboardMarkup(CustomeKeyboard, resize_keyboard=True, one_time_keyboard=True)
            bot.send_message(update.effective_user.id, text="Choose By Pressing The Link", reply_markup=replyKbd)
            customeInlineKeybd = InlineKeyboardMarkup(GunePortalForGuneShareFlagsAndVariables.listForFictionalBooks)
            bot.send_message(update.effective_user.id, text="\U0001F447	\U0001F447 \U0001F447",
                             reply_markup=customeInlineKeybd)
        elif flag == 5:
            CustomeKeyboard = [
                [KeyboardButton("<- Back")]
            ]
            replyKbd = ReplyKeyboardMarkup(CustomeKeyboard, resize_keyboard=True, one_time_keyboard=True)
            bot.send_message(update.effective_user.id, text="Choose By Pressing The Link", reply_markup=replyKbd)
            customeInlineKeybd = InlineKeyboardMarkup(GunePortalForGuneShareFlagsAndVariables.listForNonFictionalBooks)
            bot.send_message(update.effective_user.id, text="\U0001F447	\U0001F447 \U0001F447",
                             reply_markup=customeInlineKeybd)
        elif flag == 6:
            bot.send_message(update.effective_user.id, text="Enter The Language The Book Is Written ?")
            GunePortalForGuneShareFlagsAndVariables.forReceivingLanguageOfTheBook = True
        elif flag == 7:
            bot.send_message(update.effective_user.id, text="Enter  Edition Number Of The Book ?")
            GunePortalForGuneShareFlagsAndVariables.forReceivingNumberOfEdition = True
        elif flag == 8:
            bot.send_message(update.effective_user.id, text="Enter Current Price On Market ?")
            GunePortalForGuneShareFlagsAndVariables.forReceivingCurrentPrice = True
        elif flag == 9:
            CustomeKbd = [
                [KeyboardButton("Physically"), KeyboardButton("SoftCopy")],
                [KeyboardButton("<- Back")]
            ]
            replyMarkup = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
            bot.send_message(update.effective_user.id, text="Choose How You Want To Share The Document ",
                             reply_markup=replyMarkup)

        elif flag == 10:
            CustomeKeyboard = [
                [KeyboardButton("<- Back")]
            ]
            replyKbd = ReplyKeyboardMarkup(CustomeKeyboard, resize_keyboard=True, one_time_keyboard=True)
            bot.send_message(update.effective_user.id, text="Attach The Document", reply_markup=replyKbd)
            GunePortalForGuneShareFlagsAndVariables.forReceivingActualFile = True
        elif flag == 11:
            GunePortalForGuneShareFlagsAndVariables.forReceivingActualFile = False
            CustomeKeyboard = [
                [KeyboardButton("Yes"), KeyboardButton("Discard")]
            ]
            GunePortalForGuneShareFlagsAndVariables.flagFromDocumentInformationRetriverToShariningDocumentPage = False
            replymarkupCode = ReplyKeyboardMarkup(CustomeKeyboard, resize_keyboard=True)

            textToBeRetetrived = " All Information U Entered \n\U0001F4D5BookName : " + GunePortalForGuneShareFlagsAndVariables.nameOftheDocument + "\n" + \
                                 "\U0001F4D5 AuthorsName : " + GunePortalForGuneShareFlagsAndVariables.nameOftheAuthorOfTheDocument + "\n" + \
                                 "\U0001F4D5 TypeOfTheBook :" + GunePortalForGuneShareFlagsAndVariables.typeOFTheBook + "\n" + \
                                 "\U0001F202 Langauge : " + GunePortalForGuneShareFlagsAndVariables.languageOfTheDocumentWritten + "\n" + \
                                 "\U0001F522 NumberOfEdition :" + GunePortalForGuneShareFlagsAndVariables.numberOfEdition + "\n" + \
                                 "\U0001F4B8 CurrentPrice : " + GunePortalForGuneShareFlagsAndVariables.currentPriceOnMarket + "\n" + \
                                 "\U0001F449 StatusOfTheBook : " + GunePortalForGuneShareFlagsAndVariables.statusOfTheDocument + "\n"

            bot.send_message(update.effective_user.id, text=textToBeRetetrived, reply_markup=replymarkupCode)
        elif flag == 12:
            dataToBeStored = None
            GunePortalForGuneShareFlagsAndVariables.forReceivingActualFile = False
            if GunePortalForGuneShareFlagsAndVariables.flagForSharingSoftCopy:
                dataToBeStored = {
                    "StatusOfTheBook": GunePortalForGuneShareFlagsAndVariables.statusOfTheDocument,
                    "BookName": GunePortalForGuneShareFlagsAndVariables.nameOftheDocument,
                    "AuthorsName": GunePortalForGuneShareFlagsAndVariables.nameOftheAuthorOfTheDocument,
                    "TypeOfTheBook": GunePortalForGuneShareFlagsAndVariables.typeOFTheBook,
                    "Langauge": GunePortalForGuneShareFlagsAndVariables.languageOfTheDocumentWritten,
                    "NumberOfEdition": GunePortalForGuneShareFlagsAndVariables.numberOfEdition,
                    "CurrentPrice": GunePortalForGuneShareFlagsAndVariables.currentPriceOnMarket,
                    "Document": GunePortalForGuneShareFlagsAndVariables.fileContent,
                    "DocumentId": GunePortalForGuneShareFlagsAndVariables.filecontentId
                }
            elif GunePortalForGuneShareFlagsAndVariables.flagForPhysicallySahring:
                dataToBeStored = {
                    "StatusOfTheBook": GunePortalForGuneShareFlagsAndVariables.statusOfTheDocument,
                    "BookName": GunePortalForGuneShareFlagsAndVariables.nameOftheDocument,
                    "AuthorsName": GunePortalForGuneShareFlagsAndVariables.nameOftheAuthorOfTheDocument,
                    "TypeOfTheBook": GunePortalForGuneShareFlagsAndVariables.typeOFTheBook,
                    "Langauge": GunePortalForGuneShareFlagsAndVariables.languageOfTheDocumentWritten,
                    "NumberOfEdition": GunePortalForGuneShareFlagsAndVariables.numberOfEdition,
                    "CurrentPrice": GunePortalForGuneShareFlagsAndVariables.currentPriceOnMarket,
                    "Document": "Undefined",
                    "DocumentId": "Undefined"
                }
            import DataBaseConnectivity
            if GunePortalForGuneShareFlagsAndVariables.flagForPrivateDocumentRegistering:
                GunePortalForGuneShareFlagsAndVariables.flagForPrivateDocumentRegistering = False
                returnedVal = DataBaseConnectivity.GuneShareForSharingDocument().DocumentRresgistering(dataToBeStored,
                                                                                                       str(update.effective_user.id),
                                                                                                       "Private")
                if returnedVal:
                    bot.send_message(update.effective_user.id, text="Successfully Document Set")
                else:
                    bot.send_message(update.effective_user.id, text="Document Can't Be Added")

            elif GunePortalForGuneShareFlagsAndVariables.flagForPublicDocumentRegistering:
                GunePortalForGuneShareFlagsAndVariables.flagForPublicDocumentRegistering = False
                returnedVal = DataBaseConnectivity.GuneShareForSharingDocument().DocumentRresgistering(dataToBeStored,
                                                                                                       str(update.effective_user.id),
                                                                                                       "Public")
                if returnedVal:
                    bot.send_message(update.effective_user.id, text="Successfully Document Set")
                else:
                    bot.send_message(update.effective_user.id, text="Document Can't Be Added")
            self.listProviderForShareDocumentPage(update, bot)

    def listProviderForShareDocumentPage(self, update: Update, bot):

        CustomKbd = [
            [KeyboardButton("Public"), KeyboardButton("Private")],
            [KeyboardButton("<- Back")]
        ]
        GunePortalForGuneShareFlagsAndVariables.flagFromShareDocumentLandingPageToGuneSharePage = True

        replyKeyBoard = ReplyKeyboardMarkup(CustomKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose How You Want To Share Your Books?",
                         reply_markup=replyKeyBoard)

    def GuneShareMainPageListProvider(self, update: Update, bot):
        CustomeKbd = [
            [KeyboardButton("Share Document"), KeyboardButton("Manage Document")],
            [KeyboardButton("Shared Documents")],
            [KeyboardButton("<- Back")]
        ]
        replyKeyBoard = ReplyKeyboardMarkup(CustomeKbd, resize_keyboard=True)
        bot.send_message(update.effective_user.id, text="Choose What You Want perform?", reply_markup=replyKeyBoard)
        GunePortalForGuneShareFlagsAndVariables.flagFromGuneMainPageToGunePortalMainPage = True


class GunePortalForGuneShareFlagsAndVariables:
    # constants for defingn the Gener Of The Book
    listForFictionalBooks = [
        [InlineKeyboardButton(text="Fanatasy", callback_data="22-selection-Fantasy"),
         InlineKeyboardButton(text="Science Fiction", callback_data="22-selection-Science_Fiction")],
        [InlineKeyboardButton(text="Historical Fiction", callback_data="22-selection-Historical_Fiction"),
         InlineKeyboardButton(text="Realistic Fiction", callback_data="22-selection-Realistic_Fiction")],
        [InlineKeyboardButton(text="Mystrey", callback_data="22-selection-Mystrey"),
         InlineKeyboardButton(text="Fan Fiction", callback_data="22-selection-Fan_Fiction")],
        [InlineKeyboardButton(text="Suspense", callback_data="22-selection-Suspense_OR_Thriller"),
         InlineKeyboardButton(text="Crime", callback_data="22-selection-Crime")],
        [InlineKeyboardButton(text="Horror", callback_data="22-selection-Horror"),
         InlineKeyboardButton(text="Humor", callback_data="22-selection-Humor")],
        [InlineKeyboardButton(text="Classic", callback_data="22-selection-Classic"),
         InlineKeyboardButton(text="Satire", callback_data="22-selection-Satire")],
        [InlineKeyboardButton(text="Comic/Graphic", callback_data="22-selection-Comic/Graphic"),
         InlineKeyboardButton(text="Magical Realism", callback_data="22-selection-Magical_Realism")],
        [InlineKeyboardButton(text="Romance", callback_data="22-selection-Romance"),
         InlineKeyboardButton(text="Drama", callback_data="22-selection-Drama")],
        [InlineKeyboardButton(text="Anthology", callback_data="22-selection-Anthology"),
         InlineKeyboardButton(text="Fable", callback_data="22-selection-Fable")],
        [InlineKeyboardButton(text="Fairy Tale", callback_data="22-selection-Fairy_Tale"),
         InlineKeyboardButton(text="Short Story", callback_data="22-selection-Short_Story")],
        [InlineKeyboardButton(text="Mythology", callback_data="22-selection-Mythology"),
         InlineKeyboardButton(text="Legened", callback_data="22-selection-Legend")],
        [InlineKeyboardButton(text="Other", callback_data="22-selection-Other")]
    ]

    listForNonFictionalBooks = [
        [InlineKeyboardButton(text="Narrative Non-Fiction", callback_data="23-selection-Narrative_Non_Fiction"),
         InlineKeyboardButton(text="Essay", callback_data="23-selection-Essay")],
        [InlineKeyboardButton(text="Speech", callback_data="23-selection-Speech"),
         InlineKeyboardButton(text="Self Help Books", callback_data="23-selection-Self_Help_Books")],
        [InlineKeyboardButton(text="Periodicals", callback_data="23-selection-periodicals"),
         InlineKeyboardButton(text="Biography", callback_data="23-selection-Biography")],
        [InlineKeyboardButton(text="Reference Book", callback_data="23-selection-Reference_Book"),
         InlineKeyboardButton(text="Text Book", callback_data="23-selection-Text_Book")],
        [InlineKeyboardButton(text="Memoir", callback_data="23-selection-Memoir"),
         InlineKeyboardButton(text="Research Papers", callback_data="23-selection-Research_Papers")],
        [InlineKeyboardButton(text="Other", callback_data="23-selection-Other")]
    ]
    # -------------------------- end ----------------
    #     flags For backward travresal
    flagFromGuneMainPageToGunePortalMainPage = False
    flagFromShareDocumentLandingPageToGuneSharePage = False
    flagFromDocumentInformationRetriverToShariningDocumentPage = False
    # ---------------- end  -------------------------

    # variable for holding document information while uploading gune share document

    nameOftheDocument = ""
    nameOftheAuthorOfTheDocument = ""
    typeOFTheBook = ""
    languageOfTheDocumentWritten = ""
    numberOfEdition = ""
    currentPriceOnMarket = ""
    fileContent = ""
    filecontentId = ""
    statusOfTheDocument = ""

    # flagForReciving These Above Information
    forReceivingDocumentName = False
    forReceivingAuthorOfTheDocument = False
    forReceivingTypeOfTheBook = False
    forReceivingLanguageOfTheBook = False
    forReceivingNumberOfEdition = False
    forReceivingCurrentPrice = False
    forReceivingActualFile = False
    flagForRecivingStatusOfTheBook = False
    flagForPrivateDocumentRegistering = False
    flagForPublicDocumentRegistering = False
    flagForPhysicallySahring = False
    flagForSharingSoftCopy = False
    # -------------------- end ---------------------------------------------------
    # for manging documents u uploaded so far

    flagFromManagingDocuemtToGuneSharePage = False
    flagForIndicatingIFitsInManagingAndCHOOSINGtypeOfDocument = False
    flagIfChoosenIsIsPhysicallAccessebility = False
    flagForChoosenISSoftCopyAccessebility = False
    flagForIndicatingIFDeletingTheBookNotRegistering = False
    flagFromSharedDocumentsToGunesharePage = False
    flagFromGetDocumentsToSharedDocumentsPage = False
    flagFromSoftCopyShowingToGetDocumentsPage = False
    flagFromPhysicallDocToGetDocumentPage = False
    flagFromGetRequestToSharedDocuementPage = False
    flagFromDocumetnsSharedPhysicallYpanelToDocumentManipulationPage = False

    typeAccessbelityChoosen = ""
    infnsForDocument = ""
    monthHolder = ""
    timeStampIdHolder = ""
    # ------------------------ end --------------------------------------------


class GunePortalFlagAndVaraibles:
    flagForGunePortalmainMenu = False
    flagForGunePortalRegitseringView = False
    flagForGunePortalAdminControlPanel = False
    flagForGunePortalAdminLandingPage = False
    flagFromMonthlyReviewToAdminLandlingPage = False

    flagForAttachingReviewDocument = False
    flagForSeminarTittle = False
    flagForGuneReviewBookTittle = False
    flagForDateReviewHold = False
    flagForDocumentPublsisher = False
    flagForNumberOfPages = False
    flagForDiscriptionOnThreReview = False
    flagForReviewPresenter = False
    flagFortraversingFromuploaingfinshedtorecviewManipualtionPage = False
    flagForUpdaterIndicaterToDistiguishFromAdder = False
    flagFromPeoplesSuggestionToAdminLandingPage = False
    flagFromVoteCotrollingMaintoAdminMainPage = False
    flagFromOpennVotePageToVoteControlingPage = False
    flagFromResultOfVotePageToVoteControlingPage = False
    flagFromSendAlertToAdmingLandingPage = False

    flagForWritingANoticeForCommunityAsBroadcastMessage = False
    flagForNormalUserReviewViewingPageToNormalUsrPanel = False
    flagForEnteringCommentOnMothllyReview = False

    flagFromSuggestionAddertoNormalUserPage = False

    flagForEnteringSuggestionBookName = False
    flagForEnteringNameOfTheAuthor = False
    flagForEnteringActualSuggestionDocumnet = False
    flagForEnteringDocumentID = False
    flagForEnteringDiscriptionOnSuggestion = False
    flagForEnteringUserNameOfSuggestor = False
    flagForFromNormalViewAdminViewToNormalViewUsers = False
    flagFromVotingPageToNormalUserView = False
    nameofSuggestedNameOfTheBook = ""
    nameofauthourofthebook = ""
    discriptionofsuggestion = ""
    actualDocument = ""
    documentId = ""


class GunePortalMain:
    def AccountCecker(self, id):
        listOfuser = DataBaseConnectivity.PersonalAccountHandler().AccountChecker()
        if listOfuser is not None:
            listOFuserAccounts = listOfuser.values()
            flag = False
            for i in listOFuserAccounts:
                if i == id:
                    flag = True

            return flag

        else:
            return False

    def listProviderIfNotCommunityMember(self):
        CustomeKeyboard = [
            [KeyboardButton("Register")], [KeyboardButton("<- Back")]  # here u can make that if
        ]
        replKbd = ReplyKeyboardMarkup(CustomeKeyboard, resize_keyboard=True)
        return replKbd

    def listProviderIfAlreadyCommunityMember(self):
        CustomeKeyboard = [
            [KeyboardButton(text="Gune Official Reviews"), KeyboardButton(text="Gune Share")],
            [KeyboardButton(text="Gune Community Reviews")],
            [KeyboardButton(text="<- Back")]
        ]
        relKdbd = ReplyKeyboardMarkup(CustomeKeyboard, resize_keyboard=True)
        return relKdbd

    def userRegistering(self, tgid):
        DataBaseConnectivity.PersonalAccountHandler.RegisterUserAsGuneCommunity(tgid)
