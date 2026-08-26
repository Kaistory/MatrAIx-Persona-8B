# Annual Checkup Habits Survey

Use exact `questionId` and valid choice ids.

## q0

Prompt: Do you currently have a primary care provider you see for checkups?

- Construct: `currently_have_primary_care_provider`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Yes, and I see them regularly |
| `b` | Yes, but I rarely see them |
| `c` | No, but I have had one in the past |
| `d` | No, I have never had one |

## q1

Prompt: When did you last have an annual physical or general wellness checkup?

- Construct: `when_did_last_have_annual`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Within the past 6 months |
| `b` | 6 to 12 months ago |
| `c` | 1 to 2 years ago |
| `d` | 3 to 5 years ago |
| `e` | More than 5 years ago |
| `f` | I have never had one |

## q2

Prompt: How often do you typically get a general checkup?

- Construct: `often_typically_get_general_checkup`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Every year |
| `b` | Every 2 to 3 years |
| `c` | Only when I have a specific concern |
| `d` | Rarely or never |

## q3

Prompt: Roughly how many years has it been since you started getting regular checkups? Please enter a number.

- Construct: `roughly_many_years_has_it`
- Type: `free_text`
- Required: `true`

Respond in a short free-text answer.

## q4

Prompt: How do you usually schedule your annual checkup?

- Construct: `usually_schedule_annual_checkup`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | By calling the office |
| `b` | Through an online patient portal |
| `c` | Through a scheduling app |
| `d` | The office schedules it for me automatically |
| `e` | I do not schedule them in advance |

## q5

Prompt: How far in advance do you usually book your annual checkup?

- Construct: `far_advance_usually_book_annual`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Same week |
| `b` | 1 to 2 weeks ahead |
| `c` | About a month ahead |
| `d` | Several months ahead |
| `e` | I do not plan ahead |

## q6

Prompt: Which of the following do you typically do to prepare for a checkup? (Select all that apply)

- Construct: `following_typically_prepare_checkup_sele`
- Type: `multi_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Write down questions or concerns |
| `b` | Make a list of my medications |
| `c` | Track symptoms beforehand |
| `d` | Fast if bloodwork is expected |
| `e` | Gather records from other providers |
| `f` | Bring a family member |
| `g` | I do not do anything special to prepare |

## q7

Prompt: Which of the following usually happen during your annual checkup? (Select all that apply)

- Construct: `following_usually_happen_during_annual`
- Type: `multi_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Blood pressure and vitals check |
| `b` | Review of my medications |
| `c` | Bloodwork or lab tests |
| `d` | Discussion of diet and exercise |
| `e` | Mental well-being check-in |
| `f` | Vaccinations or boosters |
| `g` | Referrals to specialists or screenings |
| `h` | None of these |

## q8

Prompt: About how long does your typical checkup appointment last? Please enter a number of minutes.

- Construct: `long_does_typical_checkup_appointment`
- Type: `free_text`
- Required: `true`

Respond in a short free-text answer.

## q9

Prompt: How much do you agree or disagree: An annual checkup is worth doing even when I feel healthy.

- Construct: `much_agree_disagree_annual_checkup`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Strongly disagree |
| `b` | Disagree |
| `c` | Neither agree nor disagree |
| `d` | Agree |
| `e` | Strongly agree |

## q10

Prompt: How much do you agree or disagree: My checkups usually feel rushed.

- Construct: `much_agree_disagree_my_checkups`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Strongly disagree |
| `b` | Disagree |
| `c` | Neither agree nor disagree |
| `d` | Agree |
| `e` | Strongly agree |

## q11

Prompt: How much do you agree or disagree: I leave my checkups with a clear understanding of my health.

- Construct: `much_agree_disagree_i_leave`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Strongly disagree |
| `b` | Disagree |
| `c` | Neither agree nor disagree |
| `d` | Agree |
| `e` | Strongly agree |

## q12

Prompt: How much do you agree or disagree: My provider takes time to answer all of my questions.

- Construct: `much_agree_disagree_my_provider`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Strongly disagree |
| `b` | Disagree |
| `c` | Neither agree nor disagree |
| `d` | Agree |
| `e` | Strongly agree |

## q13

Prompt: How much do you agree or disagree: I look forward to my annual checkup.

- Construct: `much_agree_disagree_i_look`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Strongly disagree |
| `b` | Disagree |
| `c` | Neither agree nor disagree |
| `d` | Agree |
| `e` | Strongly agree |

## q14

Prompt: How much do you agree or disagree: Scheduling a checkup is easy for me.

