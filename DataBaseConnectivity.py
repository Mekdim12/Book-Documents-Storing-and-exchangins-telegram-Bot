


import firebase_admin.messaging
from firebase_admin import credentials
from firebase_admin import db


credential = credentials.Certificate({
  "type": "service_account",
  "project_id": "mytrialbookstore",
  "private_key_id": "6700b7c25c0d2fc3f57a06508b0fab00a4e595ed",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC3CMj+gJz5p5zC\n9McknLMUINShvZGNOm737hsgWdGoN2ys54SyJ5kyXjH/ZvmXdVj20AglipbkIufV\nNt+bnOo7NNA32JAaUMAdWwm3qx7867H06jHV+QETR/N9a6juj06MkEC0NMBbwsMl\nqnTQpI7klUgkg7yXPzRohRKEmxVwHwcu4Gt991INJ+yie4g1xcI0LXikzX2Z+sEr\nyAPiWIsE+to9fper0vkXVsOmHMjJhCGeD4naENZVGa1nE2/OtH2+w8wSz5DmtOkW\nAuni5a5mmFV1QtB0HmVFTDAtLvjxeh5bev/VaKHYV4OFMy2vEMJsqvkM+49rooUn\nULyD9on3AgMBAAECggEABx8L4ZRecdDa0V5VsIUk6zJlziSCg7n+HvOq0YTnxSw2\n3w6jmTeKMdf8CQGtfKjqUlwAsnk5wAbi+ebd0f+hFgxK0klrkzfeFFD6R/pGmoo5\nt8Y0NIIwz6+7zP7sfoT2hj3cjpuuJO58dObfZE4VaIEDDWH6FfELGHVI+v4lBOIs\np2SueL2yhCEaS+aLTJxO9AvSmOrDFftl4G57OF2lNpfhNqX+GZbEGybjX9ECRv10\nUptKzq2SmJZ1bLSe6+GX7/ZytnaYKc1wh3p37TDgvJLZARgCoemP3gFsV0LLQkpI\noQCfzhh2If8gE2WjC3fR0V4Apnu0CvlIHAoiA7hLfQKBgQDZiHUVQMpG+NAGC+9Z\nEsygx9MlpaNsoaYlYtgF74DzOv6DUk9v31gBRk0M9xMEb0ulpkEmplKBwHZo868y\nJQIYI39tileDEZ/NQXnVTtMquMSbR8TzEe6S8GXxqoKGPvQKjlPIqH2P/XJgWuTc\nE1LgDXwnHyI6OInO26ZBG5QrfQKBgQDXZplVQm4PISptdOnNd3KoI7QQ9eQ9Gq9q\nqCehkEwubhhFD8aMbG3QHfo3Uvv4MRWH5IBaViiomSZ0LIFpIqRxZdD1xqKX+YAI\nlCFCy8efy6dcJLjX0bXTaZpB/TrttfdrPJZK5gKOjfJu1Ib/7GizYhiDVca9XLq7\nA/lBk329gwKBgFEwSOKhx90tSBa5pZ9NEOqBKiFG7PPCcUxK0+2DMlGVlyBUPCm4\n5hOztVY9cO+aylUM9AwEz4510rvhF2ZTwbBYr1qm43qbvVTSNzKRtOahB2AdLTi7\nXJui9al4xjZskJDQBh1CJXr0URf9VKV+4NOWtNu1FwU7zNNTz31FWcvRAoGBAKla\non3VUAEXO2t5u4VvP7eQ8rdPDRc5zueVtCsj77Gln/FUmO+5JJG3sA4lcbROqzX/\n4yajjS4Z05ENmOXXdeEugx9qAFZqtU6JYKlK3PX3QeuBd88/s6y336+4cMeLBS/M\nIAJdW29HjW+0Kzw2XI+FNe601x/1M19snWIAm6EPAoGAdyVeD8iEyX3iSy/kRaxa\nvUHVdn3/LF1kEHJuirloa/RZPZ6ePTtNfWvRZ1dbVJ+p6QAAdMXnD/7dIU8Ys8U1\nO5gxYLplHWKGd7DYujQRqzPeI2R7i+jP8f72CbFFdRPG8SomeTsF4rGXcEFJU45Z\nedxwi6VWrAgpsmXS4dJOHNo=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-8z2yb@mytrialbookstore.iam.gserviceaccount.com",
  "client_id": "106229556961246454613",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8z2yb%40mytrialbookstore.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(credential, {"databaseURL": "https://mytrialbookstore-default-rtdb.firebaseio.com/"})


def writeToUserPersonalInformation(useTgId, FullName, userName, PhoneNumber, locationOfUser):
    ref = db.reference("UsersInformation").child("UserPersonalInformation").child(useTgId)
    DataToBeStored = {
        "Full_Name": FullName,
        "User_Name": userName,
        "Phone_Number": PhoneNumber,
        "Current_Location": locationOfUser
    }

    try:
        ref.set(DataToBeStored)
        return True
    except:
        return False


def writeToBooksInformation(userTelegramId, bookid, catagory, BookName, langaugeOfTheBook, publicationYear, status,
                            editionNumber, currentPriceOnMarket, actualBookInfn):
    ref = db.reference("UsersInformation").child("BookInformation").child(userTelegramId)
    var = ref.get()

    indexCounter = 100
    try:
        listOfIDs = list(var.keys())
        indexCounter = int(listOfIDs[len(listOfIDs) - 1])
        indexCounter = indexCounter + 1

    except:
        indexCounter = 100
    ref = ref.child(str(indexCounter))

    dataToBeStored = {
        "NameOFtheBook": BookName,
        "Catagory": catagory,
        "LanguageOFTheBook": langaugeOfTheBook,
        "PublicationYear": publicationYear,
        "StatusOfTheBook": status,
        "NumberEditionNumber": editionNumber,
        "CurrentPrice": currentPriceOnMarket,
        "BookId": bookid,
        "Book": actualBookInfn
    }
    # ref.set(dataToBeStored)
    try:
        ref.set(dataToBeStored)
        return True
    except :
       return  False


def writeToBooksInformation2(childId, userTelegramId, bookid, catagory, BookName, langaugeOfTheBook, publicationYear,
                             status, editionNumber, currentPriceOnMarket, actualBookInfn):
    ref = db.reference("UsersInformation").child("BookInformation").child(userTelegramId)

    ref = ref.child(str(childId))

    dataToBeStored = {
        "NameOFtheBook": BookName,
        "Catagory": catagory,
        "LanguageOFTheBook": langaugeOfTheBook,
        "PublicationYear": publicationYear,
        "StatusOfTheBook": status,
        "NumberEditionNumber": editionNumber,
        "CurrentPrice": currentPriceOnMarket,
        "BookId": bookid,
        "Book": actualBookInfn
    }
    try:
        ref.set(dataToBeStored)

        return True
    except Exception:
        return False


def PersonalInformaionRetrivater(userTgid):
    ref = db.reference("UsersInformation/UserPersonalInformation/").child(userTgid)
    return ref.get()


def UserAccountsListProvider():
    ref = db.reference("UsersInformation/UserPersonalInformation/")
    return ref.get()



def BookListProvideForSingleUserTelegIdspecifically(tguserid, bookNumber):
    ref = db.reference("UsersInformation/BookInformation/").child(tguserid).child(bookNumber)
    return ref.get()


def BookListProvideForSingleUserTelegId(tguserid):
    ref = db.reference("UsersInformation/BookInformation/").child(tguserid)
    if ref.get() is not None:
        return ref.get()
    else:
        return  None


def SpecificBookDeleter(userid, bookid):
    refObj = db.reference("UsersInformation").child("BookInformation").child(str(userid)).child(str(bookid))
    try:
        refObj.delete()
        return "Deleted"
    except:
        return "not good deleleting"


def BookListProviderALLtheBookAvaiable():
    ref = db.reference("UsersInformation/BookInformation/")
    return ref.get()


class GuneCommunityHandler:
    def sepecifiedIdSeminarDataRetriver(self, month, seminarId):
        ref = db.reference("GuneCommunity").child("SeminarReviews").child(str(month)).child(str(seminarId))
        if ref.get() is not None:
            Information = ref.get()
            CurrentDate = Information["CurrentDate"]
            DateAndTimeTheReviewHeld = Information["DateAndTimeTheReviewHeld"]
            DocumentId = Information["DocumentId"]
            NameOfSeminar = Information["NameOfSeminar"]
            NameOfTheDocument = Information["NameOfTheDocument"]
            NumberOfpages = Information["NumberOfpages"]
            ReviewDetailDiscription = Information["ReviewDetailDiscription"]
            RviewedPresenter = Information["RviewedPresenter"]
            publisherName = Information["publisherName"]

            text = "---- Review Information --" + '\n' + \
                   "\U0001F9FE	 Name Of Seminar :" + NameOfSeminar + '\n' + \
                   "\U0001F4D5 Name Of The Book :" + NameOfTheDocument + '\n' + \
                   "\U0001F464Authors Name :" + publisherName + '\n' + \
                   "\U0001F4DF	Number Of Page :" + NumberOfpages + '\n' + \
                   "\U0001F449 On DayReview Held :" + DateAndTimeTheReviewHeld + '\n' + \
                   "\U0001F481  Review Presneted By :  Mr/Ms" + RviewedPresenter + '\n' + \
                   "\U0001F449 Review Idease Raised By Attendant :" + ReviewDetailDiscription
            return text
        else:
            return  None
    def personalInformationUserNameRetriver(self, telegramId):
        ref = db.reference("UsersInformation/UserPersonalInformation/").child(telegramId)
        if ref.get() is not None:
            userName = ref.get()["User_Name"]
            return userName
        else:
            return None

    def commentsRetriverForSpecifiedSeminarInSpecifiedMonth(self, month, seminarId):
        ref = db.reference("GuneCommunity").child("MonthlyReviewComments").child(str(month))
        if ref.get() is not None:
            data = ref.get()
            templist = []
            mainlistForReturn = []
            for timestampId in data:
                Informations = data[timestampId]
                commenterId = Informations["CommenterAccount"]
                seminarReviewId = Informations["IdOfReview"]
                comment = Informations["comment"]
                if seminarReviewId == seminarId :
                    templist.append(commenterId)
                    templist.append(comment)
                    mainlistForReturn.append(templist)
                    templist = []
            return mainlistForReturn
        else:
            return None

    def seminarReviewHeldOntheMonthRetriver(self, month):
        ref = db.reference("GuneCommunity").child("SeminarReviews").child(str(month))
        if ref.get() is not None:
            tempList = []
            mainListForeturn = []
            for timestamp in ref.get():
                Information = ref.get()[timestamp]
                CurrentDate = Information["CurrentDate"]
                DateAndTimeTheReviewHeld = Information["DateAndTimeTheReviewHeld"]
                DocumentId = Information["DocumentId"]
                NameOfSeminar = Information["NameOfSeminar"]
                NameOfTheDocument = Information["NameOfTheDocument"]
                NumberOfpages = Information["NumberOfpages"]
                ReviewDetailDiscription = Information["ReviewDetailDiscription"]
                RviewedPresenter = Information["RviewedPresenter"]
                publisherName = Information["publisherName"]

                text = "---- Review Information --"+ '\n' +\
                        "Name Of Seminar :"+NameOfSeminar +'\n' +\
                        "Name Of The Book :"+NameOfTheDocument +'\n' +\
                        "Authors Name :"+publisherName +'\n' +\
                        "Number Information :"+NumberOfpages+'\n' +\
                        "On DayReview Held :"+DateAndTimeTheReviewHeld + '\n' +\
                        "Review Presneted By :  Mr/Ms"+RviewedPresenter+'\n' +\
                        "Review Idease Raised By Attendant :" +ReviewDetailDiscription

                tempList.append(text)
                tempList.append(timestamp)
                tempList.append(DocumentId)
                mainListForeturn.append(tempList)
                tempList = []
            return mainListForeturn

        else:
            return  None
    def monthRetriverForReviewIsHeld(self):
        ref = db.reference("GuneCommunity").child("SeminarReviews")
        if ref.get() is not None:
            return ref.get()
        else:
            return None




class GuneShareForSharingDocument:
    def BorrowedDocumentInformationDeleterWhenBookIsRetrived(self, telegramId, timeStampId):
        ref = db.reference("GuneCommunity").child("PhysicalSharedDocumentsInformation").child("Borrowed").child(
            str(telegramId)).child(str(timeStampId))
        try:
            ref.delete()
            return True
        except:
            return False

    def borrowedDocumentsRetriver(self, telegramId):
        ref = db.reference("GuneCommunity").child("PhysicalSharedDocumentsInformation").child("Borrowed").child(
            str(telegramId))
        listt = []
        mainList = []
        if ref.get() is not None:
            for timestampid in ref.get():
                Information = ref.get()[timestampid]
                bookId = Information["BookID"]
                otheruserId = Information["RequestedBy"]
                BooInformation = self.BookInformationRetriver(telegramId, bookId)

                listt.append(BooInformation)
                listt.append(timestampid)
                listt.append(otheruserId)

                mainList.append(listt)
                listt = []
            return mainList
        else:
            return None

    def writterIfTheBookWasPhysicallYshared(self, telegramId, dataToBeStored):
        ref = db.reference("GuneCommunity").child("PhysicalSharedDocumentsInformation").child("Borrowed").child(
            str(telegramId))
        ref2 = db.reference("GuneCommunity").child("PhysicalSharedDocumentsInformation").child("Requests").child(
            str(telegramId))
        if ref2.get() is not None:
            try:
                for timestampId in ref2.get():
                    Information = ref2.get()[timestampId]

                    if Information == dataToBeStored:
                        ref2 = ref2.child(str(timestampId))
                        ref2.delete()
                        ref.push(dataToBeStored)
                        return True
            except:
                return False
        else:
            return False

    def voteRegistrer(self, dataToBestsored, rateReciverId, raterId):
        ref = db.reference("GuneCommunity").child("RatingInformation").child(str(rateReciverId)).child(str(raterId))
        try:
            data = ref.get()
            for timestampId in data:
                Information = data[timestampId]
                if dataToBestsored["BookId"] == Information["BookId"]:
                    return False
                ref.push(dataToBestsored)
                return True
        except:
            return False

    def VoteRetriverForRequester(self, requesterTelegId):
        ref = db.reference("GuneCommunity").child("RatingInformation").child(str(requesterTelegId))
        if ref.get() is not None:
            FullInforamtion = ""
            for rateGiver in ref.get():
                for timestampId in ref.get()[rateGiver]:
                    Information = ref.get()[rateGiver][timestampId]
                    rating = Information["Rate"]
                    symbol = ""
                    if rating == 1:
                        symbol = "\U0001F92C"
                    elif rating == 2:
                        symbol = "\U00002639"
                    elif rating == 3:
                        symbol = "\U0001F642"
                    elif rating == 4:
                        symbol = "\U0001F601"
                    BookInformation = self.BookInformationRetriver(str(rateGiver), Information["BookId"])
                    FullInforamtion += BookInformation + "\n" + \
                                       "Rating :" + symbol + "\n" + \
                                       "------------------------------\n"

            return FullInforamtion
        else:
            return None

    def PersonalInformationRetriver(self, telegramID):
        ref = db.reference("UsersInformation/UserPersonalInformation/").child(telegramID)
        if ref.get() is not None:
            information = ref.get()

            text = "\U0001F5FA Curretn Location :" + information["Current_Location"] + "\n" + \
                   "\U0001F464 Full Name :" + information["Full_Name"] + "\n" + \
                   "\U0001F4F1 Phone Number :" + information["Phone_Number"] + "\n" + \
                   "\U0001F481 User Name :" + "@" + information["User_Name"]
            return text
        else:
            return None

    def BookInformationRetriver(self, telegramId, bookId):
        ref = db.reference("GuneCommunity").child("Documents").child("Public").child(str(telegramId))
        if ref.get() is not None:
            for month in ref.get():
                for timestamp in ref.get()[month]:
                    if timestamp == bookId:
                        information = ref.get()[month][timestamp]

                        text = "\U0001F4D5 Book Name :" + information["BookName"] + "\n" + \
                               "\U0001F481 Authors Name :" + information["AuthorsName"] + "\n"

                        return text

        else:
            return None

    def RequestRetriver(self, telegramID):
        ref = db.reference("GuneCommunity").child("PhysicalSharedDocumentsInformation").child("Requests").child(
            str(telegramID))
        if ref.get() is not None:
            aLLRequests = ref.get()
            for ids in aLLRequests:
                bookId = aLLRequests[ids]["BookID"]
                RequestedBy = aLLRequests[ids]["RequestedBy"]

                resultOfBookInformatio = self.BookInformationRetriver(telegramID, bookId)
                resultPersonalInformationRetriver = self.PersonalInformationRetriver(RequestedBy)
                if resultPersonalInformationRetriver is not None and resultOfBookInformatio is not None:
                    text = " ------ Personal Information ----------" + "\n" + \
                           resultPersonalInformationRetriver + "\n" + \
                           "-----------  Requested Book Informarion -------------" + "\n" + \
                           resultOfBookInformatio
                    listForReturn = [text, bookId, RequestedBy]
                    return listForReturn
                else:
                    return None


        else:
            return None

    def pysicalDocumentsRequestWriterForUser(self, dataToBeStored, telegramId):
        ref = db.reference("GuneCommunity").child("PhysicalSharedDocumentsInformation").child("Requests").child(
            str(telegramId))
        try:
            if ref.get() is not None:
                data = ref.get()
                for timestampid in data:
                    Information = data[timestampid]
                    if Information == dataToBeStored:
                        return False

            ref.push(dataToBeStored)
            return True
        except:
            return False

    def RetrivingAllPublicPhysicallDocuments(self, tgID):
        listOfDocuments = []
        ref = db.reference("GuneCommunity").child("Documents").child("Public")
        if ref.get() is not None:
            data = ref.get()
            templist = []
            for telegramIds in data:
                for months in data[telegramIds]:
                    for timstampids in data[telegramIds][months]:
                        Information = data[telegramIds][months][timstampids]
                        if Information["StatusOfTheBook"] == 'Physically' and tgID != telegramIds:
                            templist.append(months)
                            templist.append(timstampids)
                            templist.append(telegramIds)
                            templist.append(Information)
                            listOfDocuments.append(templist)
                            templist = []
            return listOfDocuments
        else:
            return None

    def RetrivingAllPublicSoftCopies(self):
        listOfDocuments = []
        ref = db.reference("GuneCommunity").child("Documents").child("Public")
        if ref.get() is not None:
            data = ref.get()
            for telegramIds in data:
                for months in data[telegramIds]:
                    for information in (data[telegramIds])[months].values():
                        if information["StatusOfTheBook"] == "SoftCopy":
                            listOfDocuments.append(information)

            return listOfDocuments
        else:
            return None

    def PrivateToPublicViceVersaConverter(self, timestampId, telegramId, month, flag):
        if flag == 1:
            ref = db.reference("GuneCommunity").child("Documents").child("Private").child(telegramId).child(
                month).child(timestampId)
            ref2 = db.reference("GuneCommunity").child("Documents").child("Public").child(telegramId).child(month)
            if ref.get() is not None:
                data = ref.get()
                try:
                    ref2.push(data)
                    ref.delete()
                    return True
                except:
                    return False
            else:
                return False

        elif flag == 2:
            ref = db.reference("GuneCommunity").child("Documents").child("Public").child(telegramId).child(month).child(
                timestampId)
            ref2 = db.reference("GuneCommunity").child("Documents").child("Private").child(telegramId).child(month)
            if ref.get() is not None:
                data = ref.get()
                try:
                    ref2.push(data)
                    ref.delete()
                    return True
                except:
                    return False
            else:
                return False

    def BookTimestampId(self, dataToBeCompared, telegramID, lookUp):
        ref = db.reference("GuneCommunity").child("Documents").child(lookUp).child(str(telegramID))
        forret = []

        if ref.get() is not None:
            data = ref.get()
            for infn in data.values():
                month = list(data.keys())[0]
                for id in infn:
                    if dataToBeCompared == infn[id]:
                        forret.append(id)
                        forret.append(month)
                        break
            return forret
        else:
            return []

    def ViewDocumentsForHisBooksOnlyButAll(self, telegramId):

        ref = db.reference("GuneCommunity").child("Documents").child("Private").child(telegramId)
        ref2 = db.reference("GuneCommunity").child("Documents").child("Public").child(telegramId)

        PrivateSofCopies = []
        PrivatePhyiscalCopies = []

        PublicSoftCopies = []
        PublicPhysicalCopies = []
        if ref.get() is not None:
            WholeDocument = ref.get()
            for month in WholeDocument:
                for timestampID in WholeDocument[month]:
                    Information = ((WholeDocument[month]))[timestampID]
                    if Information["StatusOfTheBook"] == "SoftCopy":
                        PrivateSofCopies.append(Information)
                    elif Information["StatusOfTheBook"] == "Physically":
                        PrivatePhyiscalCopies.append(Information)

        if ref2.get() is not None:
            DocumentOfPublic = ref2.get()
            for month in DocumentOfPublic:
                for timestampId in DocumentOfPublic[month]:
                    WholeInformation = ((DocumentOfPublic[month]))[timestampId]
                    if WholeInformation["StatusOfTheBook"] == "SoftCopy":
                        PublicSoftCopies.append(WholeInformation)
                    elif WholeInformation["StatusOfTheBook"] == "Physically":
                        PublicPhysicalCopies.append(WholeInformation)

        listForReturning = [PrivateSofCopies, PrivatePhyiscalCopies, PublicPhysicalCopies, PublicSoftCopies]
        return listForReturning

    def ViewDocuments(self):

        ref = db.reference("GuneCommunity").child("Documents").child("Private")
        ref2 = db.reference("GuneCommunity").child("Documents").child("Public")
        PrivateSofCopies = []
        PrivatePhyiscalCopies = []

        PublicSoftCopies = []
        PublicPhysicalCopies = []

        if ref.get() is not None:
            WholeDocument = ref.get()
            for telegramId in WholeDocument:
                for month in WholeDocument[telegramId]:
                    for timestampID in WholeDocument[telegramId][month]:
                        Information = ((WholeDocument[telegramId])[month])[timestampID]
                        if Information["StatusOfTheBook"] == "SoftCopy":
                            PrivateSofCopies.append(Information)
                        elif Information["StatusOfTheBook"] == "Physically":
                            PrivatePhyiscalCopies.append(Information)
        if ref2.get() is not None:
            DocumentOfPublic = ref2.get()
            for telegramId in DocumentOfPublic:
                for month in DocumentOfPublic[telegramId]:
                    for timestampId in DocumentOfPublic[telegramId][month]:
                        WholeInformation = ((DocumentOfPublic[telegramId])[month])[timestampId]
                        if WholeInformation["StatusOfTheBook"] == "SoftCopy":
                            PublicSoftCopies.append(WholeInformation)
                        elif WholeInformation["StatusOfTheBook"] == "Physically":
                            PublicPhysicalCopies.append(WholeInformation)

        else:
            return None
        listForReturning = [PrivateSofCopies, PrivatePhyiscalCopies, PublicPhysicalCopies, PublicSoftCopies]
        return listForReturning

    def DocumentDeleting(self, telegraId, lookUp, month, timestampId):
        ref = db.reference("GuneCommunity").child("Documents").child(lookUp).child(str(telegraId)).child(
            str(month)).child(timestampId)
        if ref.get() is not None:
            try:
                ref.delete()
                return True
            except:
                return False
        else:
            return False

    def DocumentFullInformationRetriver(self, telegramID, lookup, typelookUp, Month):
        ref = db.reference("GuneCommunity").child("Documents").child(lookup).child(telegramID).child(Month)
        if ref.get() is not None:
            return ref.get()
        else:
            return None

    def DocumetMonthRetriver(self, telegramID, lookUp):
        ref = db.reference("GuneCommunity").child("Documents").child(lookUp).child(telegramID)
        print(ref.get())
        try:
            if ref.get() is not None:
                return list(ref.get().keys())
            else:
                return None
        except:
            return None

    def DocumentRresgistering(self, dataToBeStored, telegramId, lookup):
        import datetime
        ref = db.reference("GuneCommunity").child("Documents").child(lookup).child(telegramId).child(
            str(datetime.datetime.now().month))
        try:
            ref.push(dataToBeStored)
            return True
        except:
            return  False


# GuneShareForSharingDocument().borrowedDocumentsRetriver("270241315")


class PersonalAccountHandler:
    def UserNameRetriver(self, telegramid):
        ref = db.reference("UsersInformation").child("UserPersonalInformation").child(str(telegramid))
        if ref is not None:
            return (ref.get())["User_Name"]
        else:
            return None

    def AccountChecker(self):
        ref = db.reference("GuneCommunity").child("UsersAccount").child("Accounts")
        return ref.get()

    def RegisterUserAsGuneCommunity(idd):

        ref = db.reference("GuneCommunity").child("UsersAccount").child("Accounts")
        accounts = PersonalAccountHandler().AccountChecker()

        counter = 10

        if accounts is not None:
            keyList = list(accounts.keys())
            lastItem = keyList[len(keyList) - 1]
            counter = int(lastItem) + 1
        else:
            counter = 10
        ref = ref.child(str(counter))
        ref.set(idd)


    def AccoutListProvider(self):
        ref = db.reference("GuneCommunity").child("UsersAccount").child("Accounts")
        return ref.get()


#
# PersonalAccountHandler.RegisterUserAsGuneCommunity("2702413u55515")


import datetime


class SeminarReviews:
    def MonthlyReviewCommentAdder(self, month, timestampid, comment, userID):
        ref = db.reference("GuneCommunity").child("MonthlyReviewComments").child(str(month))
        datatoStored = {"IdOfReview": timestampid, "comment": comment, "CommenterAccount": str(userID)}
        try:
            ref.push(datatoStored)
            return True
        except:
            return False

    def uploadthismonthReview(self, dataToBeStored):
        ref = db.reference("GuneCommunity").child("SeminarReviews").child(str(datetime.datetime.now().month))
        if ref.get() is not None:
            datasAlreadyStored = ref.get().values()
            alreadyStored = False
            for i in datasAlreadyStored:
                if dataToBeStored["NameOfTheDocument"] == i["NameOfTheDocument"]:
                    alreadyStored = True
                    break
            if not alreadyStored:
                try:
                    ref.push(dataToBeStored)
                    return True
                except:
                    return False
            else:
                return False
        else:
            try:
                ref.push(dataToBeStored)
                return True
            except:
                return False

    def UpdateMonthlyReview(self, dataTobeStored, identificationTimeStamp):
        import datetime
        ref = db.reference("GuneCommunity").child("SeminarReviews").child(str(datetime.datetime.now().month))
        ref = ref.child(identificationTimeStamp)

        try:
            ref.update(dataTobeStored)
            return True
        except:
            return False

    def DeleteMonthlyReview(self, timestampid):
        import datetime
        ref = db.reference("GuneCommunity").child("SeminarReviews").child(str(datetime.datetime.now().month)).child(
            timestampid)
        try:
            ref.delete()
            return True
        except:
            return False

    def montlyReviewRetriver(self):
        import datetime
        ref = db.reference("GuneCommunity").child("SeminarReviews").child(str(datetime.datetime.now().month))
        return ref.get()


class VoteHandler:
    def VoteRemoverIfThereIs(self, lookUp, telegramId, timesatpid):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes").child(str(timesatpid)).child(
            lookUp)
        if ref.get() is not None:
            valuesCheck = list(ref.get().values())
            checker = telegramId in valuesCheck
            if checker:
                for key in ref.get():
                    val = (ref.get())[key]
                    if val == telegramId:
                        ch = len(list(ref.get().values()))
                        if ch > 1:
                            ref = ref.child(key)
                            ref.delete()
                        else:
                            ref.set({"100": "0"})
                            ref = ref.child(key)
                            ref.delete()
                        break
            else:
                pass

    def voteResultRetriver(self, timesatpid, flag):
        if flag == 1:
            # for returning thumb up result
            ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes").child(str(timesatpid)).child(
                "UpVote")
            if ref.get() is not None:
                if list(ref.get().values())[0] == '0':
                    return "0"
                else:
                    return str(len(list(ref.get().values())))
            else:
                return "0"

        elif flag == 2:
            # for returning thumb down result
            ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes").child(str(timesatpid)).child(
                "DownVote")
            if ref.get() is not None:
                if list(ref.get().values())[0] == '0':
                    return "0"
                else:
                    return str(len(list(ref.get().values())))
            else:
                return "0"

    def VoteForHandlingDownVotes(self, timestampidOFsuggestion, telegramid):

        ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes")
        ref = ref.child(str(timestampidOFsuggestion))
        try:
            ref = ref.child("DownVote")
            if list(ref.get().values())[0] == '0':
                values = telegramid in list(ref.get().values())
                ref.delete()
                self.VoteRemoverIfThereIs("UpVote", telegramid, timestampidOFsuggestion)
                if not values:
                    ref.push(telegramid)
                    return str(len(list(ref.get().values())))
                else:
                    return False

            else:
                values = telegramid in list(ref.get().values())
                self.VoteRemoverIfThereIs("UpVote", telegramid, timestampidOFsuggestion)
                if not values:
                    ref.push(telegramid)
                    return str(len(list(ref.get().values())))
                else:
                    return False



        except:
            return None

    def voteforHandlingUpVotes(self, timestampidOFsuggestion, telegramid):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes")

        ref = ref.child(str(timestampidOFsuggestion))

        try:
            ref = ref.child("UpVote")
            if list(ref.get().values())[0] == '0':

                values = telegramid in list(ref.get().values())
                ref.delete()
                self.VoteRemoverIfThereIs("DownVote", telegramid, timestampidOFsuggestion)
                if not values:
                    ref.push(telegramid)
                    return str(len(list(ref.get().values())))
                else:
                    return False

            else:
                values = telegramid in list(ref.get().values())
                self.VoteRemoverIfThereIs("DownVote", telegramid, timestampidOFsuggestion)
                if not values:
                    ref.push(telegramid)
                    return str(len(list(ref.get().values())))
                else:
                    return False


        except:
            return None

    def ClosingVote(self, timestampid):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes").child(str(timestampid))
        try:
            ref.delete()
            return True
        except:
            return False

    def VoteResultRetriver(self):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes")
        if ref.get() is not None:
            return ref.get()
        else:
            return None

    def OpenVotePoll(self, timestamp, month):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveVotes")
        ref2 = db.reference("GuneCommunity").child("Suggestions").child("ApprovedSuggestions").child(str(month)).child(
            timestamp)
        if ref2.get() is not None:
            try:
                ref.push(ref2.get())
                ref2.delete()
                return True
            except:
                return False
        else:
            return False

    def listProviderForOPeningVotes(self, month):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ApprovedSuggestions").child(str(month))
        mainlist = []
        onesuggestionlist = []
        data = ref.get()
        if data is not None:
            for id in data:
                for i in data[id].values():
                    onesuggestionlist.append(i)

                onesuggestionlist.append(id)
                mainlist.append(onesuggestionlist)
                onesuggestionlist = []

            return mainlist
        else:
            return None


