challenge_3_1_sample_solution = """
Prompt:
Here is the transcript of a customer service call:

<call_log>
{CALL_LOG}
</call_log>

Please carefully analyze the transcript above, focusing on how the customer's sentiment evolves from
the beginning of the call to the end as the agent works to address their issue.

Think through your analysis step-by-step in a <scratchpad>:
- Break the call down into four equal segments
- For each segment, describe the key events and interactions that occur
- Assess the customer's sentiment during that segment
- Compare the customer's sentiment in the 4th quarter of the call to the 1st quarter and determine
if it improved or worsened

After you've thought it through, please provide your final analysis in the following JSON format:

<json>
{{
  "quarter1": {{
    "sentiment": "",
    "call_summary": ""
  }},
  "quarter2": {{
    "sentiment": "",
    "call_summary": ""
  }},
  "quarter3": {{
    "sentiment": "",
    "call_summary": ""
  }},
  "quarter4": {{
    "sentiment": "",
    "call_summary": ""
  }},
  "sentiment_change": "",
  "action_items": []
}}
</json>

The JSON should contain these elements:
- quarter1 through quarter4: Sentiment analysis and summary for each quarter of the call
- sentiment_change: An assessment of whether the customer's sentiment improved or worsened from the
1st to 4th quarter
- action_items: A list of any next steps or action items mentioned on the call to resolve the
customer's issue

Enclose your final JSON output in <result> tags. Remember, do not modify the input call log in any
way. Simply analyze it and provide your findings in the specified JSON format.
"""

challenge_3_2_sample_solution = """
Please carefully review the following call center transcript between a customer and a claims agent:

<call_log>
{CALL_LOG}
</call_log>

After reviewing the call log, reflect on what you think the Agent handled well during the
interaction. Provide your thoughts inside <reflection_positive> tags.

Next, reflect on areas where you believe the Agent could have done better or opportunities the Agent
missed to provide better service to the customer. Provide your thoughts inside <reflection_improve>
tags.

Finally, summarize the key things the Agent could have done differently to improve the service
provided on this call. Provide your summary inside <summary> tags.
"""

challenge_3_3_sample_solution = """
Here is the transcript of a call between a customer and a claims support agent:

<call_log>
{CALL_LOG}
</call_log>

Please read through the call log carefully. After you have finished reading, write a concise summary
of the key points from the call inside <summary> tags.

Then, analyze the details of the call to determine the most appropriate next steps for the support
agent to take in order to resolve the customer's issue or answer their question. Consider what
information may still need to be gathered, what actions should be taken, or what the customer should
expect next.

List out these next steps in a clear numbered list inside <next_steps> tags. Each step should be
specific and actionable.

Provide your summary and next steps analysis for this call log.
"""