- Construct: `much_agree_disagree_scheduling_checkup`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Strongly disagree |
| `b` | Disagree |
| `c` | Neither agree nor disagree |
| `d` | Agree |
| `e` | Strongly agree |

## q15

Prompt: How important to you is each of the following in a checkup: having the same provider each time?

- Construct: `important_each_following_checkup_having`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Not at all important |
| `b` | Slightly important |
| `c` | Moderately important |
| `d` | Very important |
| `e` | Extremely important |

## q16

Prompt: How important to you is each of the following in a checkup: short wait time in the office?

- Construct: `important_each_following_checkup_short`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Not at all important |
| `b` | Slightly important |
| `c` | Moderately important |
| `d` | Very important |
| `e` | Extremely important |

## q17

Prompt: How important to you is each of the following in a checkup: enough time to talk with the provider?

- Construct: `important_each_following_checkup_enough`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Not at all important |
| `b` | Slightly important |
| `c` | Moderately important |
| `d` | Very important |
| `e` | Extremely important |

## q18

Prompt: How important to you is each of the following in a checkup: getting test results explained clearly?

- Construct: `important_each_following_checkup_getting`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Not at all important |
| `b` | Slightly important |
| `c` | Moderately important |
| `d` | Very important |
| `e` | Extremely important |

## q19

Prompt: How important to you is each of the following in a checkup: convenient appointment times?

- Construct: `important_each_following_checkup_conveni`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Not at all important |
| `b` | Slightly important |
| `c` | Moderately important |
| `d` | Very important |
| `e` | Extremely important |

## q20

Prompt: What is the main reason you keep up with (or would keep up with) annual checkups?

- Construct: `main_reason_keep_up_would`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | To catch problems early |
| `b` | To maintain a relationship with a provider |
| `c` | Peace of mind |
| `d` | A requirement for insurance or work |
| `e` | A family member encourages me |
| `f` | I do not keep up with them |

## q21

Prompt: Which of the following have caused you to skip or delay a checkup? (Select all that apply)

- Construct: `following_have_caused_skip_delay`
- Type: `multi_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Being too busy |
| `b` | Cost or coverage concerns |
| `c` | Feeling healthy and not seeing the need |
| `d` | Difficulty getting an appointment |
| `e` | Not having a regular provider |
| `f` | Dislike of doctor visits |
| `g` | I have not skipped or delayed a checkup |

## q22

Prompt: After a checkup, how often do you follow through on the recommendations you receive?

- Construct: `after_checkup_often_follow_through`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Always |
| `b` | Often |
| `c` | Sometimes |
| `d` | Rarely |
| `e` | Never |

## q23

Prompt: How do you usually receive your test or lab results after a checkup?

- Construct: `usually_receive_test_lab_results`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Through an online patient portal |
| `b` | A phone call from the office |
| `c` | A follow-up appointment |
| `d` | A letter or email |
| `e` | I usually do not receive results |

## q24

Prompt: How much do you agree or disagree: I trust the advice my provider gives me during checkups.

- Construct: `much_agree_disagree_i_trust`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Strongly disagree |
| `b` | Disagree |
| `c` | Neither agree nor disagree |
| `d` | Agree |
| `e` | Strongly agree |

## q25

Prompt: How confident are you in describing your health history and concerns during a checkup?

- Construct: `confident_describing_health_history_conc`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Not at all confident |
| `b` | A little confident |
| `c` | Somewhat confident |
| `d` | Very confident |
| `e` | Completely confident |

## q26

Prompt: Do you ever bring notes or a written list of questions to your checkup?

- Construct: `ever_bring_notes_written_list`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Always |
| `b` | Usually |
| `c` | Sometimes |
| `d` | Never |

## q27

Prompt: How often do you have a specific follow-up scheduled at the end of a checkup?

- Construct: `often_have_specific_follow_up`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Always |
| `b` | Often |
| `c` | Sometimes |
| `d` | Rarely |
| `e` | Never |

## q28

Prompt: Overall, how satisfied are you with your most recent checkup experience?

- Construct: `overall_satisfied_most_recent_checkup`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Very dissatisfied |
| `b` | Dissatisfied |
| `c` | Neutral |
| `d` | Satisfied |
| `e` | Very satisfied |

## q29

Prompt: How would you rate the overall quality of care at your checkups?

- Construct: `would_rate_overall_quality_care`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Excellent |
| `b` | Very good |
| `c` | Good |
| `d` | Fair |
| `e` | Poor |

## q30

Prompt: On a scale of 0 to 10, how likely are you to recommend your checkup provider to a friend or family member? (0 = not at all likely, 10 = extremely likely)

- Construct: `scale_0_10_likely_recommend`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | 0 |
| `b` | 1 |
| `c` | 2 |
| `d` | 3 |
| `e` | 4 |
| `f` | 5 |
| `g` | 6 |
| `h` | 7 |
| `i` | 8 |
| `j` | 9 |
| `k` | 10 |

## q31

Prompt: How likely are you to schedule your next checkup within the recommended time frame?

- Construct: `likely_schedule_next_checkup_within`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Very unlikely |
| `b` | Unlikely |
| `c` | Neither likely nor unlikely |
| `d` | Likely |
| `e` | Very likely |

## q32

Prompt: Which improvements would most help you keep up with annual checkups? Select your top 3. (Select all that apply)

- Construct: `improvements_would_most_help_keep`
- Type: `multi_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Automatic reminders when I am due |
| `b` | Easier online scheduling |
| `c` | Evening or weekend appointments |
| `d` | Shorter office wait times |
| `e` | Lower out-of-pocket cost |
| `f` | More time with the provider |
| `g` | Faster access to my results |
| `h` | Seeing the same provider each time |