class CommuntitySuggestionHandler:

    def suggestionadder(self, datatobsstored):
        import datetime
        ref = db.reference("GuneCommunity").child("Suggestions").child("PeoplesSuggestions").child(
            str(datetime.datetime.now().month))

        if ref.get() is not None:
            data = ref.get().values()
            flag = False
            for dat in data:
                if dat["NameOfTheBook"] == datatobsstored["NameOfTheBook"] and dat["NameOfTheAuthor"] == datatobsstored[
                    "NameOfTheAuthor"]:
                    flag = True
                    break

            if flag:
                return False
            else:
                try:
                    ref.push(datatobsstored)
                    return True
                except:
                    return False
        else:
            try:
                ref.push(datatobsstored)
            except:
                return False

    def listofApprovedSuggestionProvider(self):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ApprovedSuggestions")
        if ref.get() is not None:
            return list(ref.get().keys())
        else:
            return None

    def listOfSuggestionMonthProvider(self):
        ref = db.reference("GuneCommunity").child("Suggestions").child("PeoplesSuggestions")
        if ref.get() is not None:
            return list(ref.get().keys())
        else:
            return None

    def listOfSuggestionOfSpecifiedMonth(self, month):
        ref = db.reference("GuneCommunity").child("Suggestions").child("PeoplesSuggestions").child(str(month))
        mainlist = []
        onesuggestionlist = []
        data = ref.get()
        if data is not None:
            for id in data:
                for i in data[id].values():
                    onesuggestionlist.append(i)
                onesuggestionlist.append(id)
                mainlist.append(onesuggestionlist)
                onesuggestionlist = []

        return mainlist

    def forRegisteringApprovedSuggestions(self, timestampidForAsSuggestinId, month):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ApprovedSuggestions").child(str(month))
        try:
            ref2 = db.reference("GuneCommunity").child("Suggestions").child("PeoplesSuggestions").child(
                str(month)).child(timestampidForAsSuggestinId)

            # ref = ref.child(timestampidForAsSuggestinId)
            ref.push(ref2.get())
            return True
        except:
            return False

    def forDeletinggSuggestionForDiscardingFunction(self, timstampid, month):
        ref = db.reference("GuneCommunity").child("Suggestions").child("PeoplesSuggestions").child(str(month)).child(
            timstampid)
        try:
            ref.delete()
            return True
        except:
            return False

    def ActiveSuggestionIfVoteisOpenedByThem(self):
        ref = db.reference("GuneCommunity").child("Suggestions").child("ActiveSuggestions")


