# MindfulMinute
## Inspiration
There is currently, on average, an 11 year delay between the first diagnosis and effective treatment of mental illnesses. This can be attributed to the lack of accessibility in mental health resources, as well as unclear delineations between different illnesses causing misdiagnosis. As seniors in high school, we wanted to focus on two of the most commonly experienced mental illnesses by people our age: unipolar depression and bipolar. These also happen to be two of the most commonly misdiagnosed mental illnesses. As patients are more likely to seek help when they are in a depressive state, those with bipolar disease are likely to be diagnosed as having depression. Their hypomanic, or “high” states, are then looked at as signs of remission of depression. This can be extremely dangerous as incorrect diagnoses lead to improper treatment. Treating bipolar patients with antidepressants can result in manic episodes and rapid cycling between episodes. Creating accessible, yet effective tools to identify misdiagnoses in their early stages is crucial.

## What it does
Here at Mindful Minute we have created a platform through which patients who were recently diagnosed with depression can be monitored for bipolar tendencies.

First we read scientific literature on the differences between depression and bipolar diseases. After identifying that the experience of hypomanic states was an indicator of bipolar vulnerability, we curated our own short questionnaire that identifies whether someone has recently experienced a hypomanic episode. Patients who have recently been diagnosed with depression are to fill out this questionnaire twice a week to track whether or not they have had any hypomanic episodes. They are emailed the results of their questionnaire, and if they are identified to have had a hypomanic episode, they will be provided with directions on where to find the right resources to help them.

While official diagnoses can only be made by psychiatric professionals, we will indicate to users their vulnerability levels for bipolar, and recommend whether or not they should be tested for it. Our resources will also aid our users through periods of mania, and help cultivate healthy coping habits that they can continue to use into the future.

## How we built it
Our questionnaire was made through google forms, and its results were linked to our Python code. In Python, we created lists of bipolar and depression symptomatology. Sentiment analysis was conducted on the google form responses, and matched to either bipolar or depression. Based on whichever list had more matches, we elucidate whether or not a user has high vulnerability to bipolar.

We then used Python to also send an email back to the user with our recommended resources based on their vulnerability levels.

## Challenges we ran into
Connecting multi-word symptoms from the form to our original list of symptoms. We separated each of the form responses into single words while conducting our sentiment analysis so having to piece together multi-word symptoms was a challenge.

Building comprehensive lists of symptoms for bipolar and depression that allow for clear distinctions between the two disorders with the use of reliable resources. Since depression and bipolar are inherently very similar in terms of symptoms experienced we needed to make sure to emphasize symptoms that are unique to each illness as well as the hypomanic symptoms seen in bipolar patients.

## Website and Devpost
Our code was uploaded onto the mindful minute website which can be accessed here: https://mindfulminuteaia.wixsite.com/mindful-minute.
Our solution secured us 1st place in the mental health track in the UniHacks 2023 hackathon. The devpost can be accessed here: https://devpost.com/software/mindful-minute-vbrhtq.
