import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import wordnet
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiment = SentimentIntensityAnalyzer()
import pandas as pd
import smtplib
from email.message import EmailMessage

#convert the sheets to dataframe
def convert_gsheets_url(u):
    try:
        worksheet_id = u.split('#gid=')[1]
    except:
        # Couldn't get worksheet id. Ignore it
        worksheet_id = None
    u = re.findall('https://docs.google.com/spreadsheets/d/.*?/',u)[0]
    u += 'export'
    u += '?format=csv'
    if worksheet_id:
        u += '&gid={}'.format(worksheet_id)
    return u

responses_sheet = 'https://docs.google.com/spreadsheets/d/1gnFd_M0PdtMoD7pGQxBwjtQPkanHKL_hsX0OrMgB0Ms/edit?usp=sharing'
try:
    url = convert_gsheets_url(responses_sheet)
    responses = pd.read_csv(url)
    print('Read successfully')
except:
    print(f"Could not read any data from the URL you provided.")

responses

responses_full_list = []
for i in range(0,len(responses)):
    indv_response = responses.loc[i].values.tolist()
    merged_indv_response = ' '.join(indv_response[4 : 13])
    responses_full_list.append(merged_indv_response)

responses_full_list

depression_symptoms = ["skinnier","lazy","tired","disinterested","worthless","suicidal","fatter","bigger","satiated","full","emptiness","angry","anxiety", "slow","outbursts","frustration","sadness","teary","hopeless","troubled","pain","headaches","guilt","blame","slow","craving","restlessness","misunderstood","negative","introvert","aching","lethargic","reserved"]
bipolar_symptoms = ["sleeplessness","gambling","reckless","moody","irritated","sad","hopeless","happy","talkative","distracted","energetic","confident","fatigue","energetic","impulsive","shopping","expensive","excited","racing","obsessive","narcissist","sleepy","inactive","elated","egotistic","high","smug","ego","spontaneous","passionate","sensual"]

def generatepred(indv_response):
    stop_words = set(stopwords.words('english'))
    my_tokenizer = RegexpTokenizer(r'\w+')
    tokens = my_tokenizer.tokenize(indv_response)
    filtered_sentence = [w for w in tokens if not w.lower() in stop_words]


    sentiment_list = []
    for i in filtered_sentence:
        pol = [sentiment.polarity_scores(i), i]
        sentiment_list.append(pol)

    filt_sentiment_list = []
    filt_bysentiment_sentence = []
    for i in sentiment_list:
        if i[0]['compound'] != 0.0:
            filt_sentiment_list.append(i[0])
            filt_bysentiment_sentence.append(i[1])

    sum_sentiment = 0
    for i in filt_sentiment_list:
        sum_sentiment += i['compound']
    avg_sentiment = (sum_sentiment)/(len(filt_sentiment_list))


    depression_exactmatch_count = 0
    bipolar_exactmatch_count = 0

    for i in depression_symptoms:
        for j in filt_bysentiment_sentence:
            if i == j:
                depression_exactmatch_count += 1

    for i in bipolar_symptoms:
        for j in filt_bysentiment_sentence:
            if i == j:
                bipolar_exactmatch_count += 1

    synonyms_full = []
    for j in filt_bysentiment_sentence:
        for syn in wordnet.synsets(j):
            for l in syn.lemmas():
                synonyms_full.append(l.name())

    def unique(list1):
        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    filtsentence_synonyms = unique(synonyms_full)

    depression_synmatch_count = 0
    bipolar_synmatch_count = 0

    for i in depression_symptoms:
        for j in filtsentence_synonyms:
            if i == j and j not in filt_bysentiment_sentence:
                depression_synmatch_count += 1

    for i in bipolar_symptoms:
        for j in filtsentence_synonyms:
            if i == j and j not in filt_bysentiment_sentence:
                bipolar_synmatch_count += 1

    depression_exactsyn_sum = depression_exactmatch_count + depression_synmatch_count
    bipolar_exactsyn_sum = bipolar_exactmatch_count + bipolar_synmatch_count

    if depression_exactsyn_sum > bipolar_exactsyn_sum and avg_sentiment <= 0:
        return "The results of our questionnaire indicate that you have a low vulnerability to bipolar disorder at this time. General mental health resources are provided on our website. Please refer to the 'depression resources' and 'mental health resources' tabs for information catered to your specific demographic."

    if bipolar_exactsyn_sum > depression_exactsyn_sum and avg_sentiment > 0:
        return "The results of our questionnaire indicate that you have a high vulnerability to bipolar disorder at this time. General mental health resources are provided on our website. Please refer to the 'bipolar disorder resources' and 'mental health resources' tabs for information catered to your specific demographic."

    if depression_exactsyn_sum > bipolar_exactsyn_sum and avg_sentiment > 0:
        return "The results of our questionnaire indicate that you have a moderate vulnerability to bipolar disorder at this time. General mental health resources are provided on our website. Please refer to the 'bipolar disorder resources' and 'mental health resources' tabs for information catered to your specific demographic."

    if bipolar_exactsyn_sum > depression_exactsyn_sum and avg_sentiment <= 0:
        return "The results of our questionnaire indicate that you have a moderate vulnerability to bipolar disorder at this time. General mental health resources are provided on our website. Please refer to the 'bipolar disorder resources' and 'mental health resources' tabs for information catered to your specific demographic."

    if bipolar_exactsyn_sum == depression_exactsyn_sum:
        if avg_sentiment > 0:
            return "The results of our questionnaire indicate that you have a moderate vulnerability to bipolar disorder at this time. General mental health resources are provided on our website. Please refer to the 'bipolar disorder resources' and 'mental health resources' tabs for information catered to your specific demographic."
        if avg_sentiment <= 0:
            return "The results of our questionnaire indicate that you have a low vulnerability to bipolar disorder at this time. General mental health resources are provided on our website. Please refer to the 'depression resources' and 'mental health resources' tabs for information catered to your specific demographic."
index = -1
emails_results = []
for res in responses_full_list:
    index += 1
    indv_result = []
    email = str(responses.iloc[index,3])
    indv_result.append(email)
    indv_result.append(generatepred(res))
    emails_results.append(indv_result)
print(emails_results)