# print(CommuntitySuggestionHandler().suggestionadder({
#     "NameOfTheBook": "this is the time",
#     "NameOfTheAuthor": "name id the name i beed talking ",
#     "ActualDocument": "f",
#     "DocumnetId": "DocumnetId",
#     "UpVote": 0,
#     "DownVote": 0,
#     "Discription": "This is The Discription",
#     "usenameofsuggester": "hassuxp"
#
# }))

# VoteHandler().VoteRemoverIfThereIs("UpVote","991848518","-MbzCUCPUBmor6KVteUL")
class RegisterNewUserAsAdmin:

    def PrivillageChecker(self, telegramId):
        ref = db.reference("GuneCommunity").child("UsersAccount").child("Adminstrators")
        if ref.get() is not None:
            listOFusers = (ref.get()).values()
            flag = False
            for i in listOFusers:
                if i == telegramId:
                    flag = True
                    break
            return flag
        else:
            return False

    def RegisterNewUserAsAdmin(userTelegramId):
        ref = db.reference("GuneCommunity").child("UsersAccount").child("Adminstrators")

        counter = 100

        if ref.get() is not None:
            listOFusers = list((ref.get()).keys())
            lastitem = listOFusers[len(listOFusers) - 1]
            counter = int(lastitem) + 1
        else:
            counter = 100
        ref = ref.child(str(counter))
        try:
            ref.set(userTelegramId)
            return True
        except:
            return False

    def DeleteAdminPrivillage(self, userTelegramId):
        ref = db.reference("GuneCommunity").child("UsersAccount").child("Adminstrators")  # .child(str(userTelegramId))
        idblock = ""
        for i in ref.get():
            if (ref.get())[i] == userTelegramId:
                idblock = i
                break
        ref = ref.child(str(idblock))

        try:
            ref.delete()
            return True
        except:
            return False

    def ViewAdminAccountList(self):
        ref = db.reference("GuneCommunity").child("UsersAccount").child("Adminstrators")
        return ref.get()