## q33

Prompt: What is your age band?

- Construct: `age_band`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | 18–24 |
| `b` | 25–34 |
| `c` | 35–44 |
| `d` | 45–54 |
| `e` | 55–64 |
| `f` | 65–74 |
| `g` | 75 or older |

## q34

Prompt: What is your gender?

- Construct: `gender`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Woman |
| `b` | Man |
| `c` | Non-binary |
| `d` | Prefer to self-describe |
| `e` | Prefer not to say |

## q35

Prompt: What is your race or ethnicity? (Select all that apply)

- Construct: `race_ethnicity_select_all_that`
- Type: `multi_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | White |
| `b` | Black or African American |
| `c` | Hispanic or Latino/a |
| `d` | Asian |
| `e` | American Indian or Alaska Native |
| `f` | Native Hawaiian or Other Pacific Islander |
| `g` | Middle Eastern or North African |
| `h` | Prefer not to say |

## q36

Prompt: What is your household's annual income before taxes?

- Construct: `household_s_annual_income_before`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Under $25,000 |
| `b` | $25,000 to $49,999 |
| `c` | $50,000 to $74,999 |
| `d` | $75,000 to $99,999 |
| `e` | $100,000 to $149,999 |
| `f` | $150,000 or more |
| `g` | Prefer not to say |

## q37

Prompt: What is the highest level of education you have completed?

- Construct: `highest_level_education_have_completed`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Less than high school |
| `b` | High school diploma or GED |
| `c` | Some college, no degree |
| `d` | Associate degree |
| `e` | Bachelor's degree |
| `f` | Graduate or professional degree |

## q38

Prompt: What is your current employment status?

- Construct: `current_employment_status`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Employed full-time |
| `b` | Employed part-time |
| `c` | Self-employed |
| `d` | Unemployed and looking for work |
| `e` | Retired |
| `f` | Student |
| `g` | Homemaker or caregiver |
| `h` | Unable to work |

## q39

Prompt: Including yourself, how many people live in your household? Please enter a number.

- Construct: `including_yourself_many_people_live`
- Type: `free_text`
- Required: `true`

Respond in a short free-text answer.

## q40

Prompt: What is your marital or relationship status?

- Construct: `marital_relationship_status`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Single, never married |
| `b` | Married |
| `c` | Living with a partner |
| `d` | Divorced or separated |
| `e` | Widowed |
| `f` | Prefer not to say |

## q41

Prompt: Which U.S. region do you live in?

- Construct: `u_s_region_live`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Northeast |
| `b` | Midwest |
| `c` | South |
| `d` | West |
| `e` | Outside the United States |

## q42

Prompt: How would you describe the area where you live?

- Construct: `would_describe_area_where_live`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Urban |
| `b` | Suburban |
| `c` | Rural |

## q43

Prompt: What is your current health insurance situation?

- Construct: `current_health_insurance_situation`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Employer-sponsored insurance |
| `b` | Insurance purchased on my own or through the marketplace |
| `c` | Medicare |
| `d` | Medicaid |
| `e` | Military or veterans coverage |
| `f` | Uninsured |
| `g` | Prefer not to say |

## q44

Prompt: In general, how would you rate your overall health?

- Construct: `general_would_rate_overall_health`
- Type: `single_choice`
- Required: `true`

| choice_id | label |
|-----------|-------|
| `a` | Excellent |
| `b` | Very good |
| `c` | Good |
| `d` | Fair |
| `e` | Poor |