"""
   for writing to the database
"""

# ref = db.reference("UsersInformation/")
#
# UserInfnEnitityRedfrences = ref.child("UserPersonalInformation").child("024041650")
# UserdataToBeStored = {
#     "FullName": "Mekdim Tamirat",
#     "UserName": "@name",
#     "CurrentLocation": "AddisAbaba",
#     "BooKInformatationID": 1
# }
# BookInfnEntityReference = ref.child("BookInformation").child("1")
#
# BookInformationToStored = {
#     "BookName": "nameOftheBook",
#     "languageOftheBook": "Amharic",
#     "status": "AvaialabelI",
#     "EditionNumber": "6th",
#     "userName": "@name"
# }
# UserInfnEnitityRedfrences.set(UserdataToBeStored)
# BookInfnEntityReference.set(BookInformationToStored)

"""
    for updating the value inside the db using there key name and it sholuld be with exact same key
"""
# ref = db.reference("UsersInformation/").child("UserPersonalInformation")
#
# ref.update({
#     "userName" : "@mekdim"
# })


"""
    For Reading data from db   if u need deatil infn of child u should check the refrences u providing
    NoneType
"""

# ref = db.reference("UsersInformation/BookInformation/")
# var = ref.get()
#
# counter = 1
# for i in var:
#     if counter == len(var):
#         print(i)
#
#     counter += 1

"""
    for deleting infn u need to be careful ion the references since it should be child node
"""
# refObj= db.reference("UsersInformation/").child("BookInformation").child("1")
# refObj.delete()


# writeToBooksInformation(userTelegramId=str(270241315) ,catagory="mekdim tamirata loves tsion getenet" ,BookName="python for begginers", langaugeOfTheBook="English" ,publicationYear="12/4/8" ,status="avaiable" ,editionNumber=5
#                        ,currentPriceOnMarket=50,actualBookInfn="text",bookid="ddd")
# writeToUserPersonalInformation(useTgId="455", FullName="Mekdim tamirat", userName="@fuckedup", locationOfUser="Ethiopia", PhoneNumber="0924041650")
